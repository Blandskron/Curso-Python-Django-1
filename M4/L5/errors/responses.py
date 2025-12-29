# core/errors/responses.py

from typing import Any, Optional


def error_response(
    *,
    status: int,
    error_code: str,
    message: str,
    detail: Optional[Any] = None,
    trace_id: Optional[str] = None,
) -> dict:
    return {
        "success": False,
        "status": status,
        "error": {
            "code": error_code,
            "message": message,
            "detail": detail,
        },
        "trace_id": trace_id,
    }
