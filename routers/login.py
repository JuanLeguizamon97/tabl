from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_access_token
from schemas.user import User

login_router = APIRouter()

@login_router.post('/login', tags=['auth'])
def login(user: User):
    token: str = create_access_token(user.model_dump())
    return JSONResponse(status_code=200, content=token)