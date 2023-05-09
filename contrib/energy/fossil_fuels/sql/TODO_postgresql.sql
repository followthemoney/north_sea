TODO

-- Clean up dates in UK Data
-- Compile Company cleaning list
-- Check geometry of wellbores
-- Clean Norway yearly production


Production

NL

(SELECT
	nl.licence_name AS field_name
	, nl.operator_name
	, nl.date AS production_date
	, nl.commodity
	, nl.sm3 / 1000 AS production_1000sm3
	, nlg.geometry
FROM
	nl_production_monthly nl
JOIN 
	nl_fields nlg
ON
	nl.licence_name = nlg."FIELD_NAME"
WHERE
	nlg."LANDSEA" = 'Sea')

UNION

(SELECT
	no.field_name
	, nog.cmpLongName AS operator_name
	, no.date AS production_date
	, no.commodity
	, no.sm3 / 1000 AS production_1000sm3
	nog.geometry
FROM no_production_monthly no
JOIN
	no_field nog
ON
	no.field_name = nog."fldName")

UNION

(SELECT
	uk.fieldname AS field_name
	, uk.orggrpnm AS operator_name
	, uk.perioddate AS production_date
	, uk.commodity
	, uk.sm3 / 1000 AS production_1000sm3
	, uk.geometry

)

)