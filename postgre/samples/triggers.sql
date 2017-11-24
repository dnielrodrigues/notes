
-- trigger procedure
--------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION my_procedure() RETURNS TRIGGER AS $$
DECLARE
	my_var int;

BEGIN

	my_var := ( SELECT 1 );
	IF( my_var = 0 ) THEN
		RAISE NOTICE "deu merda...";
		RETURN NULL;
	END IF;
	RETURN NEW;
END;

$$ LANGUAGE plpgsql;



-- trigger declare
--------------------------------------------------------------------------------
CREATE TRIGGER my_trigger
	AFTER INSERT OR UPDATE OR DELETE ON table_name
	FOR EACH ROW EXECUTE PROCEDURE
	my_procedure();


