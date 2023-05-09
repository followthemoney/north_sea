--TODO: look at geometry of no_wellbore. Transformation gives an error
--No I'm using two geometries. It shouldn't matter that much, maybe an error 
--of a few meters tops, but this should be improved

CREATE TABLE all_wellbores AS

SELECT *, ROW_NUMBER() OVER() AS pk_wellbore FROM

((SELECT
	ST_Transform(nl_wellbores.geometry, 23032) AS geometry
	, CAST(nl_wellbores."OBJECTID" AS text) AS wellbore_id
	, nl_wellbores."IDENTIFICATION" AS wellbore_name
	, nl_wellbores."WELL_TYPE" AS wellbore_type
	, nl_wellbores."OPERATOR" AS wellbore_operator
	, nl_wellbores."STATUS" AS status
	, nl_wellbores."WELL_RESULT" AS commodity
	, nl_wellbores."START_DATE_DRILLING" AS start_date
FROM
	nl_wellbores)
UNION
(SELECT
	ST_Transform(no_wellbore.geometry, 23032)
 	, CAST(no_wellbore."wlbNpdidWellbore" AS text) AS wellbore_id
	, no_wellbore."wlbWellboreName" AS wellbore_name
	, no_wellbore."wlbWellType" AS wellbore_type
	, no_wellbore."wlbDrillingOperator" AS wellbore_operator
	, no_wellbore."wlbStatus" AS status
	, no_wellbore."wlbContent" AS commodity
	, no_wellbore."wlbCompletionDate" AS start_date
FROM
 	no_wellbore)
UNION
(SELECT
	ST_Transform(uk_wells.geometry, 23032)
 	, CAST(uk_wells."WELLREGNO" AS text) AS wellbore_id
	, uk_wells."WELLREGNO" AS wellbore_name
	, uk_wells."CURRWELLIN" AS wellbore_type
	, uk_wells."SUBAREAOP" AS wellbore_operator
	, uk_wells."COMPLESTAT" AS status
	, uk_wells."FLOWCLASS" AS commodity
	, TO_DATE(uk_wells."SPUDDATE", 'YYYY-MM-DD') AS start_date
FROM
	uk_wells)) AS all_wellbores;

ALTER TABLE all_wellbores ADD CONSTRAINT pk_wellbore PRIMARY KEY (pk_wellbore);
CREATE INDEX idx_wellbores ON all_wellbores USING gist (geometry);