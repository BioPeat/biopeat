-- BioPeat Cloudflare D1 Schema (EU jurisdiction)
CREATE TABLE IF NOT EXISTS vaults (
  vault_id TEXT PRIMARY KEY,
  auth_hash TEXT NOT NULL,
  iv TEXT NOT NULL,
  ciphertext TEXT NOT NULL,
  compressed INTEGER NOT NULL DEFAULT 1,
  rev INTEGER NOT NULL DEFAULT 1,
  size_bytes INTEGER NOT NULL DEFAULT 0,
  app_version TEXT DEFAULT '',
  updated_at INTEGER NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS feedback (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  category TEXT NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  app_version TEXT DEFAULT '',
  lang TEXT DEFAULT 'es',
  view_name TEXT DEFAULT '',
  device TEXT DEFAULT '',
  origin TEXT DEFAULT '',
  status TEXT NOT NULL DEFAULT 'new',
  ai_notes TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS analytics_daily (
  day TEXT NOT NULL,
  metric TEXT NOT NULL,
  count INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (day, metric)
);

CREATE TABLE IF NOT EXISTS active_visitors_daily (
  day TEXT NOT NULL,
  visitor_hash TEXT NOT NULL,
  surface TEXT NOT NULL,
  PRIMARY KEY (day, visitor_hash, surface)
);

CREATE TABLE IF NOT EXISTS rate_limits (
  bucket TEXT PRIMARY KEY,
  hits INTEGER NOT NULL DEFAULT 0,
  expires_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_feedback_status_created ON feedback(status, created_at);
CREATE INDEX IF NOT EXISTS idx_vaults_updated ON vaults(updated_at);
CREATE INDEX IF NOT EXISTS idx_visitors_day ON active_visitors_daily(day);
CREATE INDEX IF NOT EXISTS idx_rate_limits_expires ON rate_limits(expires_at);
