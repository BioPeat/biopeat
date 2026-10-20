with open('verify.js', 'r') as f:
    verify_content = f.read()

verify_content = verify_content.replace('matchMedia: () => ({ matches: false, addEventListener: () => {} })', 'matchMedia: () => ({ matches: false, addEventListener: () => {} })')
# we need to make sure matchMedia is global
verify_content = verify_content.replace('vm.createContext(sandbox);', 'sandbox.matchMedia = sandbox.window.matchMedia; vm.createContext(sandbox);')

with open('verify.js', 'w') as f:
    f.write(verify_content)
