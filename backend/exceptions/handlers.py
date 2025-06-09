from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import datetime
from .errors import UserNotFoundError, InternalServerError

def register_exception_handlers(app):
    @app.exception_handler(UserNotFoundError)
    async def user_not_found_handler(request: Request, exc: UserNotFoundError):
        return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "code": 404,
                "error": "UserNotFound",
                "message": exc.message,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )

    @app.exception_handler(InternalServerError)
    async def internal_server_error_handler(request: Request, exc: InternalServerError):
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "code": 500,
                "error": "InternalServerError",
                "message": exc.message,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "code": 400,
                "error": "ValidationError",
                "message": exc.errors(),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )