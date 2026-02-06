-- CHECK POSTGRE VERSION
SELECT version();

-- SHOW TABLE DETAILS (FIELDS, CONSTRAITS, ETC)
\d __table_name__;

-- SELECT
SELECT * FROM scheme_name.table_name WHERE sample_name ILIKE '%joao%';

-- CREATE
INSERT INTO scheme_name.table_name (id, nome, etc) VALUES(nextval('table_name_tbn_id_seq'::regclass), 'Sample', 'Etc...');

-- UPDATE
UPDATE scheme_name.table_name SET nome='Maria' WHERE id=666;

-- DELETE
DELETE FROM scheme_name.table_name WHERE id=666;

-- MERGE
MERGE INTO scheme_name.table_name AS tgt USING SOURCE_TABLE AS src
ON (tgt.id=src.id) WHEN MATCHED THEN UPDATE SET tgt.nome=src.nome
WHEN NOT MATCHED THEN INSERT (nome) VALUES (src.nome);

-- RENAME DATABASE
ALTER DATABASE current_name RENAME TO new_name;
