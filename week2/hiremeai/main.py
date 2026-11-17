from fastapi import FastAPI

app = FastAPI(title="HireMeAI")

@app.get("/")
async def root():
    return {"message": "Hello from HireMeAI!"}

@app.get("/health")
async def health():
    return {"status": "ok"}