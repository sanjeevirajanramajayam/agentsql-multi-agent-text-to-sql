# AgentSQL

AgentSQL is a multi-agent **Text-to-SQL** project that converts natural-language questions into SQL, executes them on the Chinook SQLite database, and returns a readable answer.

## Tech Stack

- FastAPI (API service)
- Streamlit (chat UI)
- LangGraph + LangChain (agent orchestration)
- Google Gemini via `langchain-google-genai` (LLM)
- SQLAlchemy + SQLite (query execution)
- `sqlglot` (SQL validation)

## What It Does

- Converts plain-English questions to SQL
- Uses a staged multi-agent workflow
- Reads live schema before SQL generation
- Validates SQL before execution
- Executes queries against `app/database/chinook.db`
- Returns both SQL output and a natural-language response

## Multi-Agent Workflow

The request pipeline is defined in `app/graph/workflow.py`:

1. **Schema Agent** (`schema_agent`) gathers schema metadata.
2. **SQL Generator Agent** (`sql_generator_agent`) generates SQL from question + schema.
3. **SQL Validator Agent** (`sql_validator_agent`) parses SQL with `sqlglot`.
4. **SQL Executor Agent** (`sql_executor_agent`) runs validated SQL.
5. **Response Agent** (`response_agent`) turns SQL result into final answer text.

## Project Structure

```text
app/
  agents/        # Individual agents for schema, SQL generation, validation, execution, response
  api/           # FastAPI routes
  database/      # Chinook DB and DB helper
  graph/         # LangGraph workflow
  models/        # Shared state model
  utils/         # SQL utilities
run.py           # Starts FastAPI with Uvicorn
ui.py            # Streamlit chat interface
```

## Prerequisites

- Python
- A Google AI API key (`GOOGLE_API_KEY`)

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set environment variable:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

## Run the Application

### 1) Start the FastAPI backend

```bash
python run.py
```

API runs on `http://localhost:8000`.

### 2) (Optional) Start the Streamlit UI

In a second terminal:

```bash
streamlit run ui.py
```

UI sends requests to `http://localhost:8000/query`.

## API Usage

### Endpoint

`POST /query`

### Request Body

```json
{
  "question": "What are the top 5 best-selling artists?"
}
```

### Example Response

```json
{
  "question": "What are the top 5 best-selling artists?",
  "sql_query": "SELECT ...",
  "result": "...",
  "answer": "..."
}
```

## Example Questions

- What are the top 5 best-selling tracks?
- Which customers spent the most?
- How many invoices were generated in each country?
