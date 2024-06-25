
SELECT
  event_type,
  event_attributes
FROM `numia-data.injective.injective_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.akash.akash_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.celestia.celestia_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.cosmoshub.cosmoshub_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.dydx_mainnet.dydx_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.injective.injective_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.migaloo.migaloo_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.noble.noble_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.secret.secret_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.stargaze.stargaze_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.stride.stride_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'
UNION ALL
SELECT
  event_type,
  event_attributes
FROM `numia-data.umee.umee_message_events`
WHERE JSON_EXTRACT_SCALAR(event_attributes, '$.client_id') LIKE '08-wasm%'

