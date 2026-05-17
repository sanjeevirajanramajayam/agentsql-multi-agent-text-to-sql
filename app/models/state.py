from typing import TypedDict, Optional


class AgentState(TypedDict):
    question: str
    schema: Optional[str]
    sql_query: Optional[str]
    validated: Optional[bool]
    sql_result: Optional[str]
    final_response: Optional[str]
