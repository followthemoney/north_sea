--For now I have chosen to use the emodnet platform data for Denmark, Germany and the Netherlands.
--This data is a bit sparse though, only using platforms and not other infrastructure.
--I still have to look for those files though.

CREATE TABLE all_infrastructure_points AS

--ALTER TABLE no_facility ADD COLUMN end_date date;
--UPDATE no_facility SET end_date = NULL;

SELECT *, ROW_NUMBER() OVER() AS object_id FROM

((SELECT
  uk1.name
  , uk1.inf_type
  , uk1.operator
  , uk1.description
  , uk1.status
  , uk1.comments
  , uk1.start_date
  , uk1.end_date
  , uk1.feature_id
  , ST_Transform(uk1.geometry, 23032) AS geometry

FROM uk_infrastructure_points uk1)

UNION
 
 (SELECT
  no1.fclname AS "name"
  , no1.fclkind AS inf_type
  , no1.fclcurrentoperatorname AS "operator"
  , no1.fclfunctions AS description
  , no1.fclstatus AS status
  , no1.fclfactpageurl AS "comments"
  , no1.fclstartupdate AS startdate
  , no1.end_date AS end_date
  , no1.fclnpdidfacility::text AS feature_id
  , ST_Transform(no1.geometry, 23032) AS geometry
  
FROM no_facility no1)
 
UNION
 
 (SELECT
  int.name
  , int.category AS inf_type
  , int.operator 
  , int.function AS description
  , int.current_status AS status
  , int.remarks AS "comments"
  , TO_DATE(int.production_start, 'DD/MM/YYYY') AS start_date
  , TO_DATE(int.valid_to, 'DD/MM/YYYY') AS end_date
  , int.platformid AS feature_id
  , ST_Transform(int.geometry, 23032) AS geometry
FROM int_platforms int
WHERE country IN ('Netherlands', 'Denmark', 'Germany'))
 ) AS all_infrastructure_points;
 
ALTER TABLE all_infrastructure_points ADD CONSTRAINT infrastructure_object_id PRIMARY KEY (object_id);
CREATE INDEX idx_all_infrastructure_points ON all_infrastructure_points USING gist (geometry);
 
