# AgentSQL

AgentSQL is a Multi-Agent Text-to-SQL system built using:

- LangChain
- LangGraph
- FastAPI
- Claude LLM
- SQLAlchemy
- sqlglot

## Features

- Natural Language to SQL
- Multi-Agent Workflow
- Schema-Aware Querying
- SQL Validation
- Safe SQL Execution
- AI-Powered Responses

## Example Query

"What are the top 5 best-selling tracks?"

## Run Project

```bash
pip install -r requirements.txt
```

```bash
python run.py
```

## API Endpoint

POST:

```bash
/query
```

Request:

```json
{
  "question": "What are the top 5 best-selling artists?"
}
```
