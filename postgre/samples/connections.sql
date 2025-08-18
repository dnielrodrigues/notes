-- CLOSE ALL CONNECTIONS
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'intranet_v3'  -- Replace for DB name or remove for all
  AND pid <> pg_backend_pid();  -- Don't close your own connection
