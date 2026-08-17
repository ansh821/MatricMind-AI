import json
import ollama

from metrics import METRICS, DIMENSIONS


# --------------------------------------------------
# AI Intent Detection using Local Ollama Model
# --------------------------------------------------

def analyze_question(question: str):

    system_prompt = f"""
You are the AI intent classifier for MetricMind,
an Agentic Business Intelligence system.

Your job is to understand the user's business question
and identify which MetricMind analytics function should
be used.

Available Metrics:
{json.dumps(METRICS, indent=2)}

Available Dimensions:
{json.dumps(DIMENSIONS, indent=2)}

Available analytics functions:

1. get_total_summary
   Use for total revenue, total profit,
   or overall profit margin.

2. get_revenue_by_region
   Use for revenue analysis by region.

3. get_category_performance
   Use for category-level revenue, profit,
   and profit margin.

4. get_top_profitable_products
   Use for questions about the most profitable,
   best performing, or top profitable products.


Important examples:

Question:
"Which region generated the most revenue?"

Correct response:
{{
    "intent": "get_revenue_by_region",
    "metric": "revenue",
    "dimension": "region",
    "reason": "The user wants to find which region generated the highest revenue."
}}

Question:
"What are our most profitable products?"

Correct response:
{{
    "intent": "get_top_profitable_products",
    "metric": "profit",
    "dimension": "product",
    "reason": "The user wants to find the products with the highest profit."
}}

Question:
"Show me category performance"

Correct response:
{{
    "intent": "get_category_performance",
    "metric": "revenue",
    "dimension": "category",
    "reason": "The user wants to compare business performance across categories."
}}

Question:
"What is our total profit?"

Correct response:
{{
    "intent": "get_total_summary",
    "metric": "profit",
    "dimension": null,
    "reason": "The user wants to know the overall profit."
}}

Question:
"What is our overall profit margin?"

Correct response:
{{
    "intent": "get_total_summary",
    "metric": "profit_margin",
    "dimension": null,
    "reason": "The user wants to know the overall profit margin."
}}


Return ONLY valid JSON.

The JSON format must be:

{{
    "intent": "function_name",
    "metric": "metric_name",
    "dimension": "dimension_name",
    "reason": "short explanation"
}}

If the question is not supported, return:

{{
    "intent": "unknown",
    "metric": null,
    "dimension": null,
    "reason": "Question is outside the currently supported analytics."
}}
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    result = response["message"]["content"]

    try:
        return json.loads(result)

    except json.JSONDecodeError:

        return {
            "intent": "unknown",
            "metric": None,
            "dimension": None,
            "reason": "AI returned an invalid JSON response.",
            "raw_response": result
        }