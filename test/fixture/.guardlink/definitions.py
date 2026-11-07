# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GuardLink Shared Definitions — notes-api
#
# ALL @asset, @threat, and @control declarations live here.
# Source files reference by #id only (e.g. @mitigates X against #sqli).
# Never redeclare an ID that exists in this file.
# Before adding: read this file to check for duplicates.
#
# Run: guardlink validate .
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ─── Examples (uncomment and customize for your project) ────────
#
#   # @asset App.API (#api) -- "Main REST endpoint"
#   # @asset App.Database (#db) -- "Primary data store"
#
#   # @threat SQL_Injection (#sqli) [critical] cwe:CWE-89 -- "Unsanitized input reaches SQL query"
#   # @threat Cross_Site_Scripting (#xss) [high] cwe:CWE-79 -- "Unsanitized input rendered in browser"
#   # @threat Broken_Access_Control (#bac) [critical] cwe:CWE-284 -- "Missing or bypassable authorization"
#
#   # @control Parameterized_Queries (#prepared-stmts) -- "SQL queries use bound parameters"
#   # @control Input_Validation (#input-validation) -- "Input validated against schema/allowlist"
#   # @control RBAC (#rbac) -- "Role-based access control"
#
# ─── Your Definitions ──────────────────────────────────────────


# @asset Notes.API (#api) -- "The Flask HTTP API"
# @asset Notes.Database (#db) -- "SQLite file holding every note"
# @threat SQL_Injection (#sqli) [critical] cwe:CWE-89 -- "Request input reaches a SQL query"
# @threat Command_Injection (#cmdi) [critical] cwe:CWE-78 -- "Request input reaches a shell command"
# @control Bound_Parameters (#bound-params) -- "SQL values are passed as bound parameters"
