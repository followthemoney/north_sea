ALTER TABLE all_infrastructure_points ADD COLUMN status_normalised text;
UPDATE all_infrastructure_points SET status_normalised = status;

UPDATE all_infrastructure_points 
SET status_normalised = upper(status_normalised);

--Update status
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'ABANDONED', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'AOC CANCELLED', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'OPERATIONAL', 'ACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'PROPOSED', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'AOC OK', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'DECOMMISSIONED', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'REMOVED', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'PRECOMMISSIONED', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'CLOSED DOWN', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'IN QUEUE FOR AOC', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'UNDER CONSTRUCTION', 'INACTIVE');
UPDATE all_infrastructure_points SET status_normalised = REGEXP_REPLACE(status_normalised, 'NOT IN USE', 'INACTIVE');