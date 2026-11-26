#!/usr/bin/env python3
"""Comprobación de seguridad estática y aislamiento de secretos para BioPeat."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILS = []


def fail(msg):
    FAILS.append(msg)
    print("  ✗", msg)


def ok(msg):
    print("  ✓", msg)


def main():
    print("Comprobaciones de seguridad de BioPeat")

    # 1. CSP en index.html e inicio.html
    for name in ("index.html", "inicio.html"):
        text = (ROOT / name).read_text(encoding="utf-8")
        m = re.search(r'<meta[^>]+http-equiv=["\']Content-Security-Policy["\'][^>]+content="([^"]+)"', text, re.I)
        if not m:
            fail(f"{name}: falta meta Content-Security-Policy")
            continue
        csp = m.group(1)
        for req in ("default-src 'self'", "worker-src 'self'", "manifest-src 'self'", "object-src 'none'", "base-uri 'self'", "form-action 'self'"):
            if req not in csp:
                fail(f"{name}: CSP sin directiva '{req}'")
        if re.search(r"unsafe-eval", csp, re.I):
            fail(f"{name}: CSP no debe permitir 'unsafe-eval'")
        ok(f"{name}: CSP verificada")

    # 2. Prohibido eval / new Function / document.write en código fuente
    code_files = [
        ROOT / "index.html",
        ROOT / "inicio.html",
        ROOT / "sw.js",
        ROOT / "assets" / "data.js",
        ROOT / "assets" / "app.js",
        ROOT / "assets" / "i18n-en.js",
        ROOT / "cloudflare" / "worker.js",
    ]
    for p in code_files:
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8")
        if re.search(r"(?<![.\w$])eval\s*\(", txt):
            fail(f"{p.name}: contiene eval()")
        if re.search(r"new\s+Function\s*\(", txt):
            fail(f"{p.name}: contiene new Function()")
        if re.search(r"document\.write(?:ln)?\s*\(", txt):
            fail(f"{p.name}: contiene document.write()")
    ok("Sin eval(), new Function() ni document.write()")

    # 3. Aislamiento de claves IA y clave de respaldo en storableState / portable
    idx = (ROOT / "assets" / "app.js").read_text(encoding="utf-8")
    m_st = re.search(r"function storableState\(\)\{[\s\S]*?\n\}", idx)
    m_pt = re.search(r"(?:async\s+)?function portable\(\)\{[\s\S]*?\n\}", idx)
    m_cb = re.search(r"function buildCloudBundle\(\)\{[\s\S]*?\n\}", idx)
    for fn_name, m in (("storableState", m_st), ("portable", m_pt), ("buildCloudBundle", m_cb)):
        if not m:
            fail(f"index.html: no se encontró {fn_name}()")
            continue
        body = m.group(0)
        if "biopeat_ai24" in body or "SYNC_KEY_STORE" in body or "bp_sync_key" in body:
            fail(f"{fn_name}() hace referencia a claves privadas")
    if "stripProto" not in idx:
        fail("index.html: falta helper anti prototype-pollution stripProto()")
    ok("Claves IA/E2EE aisladas de storableState(), portable() y buildCloudBundle()")

    # 4. Cloudflare Worker: auth en tiempo constante, SQL parametrizado y headers
    wk = (ROOT / "cloudflare" / "worker.js").read_text(encoding="utf-8")
    if "timingSafeStrEqual" not in wk:
        fail("cloudflare/worker.js: falta timingSafeStrEqual")
    if re.search(r"\.prepare\s*\(\s*`[^`]*\$\{", wk):
        fail("cloudflare/worker.js: posible interpolación SQL en prepare()")
    for hdr in ("Strict-Transport-Security", "X-Content-Type-Options", "X-Frame-Options", "Referrer-Policy"):
        if hdr not in wk:
            fail(f"cloudflare/worker.js: falta cabecera {hdr}")
    if "adminHtml" in wk and "X-Robots-Tag" not in wk:
        fail("cloudflare/worker.js: /admin sin X-Robots-Tag noindex")
    ok("cloudflare/worker.js: SQL parametrizado, comparación constante y cabeceras presentes")

    # 5. Secretos e historial / gitignore
    gi = (ROOT / ".gitignore").read_text(encoding="utf-8") if (ROOT / ".gitignore").exists() else ""
    if ".biopeat-admin-key.txt" not in gi:
        fail(".gitignore: falta excluir .biopeat-admin-key.txt")
    if (ROOT / ".git").exists():
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
        if ".biopeat-admin-key.txt" in tracked:
            fail("CRÍTICO: .biopeat-admin-key.txt está rastreado por git")
        secret_pats = [
            ("Google API key", re.compile(r"AIza[0-9A-Za-z\-_]{30,}")),
            ("Token Sk/OpenAI/Groq", re.compile(r"\b(?:sk-|gsk_|ghp_)[0-9A-Za-z\-_]{20,}")),
            ("Private Key PEM", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
        ]
        for rel in tracked:
            fp = ROOT / rel
            if not fp.is_file() or fp.suffix.lower() in {".png", ".jpg", ".ico", ".webp"}:
                continue
            txt = fp.read_text(encoding="utf-8", errors="ignore")
            for label, pat in secret_pats:
                if pat.search(txt):
                    fail(f"Posible secreto ({label}) en archivo rastreado: {rel}")
    ok("Sin secretos rastreados ni fugas de .biopeat-admin-key.txt")

    if FAILS:
        print(f"\nFALLOS DE SEGURIDAD ({len(FAILS)}):")
        for f in FAILS:
            print(" -", f)
        sys.exit(1)
    print("\nSEGURIDAD OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
