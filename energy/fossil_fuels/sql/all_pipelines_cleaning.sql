ALTER TABLE all_pipelines ADD COLUMN commodity_normalised text;
UPDATE all_pipelines SET commodity_normalised = commodity;

ALTER TABLE all_pipelines ADD COLUMN status_normalised text;
UPDATE all_pipelines SET status_normalised = status;

ALTER TABLE all_pipelines ADD COLUMN type_normalised text;
UPDATE all_pipelines SET type_normalised = pipeline_type;

UPDATE all_pipelines 
SET status_normalised = upper(status_normalised),
	commodity_normalised = upper(commodity_normalised),
	type_normalised = upper(type_normalised);

--Update commodity
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS/OLIE', 'GAS AND OIL');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS/OIL', 'GAS AND OIL');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OLIE', 'OIL');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'ONBEKEND', 'UNKNOWN');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'RIOOLWATER', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'KOELWATER', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'RIOOLSLIB', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'NO VALUE', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OTHER FLUID', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'FIBRE', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'HYDRAULIC', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'METHANOL', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'WATER', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'MIXED HYDROCARBONS', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'CONTROL', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GLYCOL', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'INJECTION', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'UNKNOWN', 'OTHER');
UPDATE all_pipelines SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'CHEMICAL', 'OTHER');

--Update status
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'ABANDONED IN PLACE', 'INACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'DECOMMISSIONED', 'INACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'IN SERVICE', 'ACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'PROPOSED', 'INACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'ABANDONED', 'INACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'NOT IN USE', 'INACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'REMOVED', 'INACTIVE');
UPDATE all_pipelines SET status_normalised = REGEXP_REPLACE(status_normalised, 'PRECOMMISSIONED', 'INACTIVE');

--Update type
UPDATE all_pipelines SET type_normalised = REGEXP_REPLACE(type_normalised, 'PIJPLEIDING', 'PIPELINE');
UPDATE all_pipelines SET type_normalised = REGEXP_REPLACE(type_normalised, 'MONITOR BUOY', 'BUOY');
UPDATE all_pipelines SET type_normalised = REGEXP_REPLACE(type_normalised, 'TRANSPORTATION', 'PIPELINE');
UPDATE all_pipelines SET type_normalised = REGEXP_REPLACE(type_normalised, 'UMBILICAL', 'PIPELINE');
