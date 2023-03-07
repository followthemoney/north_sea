--Create to normalised columns

ALTER TABLE all_wellbores ADD COLUMN commodity_normalised text;
UPDATE all_wellbores SET commodity_normalised = commodity;

ALTER TABLE all_wellbores ADD COLUMN status_normalised text;
UPDATE all_wellbores SET status_normalised = status;

UPDATE all_wellbores SET status_normalised = upper(status);
UPDATE all_wellbores SET commodity_normalised = upper(commodity);

--Update commodity
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'TECHNISCH MISLUKT', 'UNKNOWN');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OLIE EN GAS', 'OIL AND GAS');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OLIE SHOWS', 'OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OLIE', 'OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'DROOG', 'DRY');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'ZOUT', 'OTHER');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'RIOOLSLIB', 'OTHER');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS SHOWS', 'GAS');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'ONBEKEND', 'UNKNOWN');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'STEENKOOL', 'OTHER');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS MET OLIE SHOWS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OLIE MET GAS SHOWS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OIL/GAS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS/CONDENSATE', 'GAS AND CONDENSATE');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OIL/GAS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'SHOWS', 'UNKNOWN');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'NOT APPLICABLE', 'UNKNOWN');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS MET OLIE SHOWS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS EN OLIE SHOWS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'BRONWATER', 'OTHER');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",' SHOWS', '', 'g');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",' SHOW', '', 'g');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",' WELL', '', 'g');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",' HOLE', '', 'g');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OIL AND GAS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'HYDROCARBON INDICATIONS', 'OTHER');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OIL WITH GAS', 'GAS AND OIL');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'CONDENSATE WITH GAS', 'GAS AND CONDENSATE');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'CONDENSATE WITH OIL', 'OIL AND CONDENSATE');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'CONDENSATE WITH OIL & GAS', 'GAS, OIL AND CONDENSATE');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'OIL WITH CONDENSATE', 'OIL AND CONDENSATE');
UPDATE all_wellbores SET commodity_normalised = REGEXP_REPLACE("commodity_normalised",'GAS WITH OIL', 'GAS AND OIL');


--Update status
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PLUGGED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'CLOSED_IN', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'ABANDONED', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'SUSPENDED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PLUGGED BACK AND SIDETRACKED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'OBSERVING', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PRODUCING/INJECTING', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'P&A', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'JUNKED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'RE-CLASS TO DEV', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'WILL NEVER BE DRILLED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'CLOSED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'BLOWOUT', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'DECOMMISIONED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'CONSTRUCTED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'CONSTRUCTING', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PHASE 3', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PHASE 2', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PHASE 1', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'INACTIVE BACK AND SIDETRACKED', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'COMPLETED \(OPERATING\)', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PRODUCING', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'INJECTING', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'PREDRILLED', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'RE-CLASS TO TEST', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'COMPLETED TO WELL', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'DRILLING', 'ACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'COMPLETED \(SHUT IN\)', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'INACTIVE-IN', 'INACTIVE');
UPDATE all_wellbores SET status_normalised = REGEXP_REPLACE(status_normalised, 'ACTIVE ACTIVE', 'ACTIVE');



