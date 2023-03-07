CREATE TABLE all_production AS 

SELECT *, ROW_NUMBER() OVER() AS pk_production FROM

((SELECT
	nl.license_name AS field_name
	, nl.operator_name
	, EXTRACT(YEAR FROM nl.date) AS production_year
	, nl.commodity
	, SUM(nl.sm3 / 1000) AS production_1000sm3
FROM
	nl_production_monthly nl
JOIN 
	nl_fields nlg
ON
	nl.license_name = nlg.field_name
WHERE
	nlg.landsea = 'Sea'

GROUP BY
 	nl.license_name
 	, nl.operator_name
 	, EXTRACT(YEAR FROM nl.date)
 	, nl.commodity
)

UNION

(SELECT
	no_.field_name
	, nof.cmplongname AS operator_name
	, EXTRACT(YEAR FROM no_.date) AS production_year
	, no_.commodity
	, SUM(no_.sm3 / 1000) AS production_1000sm3
FROM no_production_monthly no_
LEFT JOIN
	public.no_field nof
ON
	no_.field_name = nof.fldname
GROUP BY
	no_.field_name
	, nof.cmplongname
	, EXTRACT(YEAR FROM no_.date) 
	, no_.commodity
 )
	
UNION

(SELECT
	uk.fieldname AS field_name
	, uk.orggrpnm AS operator_name
	, EXTRACT(YEAR FROM uk.perioddate) AS production_year
	, uk.commodity
	, SUM(uk.sm3 / 1000) AS production_1000sm3
FROM
 	uk_production_monthly uk
WHERE 
	uk.location = 'Offshore'
GROUP BY
 	uk.fieldname
 	, uk.orggrpnm
 	, EXTRACT(YEAR FROM uk.perioddate)
 	, uk.commodity
 )) AS all_production;
 
ALTER TABLE all_production ADD CONSTRAINT pk_production PRIMARY KEY (pk_production);

