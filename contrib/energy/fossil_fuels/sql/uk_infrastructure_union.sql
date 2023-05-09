CREATE TABLE uk_infrastructure_points AS

SELECT *, ROW_NUMBER() OVER() AS object_id FROM

((SELECT 
 	u1.name
	, u1.inf_type AS infrastructure_type
	, u1.rep_group AS "operator"
	, u1.descriptio AS description
	, u1.status
	, u1.comments
 	, TO_DATE(u1.start_date, 'YYYYMMDD') AS start_date
 	, TO_DATE(u1.end_date, 'YYYYMMDD') AS end_date
  	, u1.feature_id
 	, u1.geometry
FROM uk_subsea_points u1)
UNION
(SELECT
 	u2.name
	, u2.inf_type AS infrastructure_type
	, u2.rep_group AS "operator"
	, u2.descriptio AS description
	, u2.status
	, u2.comments
 	, to_timestamp(u2.start_date::bigint/ 1000) AS start_date
 	, to_timestamp(u2.end_date::bigint / 1000) AS end_date
 	, u2.feature_id
 	, u2.geometry
 FROM uk_subsea_points_removed u2
)

UNION 
(SELECT
	u3.name
	, u3.inf_type AS infrastructure_type
	, u3.rep_group AS "operator"
	, u3.descriptio AS description
	, u3.status
	, u3.comments
 	, to_timestamp(u3.start_date::bigint/ 1000) AS start_date
 	, to_timestamp(u3.end_date::bigint / 1000) AS end_date
 	, u3.feature_id
 	, u3.geometry
 FROM uk_surface_points_removed u3
) 
UNION
 (SELECT 
  	u4.name
	, u4.inf_type AS infrastructure_type
	, u4.rep_group AS "operator"
	, u4.descriptio AS description
	, u4.status
	, u4.comments
 	, TO_DATE(u4.start_date, 'YYYYMMDD') AS start_date
 	, TO_DATE(u4.end_date, 'YYYYMMDD') AS end_date
  	, u4.feature_id
 	, u4.geometry
 FROM uk_surface_points u4
)
UNION
 (SELECT
 	u5.name
  	, u5.inf_type
  	, u5.rep_group AS "operator"
  	, u5.descriptio AS description
  	, u5.status
  	, u5.comments
  	, TO_DATE(u5.start_date, 'YYYYMMDD') AS start_date
 	, TO_DATE(u5.end_date, 'YYYYMMDD') AS end_date
  	, u5.feature_id
  	, u5.geometry
FROM uk_pipeline_points u5)
) AS uk_infrastructure_points;

ALTER TABLE uk_infrastructure_points ADD CONSTRAINT object_id PRIMARY KEY (object_id);
CREATE INDEX idx_uk_infrastructure_points ON uk_infrastructure_points USING gist (geometry);