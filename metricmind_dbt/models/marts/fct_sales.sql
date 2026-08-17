SELECT
    ORDER_ID AS order_id,
    ORDER_DATE AS order_date,
    SHIP_DATE AS ship_date,

    CUSTOMER_ID AS customer_id,
    CUSTOMER_NAME AS customer_name,

    PRODUCT_ID AS product_id,
    PRODUCT_NAME AS product_name,

    CATEGORY AS category,
    SUB_CATEGORY AS sub_category,

    SEGMENT AS segment,

    CITY AS city,
    STATE AS state,
    COUNTRY AS country,
    REGION AS region,
    MARKET AS market,

    SALES AS sales,
    PROFIT AS profit,
    QUANTITY AS quantity,
    DISCOUNT AS discount,
    SHIPPING_COST AS shipping_cost

FROM {{ ref('stg_superstore') }}