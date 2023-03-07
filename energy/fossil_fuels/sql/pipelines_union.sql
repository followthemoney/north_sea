--ALTER TABLE uk_pipeline_freespans ADD COLUMN pipeline_type text;
UPDATE uk_pipeline_freespans SET pipeline_type = 'Unknown';
--ALTER TABLE uk_pipeline_freespans ADD COLUMN status text;
UPDATE uk_pipeline_freespans SET status = 'Unknown';
--ALTER TABLE uk_pipeline_freespans ADD COLUMN fluid text;
UPDATE uk_pipeline_freespans SET fluid = 'Unknown';
--ALTER TABLE uk_pipeline_freespans ADD COLUMN descriptio text;
UPDATE uk_pipeline_freespans SET descriptio = 'Unknown';
--ALTER TABLE uk_pipelines_linear_removed ADD COLUMN fluid text;
UPDATE uk_pipelines_linear_removed SET fluid = 'Unknown';
--ALTER TABLE uk_pipeline_freespan_removed ADD COLUMN fluid text;
UPDATE uk_pipeline_freespan_removed SET fluid = 'Unknown';

CREATE TABLE all_pipelines AS

SELECT *, ROW_NUMBER() OVER() AS pk_pipeline FROM

((SELECT
	ST_Transform(nl1.geometry, 25831) AS geometry
	, nl1.leid_nr AS pipeline_id
	, concat_ws('-', trace_van, trace_tot) AS pipeline_name
	, nl1."type" AS pipeline_type
	, nl1."operator" AS pipeline_operator
	, nl1.status AS status
	, nl1.stofnaam AS commodity
	, nl1.opmerking AS remarks
	, nl1.since AS start_date
  	, TO_DATE(nl1.until, 'YYYYMMDD') AS end_date
FROM
  	nl_pipelines nl1)
 UNION
 (SELECT
	ST_Transform(no1.geometry, 25831) AS geometry
	, CAST(no1.pplnpdidpipeline AS text) AS pipeline_id
	, no1.pplname AS pipeline_name
	, no1.pplmaingroupingname AS pipeline_type
	, no1.cmplongname AS pipeline_operator
	, no1.pplcurrentphase AS status
	, no1.pplmedium AS commodity
	, concat_ws('-', no1.fclnamefrom, no1.fclnameto, no1.pplbelongstoname) AS remarks
	, no1.pplcurrentphasefromdate AS start_date
  	, no1.ppldateupdated AS end_date
FROM no_pipeline_thin no1)
UNION
(SELECT
	ST_TRANSFORM(u1.geometry, 25831) AS geometry
	, u1.feature_id AS pipeline_id
	, u1.pipe_name AS pipeline_name
	, u1.inf_type AS pipeline_type
	, u1.rep_group AS pipeline_operator
	, u1.status AS status
	, u1.fluid AS commodity
	, u1.descriptio AS remarks
	, TO_DATE(u1.start_date, 'YYYYMMDD') AS start_date
 	, TO_DATE(u1.end_date, 'YYYYMMDD') AS end_date
FROM uk_pipelines_linear u1)
UNION
 (SELECT 
 ST_TRANSFORM(u2.geometry, 25831) AS geometry
	, u2.feature_id AS pipeline_id
	, u2.pipe_name AS pipeline_name
	, u2.pipeline_type AS pipeline_type
	, u2.rep_group AS pipeline_operator
	, u2.status AS status
	, u2.fluid AS commodity
	, u2.descriptio AS remarks
	, TO_DATE(u2.start_date, 'YYYYMMDD') AS start_date
  	, TO_DATE(u2.end_date, 'YYYYMMDD') AS end_date
FROM uk_pipeline_freespans u2)
UNION
 (SELECT
 ST_TRANSFORM(u3.geometry, 25831) AS geometry
	, u3.feature_id AS pipeline_id
	, u3.name AS pipeline_name
	, u3.inf_type AS pipeline_type
	, u3.rep_group AS pipeline_operator
	, u3.status AS status
	, u3.fluid AS commodity
	, u3.descriptio AS remarks
	, to_timestamp(u3.start_date::bigint / 1000) AS start_date
  	, to_timestamp(u3.end_date::bigint / 1000) AS end_date
FROM uk_pipelines_linear_removed u3
)
UNION
  (SELECT
  ST_TRANSFORM(u4.geometry, 25831) AS geometry
	, u4.feature_id AS pipeline_id
	, u4.name AS pipeline_name
	, u4.inf_type AS pipeline_type
	, u4.rep_group AS pipeline_operator
	, u4.status AS status
	, u4.fluid AS commodity
	, u4.descriptio AS remarks
	, to_timestamp(u4.start_date::bigint / 1000) AS start_date
  	, to_timestamp(u4.end_date::bigint / 1000) AS end_date
FROM uk_pipeline_freespan_removed u4 )

) AS all_pipelines;

ALTER TABLE all_pipelines ADD CONSTRAINT pk_pipeline PRIMARY KEY (pk_pipeline);
CREATE INDEX idx_pipelines ON all_pipelines USING gist (geometry);