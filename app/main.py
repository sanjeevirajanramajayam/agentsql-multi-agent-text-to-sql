from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(title="AgentSQL")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "AgentSQL API Running"}
