-- REMEMBER: FIRST CREATE SCHEMA
DO $$ 
DECLARE
    tbl RECORD;
    old_schema varchar = '_old_schema_name_';
    new_schema varchar = '_new_schema_name_';
BEGIN
    FOR tbl IN
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = old_schema
    LOOP
        EXECUTE FORMAT('CREATE TABLE '|| new_schema ||'.%I (LIKE '|| old_schema ||'.%I INCLUDING ALL)', tbl.tablename, tbl.tablename);
        EXECUTE FORMAT('INSERT INTO '|| new_schema ||'.%I SELECT * FROM '|| old_schema ||'.%I', tbl.tablename, tbl.tablename);
    END LOOP;
END $$;
