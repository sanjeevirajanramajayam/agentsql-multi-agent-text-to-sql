from app.database.db import get_database



def schema_agent(state):
    db = get_database()

    tables = db.get_usable_table_names()

    schema_info = []

    for table in tables:
        table_schema = db.get_table_info([table])
        schema_info.append(table_schema)

    state["schema"] = "\n\n".join(schema_info)

    return state
