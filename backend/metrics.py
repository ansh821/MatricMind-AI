# MetricMind Semantic Metrics

METRICS = {
    "revenue": {
        "name": "Revenue",
        "definition": 'SUM("Sales")',
        "description": "Total sales revenue generated."
    },

    "profit": {
        "name": "Profit",
        "definition": 'SUM("Profit")',
        "description": "Total profit generated."
    },

    "profit_margin": {
        "name": "Profit Margin",
        "definition": '(SUM("Profit") / NULLIF(SUM("Sales"), 0)) * 100',
        "description": "Profit as a percentage of total sales."
    }
}
DIMENSIONS = {
    "region": '"Region"',
    "category": '"Category"',
    "sub_category": '"Sub.Category"',
    "product": '"Product.Name"',
    "country": '"Country"',
    "market": '"Market"',
    "segment": '"Segment"',
    "year": '"Year"'
}