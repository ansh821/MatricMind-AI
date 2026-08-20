from ai_agent import analyze_question

from metrics import METRICS, DIMENSIONS

from query_engine import (
    get_total_summary,
    get_revenue_by_region,
    get_category_performance,
    get_top_profitable_products,
    get_profit_by_category,
    get_revenue_trend,
    get_top_products,
)


# --------------------------------------------------
# Semantic Layer Context
# --------------------------------------------------

SEMANTIC_CONTEXT = {
    "metrics": list(METRICS.keys()),
    "dimensions": list(DIMENSIONS.keys()),
}


# --------------------------------------------------
# Route AI Intent to Query Engine
# --------------------------------------------------

def run_metricmind_agent(question: str):

    # Step 1: AI understands the question
    ai_result = analyze_question(question)

    print("AI RESULT:", ai_result)

    intent = ai_result.get("intent")
    limit = ai_result.get("limit")

    # --------------------------------------------------
    # Step 2: Approved intent handlers
    # --------------------------------------------------

    intent_handlers = {
        "get_total_summary": get_total_summary,
        "get_revenue_by_region": get_revenue_by_region,
        "get_category_performance": get_category_performance,
        "get_top_profitable_products": get_top_profitable_products,
        "get_profit_by_category": get_profit_by_category,
        "get_revenue_trend": get_revenue_trend,
        "get_top_products": get_top_products,
    }

    handler = intent_handlers.get(intent)

    if handler is None:

        return {
            "success": False,
            "question": question,
            "ai_analysis": ai_result,
            "semantic_context": SEMANTIC_CONTEXT,
            "data": None,
            "message": "Sorry, I could not understand this question."
        }

    # --------------------------------------------------
    # Step 3: Execute query
    # --------------------------------------------------

    # Functions that support a dynamic limit
    if intent in [
        "get_top_products",
        "get_top_profitable_products"
    ]:

        data = handler(limit=limit)

    else:

        data = handler()

    # --------------------------------------------------
    # Step 4: Return result
    # --------------------------------------------------

    return {
        "success": True,
        "question": question,
        "ai_analysis": ai_result,
        "semantic_context": SEMANTIC_CONTEXT,
        "data": data
    }