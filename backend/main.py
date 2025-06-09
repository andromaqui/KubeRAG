from fastapi import FastAPI
from api.questions import router as questions_router
from exceptions.handlers import register_exception_handlers

app = FastAPI(
    title="KubeRAG",
    version="0.1.0",
    description="Chat with your Kubernetes cluster"
)

app.include_router(questions_router, prefix="/api")
register_exception_handlers(app)


@app.get("/health")
def health_check():
    return {"status": "ok"}
