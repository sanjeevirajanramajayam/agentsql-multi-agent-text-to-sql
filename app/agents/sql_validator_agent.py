from app.utils.sql_utils import validate_sql



def sql_validator_agent(state):
    query = state["sql_query"]

    valid, error = validate_sql(query)

    state["validated"] = valid

    if not valid:
        state["sql_result"] = error

    return state
