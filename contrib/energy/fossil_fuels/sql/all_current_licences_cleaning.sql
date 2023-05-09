ALTER TABLE all_current_licences ADD COLUMN status_normalised text;

UPDATE all_current_licences SET status_normalised = upper(status);

UPDATE all_current_licences SET status = upper(status);

--Clean commodity
UPDATE all_current_licences SET status = REPLACE(status, 'EXTANT', 'ACTIVE');
UPDATE all_current_licences SET status = REPLACE(status, 'ONHERROEPELIJK VAN KRACHT', 'ACTIVE');
UPDATE all_current_licences SET status = REPLACE(status, 'VERLENGD', 'ACTIVE');