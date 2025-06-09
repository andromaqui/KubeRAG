from exceptions.errors import BadRequestError, InternalServerError

class QuestionService:
    MAX_PROMPT_CHARS = 12000

    def __init__(self):
        pass

    async def handle_question(self, question: str) -> str:
        if not question.strip():
            raise BadRequestError("Question cannot be empty")

        if len(question) > self.MAX_PROMPT_CHARS:
            raise BadRequestError("The inputted prompt is too long.")

        try:
            return "hey"
        except Exception:
            raise InternalServerError