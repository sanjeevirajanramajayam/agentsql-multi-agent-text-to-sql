from langgraph.graph import StateGraph, END

from app.models.state import AgentState

from app.agents.schema_agent import schema_agent
from app.agents.sql_generator_agent import sql_generator_agent
from app.agents.sql_validator_agent import sql_validator_agent
from app.agents.sql_executor_agent import sql_executor_agent
from app.agents.response_agent import response_agent


workflow = StateGraph(AgentState)

workflow.add_node("schema_agent", schema_agent)
workflow.add_node("sql_generator_agent", sql_generator_agent)
workflow.add_node("sql_validator_agent", sql_validator_agent)
workflow.add_node("sql_executor_agent", sql_executor_agent)
workflow.add_node("response_agent", response_agent)

workflow.set_entry_point("schema_agent")

workflow.add_edge("schema_agent", "sql_generator_agent")
workflow.add_edge("sql_generator_agent", "sql_validator_agent")
workflow.add_edge("sql_validator_agent", "sql_executor_agent")
workflow.add_edge("sql_executor_agent", "response_agent")
workflow.add_edge("response_agent", END)


app_graph = workflow.compile()
