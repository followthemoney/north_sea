--Script for cleaning values in commodity and status columns


--Create normalised commodity column
ALTER TABLE all_fields ADD COLUMN commodity_normalised text;
UPDATE all_fields SET commodity_normalised = commodity;

--Create normalised status column
ALTER TABLE all_fields ADD COLUMN status_normalised text;
UPDATE all_fields SET status_normalised = status;

UPDATE all_fields SET status_normalised = upper(status);
UPDATE all_fields SET commodity_normalised = upper(commodity);

UPDATE all_fields SET status = upper(status);
UPDATE all_fields SET commodity = upper(commodity);

--Clean commodity
UPDATE all_fields SET status = REPLACE(status, 'IN PRODUCTIE', 'PRODUCING');
UPDATE all_fields SET status = REPLACE(status, 'PRODUCTIE GEPLAND > 5 JAAR', 'PRODUCTION PLANNED');
UPDATE all_fields SET status = REPLACE(status, 'PRODUCTIE GEPLAND < 5 JAAR', 'PRODUCTION PLANNED');
UPDATE all_fields SET status = REPLACE(status, 'VERLATEN', 'ABANDONED');
UPDATE all_fields SET status = REPLACE(status, 'UITGEPRODUCEERD', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'TIJDELIJK VERLATEN', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'GAS OPSLAG', 'STORAGE');
UPDATE all_fields SET status = REPLACE(status, 'SHUTDOWN', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'APPROVED FOR PRODUCTION', 'PRODUCTION PLANNED');
UPDATE all_fields SET status = REPLACE(status, 'PRODUCTION CEASED', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'POST-COP', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'PRODUCTION SUSPENDED - POSSIBLE RESERVES REMAIN', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'PRODUCTION CEASED - VENT CONSENT NEEDED', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'UNDER APPRAIS - NO FDP', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'UNDER APPRAI-FUTURE FDP', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'PRODUCTION SUSPENDED', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'SHELVED', 'INACTIVE');
UPDATE all_fields SET status = REPLACE(status, 'NO APPRAISAL', 'INACTIVE');

--Clean status
UPDATE all_fields SET commodity = REPLACE(commodity, 'GAS/CONDENSATE', 'GAS AND CONDENSATE');
UPDATE all_fields SET commodity = REGEXP_REPLACE(commodity, 'COND', 'CONDENSATE');
UPDATE all_fields SET commodity = REGEXP_REPLACE(commodity, 'OLIE EN GAS', 'OIL AND GAS');	
UPDATE all_fields SET commodity = REGEXP_REPLACE(commodity, 'OLIE', 'OIL');
UPDATE all_fields SET commodity = REGEXP_REPLACE(commodity, 'OIL EN GAS', 'OIL AND GAS');
