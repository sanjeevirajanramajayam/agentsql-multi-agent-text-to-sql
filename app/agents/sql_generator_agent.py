import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


SYSTEM_PROMPT = """
You are an expert SQL generator.

Generate syntactically correct SQL queries.

Rules:
- Only generate SELECT queries
- Never generate DELETE, UPDATE, DROP, INSERT
- Use only provided schema
- Return ONLY SQL query
"""


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)



def sql_generator_agent(state):
    question = state["question"]
    schema = state["schema"]

    prompt = f"""
Database Schema:
{schema}

Question:
{question}
"""

    response = model.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", prompt),
        ]
    )

    sql_query = response.content.strip()

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")

    state["sql_query"] = sql_query.strip()

    return state
