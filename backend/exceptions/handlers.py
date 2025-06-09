from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import datetime
from .errors import InternalServerError, BadRequestError


def register_exception_handlers(app):
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
            status_code=422,
            content={
                "status": "error",
                "code": 422,
                "error": "ValidationError",
                "message": "Invalid input: " + "; ".join(
                    f"{'.'.join(map(str, e['loc']))}: {e['msg']}" for e in exc.errors()
                ),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )

    @app.exception_handler(BadRequestError)
    async def bad_request_exception_handler(request: Request, exc: BadRequestError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "error",
                "code": 400,
                "error": "BadRequestError",
                "message": exc.message,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )