from sqlalchemy import create_engine, text
from app.database.db import DB_PATH


engine = create_engine(f"sqlite:///{DB_PATH}")



def sql_executor_agent(state):
    if not state["validated"]:
        return state

    query = state["sql_query"]

    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))

            rows = result.fetchall()

            formatted_rows = []

            for row in rows:
                formatted_rows.append(str(row))

            state["sql_result"] = "\n".join(formatted_rows)

    except Exception as e:
        state["sql_result"] = str(e)

    return state
