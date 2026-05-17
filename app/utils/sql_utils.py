import sqlglot



def validate_sql(query: str):
    try:
        sqlglot.parse_one(query)
        return True, None
    except Exception as e:
        return False, str(e)
