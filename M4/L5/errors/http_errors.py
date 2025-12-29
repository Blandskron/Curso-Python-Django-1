# core/errors/http_errors.py

from typing import Optional, Any


class HttpError(Exception):
    status_code: int = 500
    error_code: str = "INTERNAL_ERROR"
    message: str = "Unexpected error"
    detail: Optional[Any] = None

    def __init__(
        self,
        message: Optional[str] = None,
        *,
        detail: Optional[Any] = None,
    ):
        if message:
            self.message = message
        self.detail = detail
        super().__init__(self.message)


class BadRequest(HttpError):
    status_code = 400
    error_code = "VALIDATION_ERROR"


class Unauthorized(HttpError):
    status_code = 401
    error_code = "AUTH_ERROR"


class Forbidden(HttpError):
    status_code = 403
    error_code = "PERMISSION_DENIED"


class NotFound(HttpError):
    status_code = 404
    error_code = "NOT_FOUND"


class Conflict(HttpError):
    status_code = 409
    error_code = "CONFLICT"
