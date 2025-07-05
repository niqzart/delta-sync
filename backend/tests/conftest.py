from collections.abc import AsyncIterator

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

from app.main import app
from tests.common.api_client import AsyncTestClient

pytest_plugins = (
    "anyio",
    "tests.common.active_session",
    "tests.common.mock_stack",
)


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def lifespanned_app() -> AsyncIterator[FastAPI]:
    # LifespanManager is used to start fastapi's lifespan before all tests
    async with LifespanManager(app):
        yield app


@pytest.fixture()
async def unauthorized_client(lifespanned_app: FastAPI) -> AsyncTestClient:
    return AsyncTestClient.build_app_client(app=lifespanned_app)
