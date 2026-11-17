from fastapi import FastAPI

app = FastAPI(
    title="Async Data Processing Platform",
    description="API for asynchronous data processing",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}