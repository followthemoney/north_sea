CREATE TABLE all_current_licences AS

SELECT *, ROW_NUMBER() OVER() AS pk_current_licences FROM

((SELECT
	ST_TRANSFORM(geometry, 25831) AS geometry
	, l.licence_dbk AS licence_id
	, l.licence_nm AS licence_name
	--, l.licence_type AS licence_type
	, l.operator AS licence_operator
	--, l.licensees AS licensees
	, l.status AS status
	--, l.resource_nm AS commodity
  	, nh.start_date AS start_date
	FROM nl_licences_current l
	INNER JOIN nl_licence_hist nh
	ON nh.licence_normalized = l.licence_nm)

UNION
(SELECT

	ST_TRANSFORM(geometry, 25831) AS geometry
	, no_licence."prlnpdidlicence" AS licence_id
	, no_licence."prlname" AS licence_name
	--, no_licence."wlbwWelltype" AS licence_type
	, no_licence."cmplongname" AS licence_operator
	, no_licence."prlstatus" AS status
	--, no_licence."wlbcontent" AS commodity
	, no_licence."prldategranted" AS start_date

FROM no_licence)
UNION
(SELECT

	ST_TRANSFORM(geometry, 25831) AS geometry
	, uk_licences.licno AS licence_id
	, uk_licences.licref AS licence_name
	--, uk_licences.lictype AS licence_type
	, uk_licences.suboporg AS licence_operator
	, uk_licences.licstatus AS status
	--, uk_licences.flowclass AS commodity
	, uk_licences.licstartdt AS start_date
FROM
	uk_licences
WHERE
	uk_licences.location = 'OFFSHORE')) AS all_current_licences;
	
ALTER TABLE all_current_licences ADD CONSTRAINT pk_current_licences PRIMARY KEY (pk_current_licences);
CREATE INDEX idx_current_licences ON all_current_licences USING gist (geometry);