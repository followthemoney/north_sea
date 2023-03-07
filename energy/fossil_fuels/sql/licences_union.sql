CREATE TABLE licences_all AS

SELECT *, ROW_NUMBER() OVER() AS pk_licence FROM

((SELECT 
  	geometry,
  	licence_name,
  	licence_type,
  	licensees,
  	licences_nl.operator AS licence_operator,
 	status,
  	'1970' AS start_year
  FROM licences_nl)
 
UNION
 
 (SELECT
  	geometry,
  	licence_name,
  	'PRODUCTION' AS licence_type,
  	'UNKNOWN' AS licensees,
  	licences_no.operator_ AS licence_operator,
  	status,
  	CAST((EXTRACT(year from start_date)) AS text) AS start_year
  FROM licences_no)
 
 UNION
 
 (SELECT
 	geometry,
  	licence_name,
    licence_type,
  	licensees,
  	licences_uk.operator AS licence_operator,
 	status,
  	CAST((EXTRACT(year from start_date)) AS text) AS start_year
  FROM licences_uk)
  	) AS licences_all;

ALTER TABLE licences_all ADD CONSTRAINT pk_licence PRIMARY KEY (pk_licence);
CREATE INDEX idx_licences ON licences_all USING gist (geometry);