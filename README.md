# Delta Sync
Delta-based synchronization demo web application made with FastAPI, SocketIO (TMEXIO), SQLAlchemy, React & Vite

## Backend
### Install
```sh
pip install poetry==2.1.3
poetry --directory=backend install
pre-commit install --install-hooks
```

If you are using PyCharm, mark the `backend` directory as "Sources Root"

### Run
```sh
docker compose up -d --wait
```

## Frontend
```sh
cd frontend
```

### Install
```sh
pnpm install
```

### Run (dev-mode)
```sh
pnpm run dev
```

### Build
```sh
pnpm run build
```
