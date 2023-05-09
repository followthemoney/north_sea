CREATE TABLE dt.int_platforms AS

SELECT *, ROW_NUMBER() OVER() AS pk_platform FROM

(SELECT
	country
	, p.platformid
	, p.current_status
	, p.name
	, UPPER(p.category) AS category
	, UPPER(p.operator) AS operator
	, com.name_international AS name_normalised
	, p.primary_production
	, TO_DATE(p.production_start, 'DD/MM/YYYY') AS start_date
	, EXTRACT(YEAR FROM TO_DATE(p.production_start, 'DD/MM/YYYY')) AS start_year
	, TO_DATE(p.valid_to, 'DD/MM/YYYY') AS end_date
	, p.remarks
	, p.geometry
FROM
	public.int_platforms p
LEFT JOIN
	public.company_names com
ON
	UPPER(p.operator) = com.name_db) AS int_platforms;
	
ALTER TABLE dt.int_platforms ADD CONSTRAINT pk_platformid PRIMARY KEY (pk_platform);
CREATE INDEX idx_int_platforms ON dt.int_platforms USING gist (geometry);
