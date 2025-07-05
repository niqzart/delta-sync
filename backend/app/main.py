import logging
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import APIRouter, FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from tmexio import TMEXIO, EventName, PydanticPackager

from app.common.sqlalchemy_ext import session_context
from app.common.starlette_cors_ext import CorrectCORSMiddleware
from app.common.tmexio_ext import remove_ping_pong_logs
from app.config import Base, engine, sessionmaker, settings

internal_router = APIRouter(prefix="/api/internal")

public_router = APIRouter(prefix="/api/public")


tmex = TMEXIO(
    async_mode="asgi",
    transports=["websocket"],
    cors_allowed_origins="*",
    logger=True,
    engineio_logger=True,
)
remove_ping_pong_logs()


@tmex.on_other(summary="[special] Handler for non-existent events")
async def handle_other_events(
    event_name: EventName,
) -> Annotated[str, PydanticPackager(str, status.HTTP_404_NOT_FOUND)]:
    return f"Unknown event: '{event_name}'"


async def reinit_database() -> None:  # pragma: no cover
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    if settings.postgres_automigrate:
        await reinit_database()

    yield


app = FastAPI(lifespan=lifespan)

app.mount("/socket.io/", tmex.build_asgi_app())
app.include_router(internal_router)
app.include_router(public_router)


@app.get(
    "/_healthcheck", include_in_schema=False, status_code=status.HTTP_204_NO_CONTENT
)
async def healthcheck() -> None:
    pass


app.add_middleware(
    CorrectCORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def database_session_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    async with sessionmaker.begin() as session:
        session_context.set(session)
        return await call_next(request)


class HealthCheckFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:  # noqa: FNE005
        return "/_healthcheck" not in record.getMessage()


logging.getLogger("uvicorn.access").addFilter(HealthCheckFilter())
