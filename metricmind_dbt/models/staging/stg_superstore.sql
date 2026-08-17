SELECT
    *
FROM {{ source('raw', 'superstore_raw') }}