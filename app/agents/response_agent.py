import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)



def response_agent(state):
    question = state["question"]
    sql_query = state["sql_query"]
    result = state["sql_result"]

    prompt = f"""
User Question:
{question}

SQL Query:
{sql_query}

SQL Result:
{result}

Generate a professional natural language answer.
"""

    response = model.invoke(prompt)

    state["final_response"] = response.content

    return state
