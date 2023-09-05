-- list sequences
select sequence_schema, sequence_name from information_schema.sequences;

-- get sequence name
select pg_get_serial_sequence('__table_name__', '__column_name__');

-- get sequence properties
SELECT * FROM __sequence_name__;

-- get sequence current value (and increment self)
nextval('__sequence_name__'::regclass)

-- get the last ID
SELECT MAX(__column_name__) FROM __table_name__;

-- set sequence value
ALTER SEQUENCE __sequence_name__ RESTART WITH 666;
