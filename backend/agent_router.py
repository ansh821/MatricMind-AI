from ai_agent import analyze_question

from query_engine import (
    get_total_summary,
    get_revenue_by_region,
    get_category_performance,
    get_top_profitable_products
)


# --------------------------------------------------
# Route AI Intent to Query Engine
# --------------------------------------------------

def run_metricmind_agent(question: str):

    # Step 1: Ask AI to understand the question
    ai_result = analyze_question(question)

    intent = ai_result.get("intent")

    # --------------------------------------------------
    # Step 2: Route to correct database function
    # --------------------------------------------------

    if intent == "get_total_summary":

        data = get_total_summary()

    elif intent == "get_revenue_by_region":

        data = get_revenue_by_region()

    elif intent == "get_category_performance":

        data = get_category_performance()

    elif intent == "get_top_profitable_products":

        data = get_top_profitable_products()

    else:

        return {
            "success": False,
            "question": question,
            "ai_analysis": ai_result,
            "data": None,
            "message": "Sorry, I could not understand this question."
        }

    # --------------------------------------------------
    # Step 3: Return AI analysis + Real PostgreSQL data
    # --------------------------------------------------

    return {
        "success": True,
        "question": question,
        "ai_analysis": ai_result,
        "data": data
    }