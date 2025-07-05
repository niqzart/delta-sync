# Delta Sync
Delta-based synchronization demo web application made with FastAPI, SocketIO (TMEXIO), SQLAlchemy, React & Vite

## Backend
### Install
```sh
pip install poetry==2.1.3
poetry --directory=backend install
pre-commit install
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

### Run (dev-mode)
```sh
npm run develop
```

### Build
```sh
npm run build
```
