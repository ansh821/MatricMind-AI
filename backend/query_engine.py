from sqlalchemy import text
from database import engine


def get_total_summary():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    SUM("Sales") AS total_revenue,
                    SUM("Profit") AS total_profit,
                    SUM("Quantity") AS total_sales,
                    ROUND(
                        (
                            SUM("Profit")
                            / NULLIF(SUM("Sales"), 0)
                            * 100
                        )::numeric,
                        2
                    ) AS profit_margin
                FROM sales
            """)
        )

        row = result.fetchone()

        return {
            "revenue": float(row.total_revenue),
            "profit": float(row.total_profit),
            "sales": int(row.total_sales),
            "profit_margin": float(row.profit_margin)
        }


def get_revenue_by_region():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    "Region" AS region,
                    SUM("Sales") AS revenue
                FROM sales
                GROUP BY "Region"
                ORDER BY revenue DESC
            """)
        )

        return [
            {
                "region": row.region,
                "revenue": float(row.revenue)
            }
            for row in result
        ]


def get_category_performance():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    "Category" AS category,
                    SUM("Sales") AS revenue,
                    SUM("Profit") AS profit,
                    ROUND(
                        (
                            SUM("Profit")
                            / NULLIF(SUM("Sales"), 0)
                            * 100
                        )::numeric,
                        2
                    ) AS profit_margin
                FROM sales
                GROUP BY "Category"
                ORDER BY revenue DESC
            """)
        )

        return [
            {
                "category": row.category,
                "revenue": float(row.revenue),
                "profit": float(row.profit),
                "profit_margin": float(row.profit_margin)
            }
            for row in result
        ]


def get_top_profitable_products():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    "Product.Name" AS product,
                    SUM("Sales") AS revenue,
                    SUM("Profit") AS profit,
                    ROUND(
                        (
                            SUM("Profit")
                            / NULLIF(SUM("Sales"), 0)
                            * 100
                        )::numeric,
                        2
                    ) AS profit_margin
                FROM sales
                GROUP BY "Product.Name"
                ORDER BY profit DESC
                LIMIT 10
            """)
        )

        return [
            {
                "product": row.product,
                "revenue": float(row.revenue),
                "profit": float(row.profit),
                "profit_margin": float(row.profit_margin)
            }
            for row in result
        ]
def get_profit_by_category():
    query = """
        SELECT
            "Category" AS category,
            SUM("Profit") AS profit
        FROM sales
        GROUP BY "Category"
        ORDER BY profit DESC;
    """

    with engine.connect() as connection:
        result = connection.execute(text(query))

        return [
            {
                "category": row.category,
                "profit": float(row.profit or 0)
            }
            for row in result
        ] 
def get_revenue_trend():
    query = """
        SELECT
            "Year" AS year,
            SUM("Sales") AS revenue
        FROM sales
        GROUP BY "Year"
        ORDER BY "Year";
    """

    with engine.connect() as connection:
        result = connection.execute(text(query))

        return [
            {
                "month": str(row.year),
                "revenue": float(row.revenue or 0)
            }
            for row in result
        ]
def get_top_products():
    query = """
        SELECT
            "Product.Name" AS product,
            SUM("Sales") AS revenue
        FROM sales
        GROUP BY "Product.Name"
        ORDER BY revenue DESC
        LIMIT 5;
    """

    with engine.connect() as connection:
        result = connection.execute(text(query))

        return [
            {
                "product": row.product,
                "revenue": float(row.revenue or 0)
            }
            for row in result
        ]