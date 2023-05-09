CREATE TABLE all_fields AS

SELECT *, ROW_NUMBER() OVER() AS pk_field FROM

((SELECT
	ST_Transform(nl.geometry, 25831) AS geometry,
	nl.field_name AS field_name,
	nl.result AS commodity,
	nl.status AS status,
	nl."operator" AS field_operator,
	nl.lic_area AS licence
FROM
	nl_fields nl
WHERE
	"landsea" = 'Sea')
UNION
(SELECT
	ST_Transform(no.geometry, 25831) AS geometry,
 	no.fldname" AS field_name,
 	no.fldhctype" AS commodity,
 	no.fldcurrentactivitystatus" AS status,
 	no.cmplongname" AS field_operator,
 	no.fldownernName" AS licence
 FROM
 	no_field no)
UNION
(SELECT
	ST_Transform(uk.geometry, 25831) AS geometry,
	uk.fieldname AS field_name,
	uk.fieldtype AS commodity,
	uk.status AS status,
	uk.curr_oper AS field_operator,
	uk.orig_lic AS licence
FROM
	uk_offshore_fields uk)
) AS all_fields;

ALTER TABLE all_fields ADD CONSTRAINT pk_field PRIMARY KEY (pk_field);
CREATE INDEX idx_fields ON all_fields USING gist (geometry);