from fastapi import APIRouter
from .books.views import router as books_router
from .users.views import router as user_router

router = APIRouter()
router.include_router(router=books_router, prefix="/books")
router.include_router(router=user_router, prefix="/users")