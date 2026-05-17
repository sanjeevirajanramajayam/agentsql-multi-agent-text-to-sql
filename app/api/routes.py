from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.workflow import app_graph


router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def ask_question(request: QueryRequest):

    initial_state = {
        "question": request.question,
        "schema": None,
        "sql_query": None,
        "validated": None,
        "sql_result": None,
        "final_response": None,
    }

    result = app_graph.invoke(initial_state)

    return {
        "question": request.question,
        "sql_query": result["sql_query"],
        "result": result["sql_result"],
        "answer": result["final_response"],
    }
