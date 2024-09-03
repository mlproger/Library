from contextlib import asynccontextmanager
import uvicorn
from core.config import config
from core.models import Base, db_helper
from fastapi import FastAPI
from api_v1 import router as router_v1
from api_v1.rent_inspector.views import router as rent_router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Hello")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=config.api_v1_prefix, tags=["API"])
app.include_router(rent_router, prefix=config.api_v1_prefix, tags=["Rent"])

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=8000,
    )
