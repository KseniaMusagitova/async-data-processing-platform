from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI(
    title="Async Data Processing Platform",
    description="API for asynchronous data processing",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/v1/files", status_code=201)
async def upload_file(file: UploadFile = File(...)):

    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    content = await file.read(5 * 1024 * 1024 + 1)

    # Check the file size
    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(
        status_code=413,
        detail="File exceeds the 5 MB limit"
    )

    # Check if the file is empty
    if not content:
        raise HTTPException(
            status_code=400,
            detail="File cannot be empty"
        )

    return {"filename": file.filename}