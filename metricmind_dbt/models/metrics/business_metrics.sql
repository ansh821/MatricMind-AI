{{ config(
    materialized='table',
    
) }}

SELECT
    SUM(SALES) AS total_sales,
    SUM(PROFIT) AS total_profit,
    SUM(QUANTITY) AS total_quantity,
    SUM(SALES) AS total_revenue,
    SUM(PROFIT) / NULLIF(SUM(SALES), 0) AS profit_margin

FROM {{ ref('fct_sales') }}