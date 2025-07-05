from typing import Self

from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient


class AsyncTestClient(AsyncClient):
    @classmethod
    def build_app_client(
        cls, app: FastAPI, headers: dict[str, str] | None = None
    ) -> Self:
        return cls(
            base_url="http://test",
            transport=ASGITransport(app),
            headers=headers,
        )
