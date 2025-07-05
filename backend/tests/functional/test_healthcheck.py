import pytest
from starlette import status

from tests.common.api_client import AsyncTestClient
from tests.common.assert_contains_ext import assert_response

pytestmark = pytest.mark.anyio


async def test_healthcheck_method(unauthorized_client: AsyncTestClient) -> None:
    assert_response(
        await unauthorized_client.get("/_healthcheck"),
        expected_code=status.HTTP_204_NO_CONTENT,
    )
