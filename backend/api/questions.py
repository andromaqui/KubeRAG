from fastapi import APIRouter, HTTPException
from models.question import QuestionRequest, QuestionResponse
from exceptions.handlers import register_exception_handlers
from exceptions.errors import UserNotFoundError, InternalServerError

router = APIRouter()
register_exception_handlers(app)

@router.post("/questions", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    try:
        answer = "handle_question(request.question)"
        return {"answer": answer}
    except Exception:
        raise InternalServerError
