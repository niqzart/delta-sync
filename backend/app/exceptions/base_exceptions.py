from typing import Any

from starlette.responses import JSONResponse


class BaseClientException(Exception):
    """Base class for exceptions returned to the client"""

    status_code: int
    """HTTP status code for the exception"""
    reason: str
    """Machine-readable exception identifier"""
    message: str
    """Human-readable explanation for the exception"""

    def __init__(self, detail: Any | None = None) -> None:
        """
        :param detail: Additional information about the exception
        """
        self.detail = detail

    def build_json_data(self) -> dict[str, Any]:
        return {
            "reason": self.reason,
            "message": self.message,
            "detail": self.detail,
        }

    def build_json_response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code,
            content=self.build_json_data(),
        )


class BaseServerException(Exception):
    """Base class for unknown exceptions needed for logging"""

    message: str
    """Human-readable explanation for the exception"""
