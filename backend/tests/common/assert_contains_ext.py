from json import JSONDecodeError

from httpx import Response
from pydantic_marshals.contains import TypeChecker, assert_contains
from starlette import status

from app.exceptions.base_exceptions import BaseClientException


def assert_response(
    response: Response,
    *,
    expected_code: int = status.HTTP_200_OK,
    expected_headers: dict[str, TypeChecker] | None = None,
    expected_cookies: dict[str, TypeChecker] | None = None,
    expected_json: TypeChecker = None,
    expected_content: TypeChecker = ...,
) -> Response:
    try:
        json_data = response.json()
    except (UnicodeDecodeError, JSONDecodeError):
        json_data = None

    expected_headers = expected_headers or {}
    if expected_json is not None:
        expected_headers.setdefault("Content-Type", "application/json")

    assert_contains(
        {
            "status_code": response.status_code,
            "headers": response.headers,
            "cookies": response.cookies,
            "json_data": json_data,
            "content": None if response.content == b"" else response.content,
        },
        {
            "status_code": expected_code,
            "headers": expected_headers,
            "cookies": expected_cookies or {},
            "json_data": expected_json,
            "content": expected_content,
        },
    )
    return response


def assert_exception_response(
    response: Response,
    *,
    expected_exception: type[BaseClientException],
    expected_detail: TypeChecker = None,
    expected_headers: dict[str, TypeChecker] | None = None,
    expected_cookies: dict[str, TypeChecker] | None = None,
) -> Response:
    return assert_response(
        response,
        expected_code=expected_exception.status_code,
        expected_headers=expected_headers,
        expected_cookies=expected_cookies,
        expected_json={
            "reason": expected_exception.reason,
            "message": expected_exception.message,
            "detail": expected_detail,
        },
    )
