from fastapi import APIRouter, HTTPException, Depends
from models.question import QuestionRequest, QuestionResponse
from services.question_service import QuestionService

router = APIRouter()
def get_question_service() -> QuestionService:
    return QuestionService()

@router.post("/questions", response_model=QuestionResponse)
async def ask_question(
    request: QuestionRequest,
    service: QuestionService = Depends(get_question_service)
):
    answer = await service.handle_question(request.question)
    return QuestionResponse(answer=answer)