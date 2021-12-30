from datetime import timedelta
from fastapi import Depends, APIRouter, HTTPException, status

from app.core.db import db
from app.core.security import authenticate_user, create_access_token, get_password_hash, get_current_user
from app.schemas.auth import SinginInput, Token, User, SingupInput

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"message": "Not found"}},
)

@router.post("/singin", response_model=Token)
async def singin(body: SinginInput):
    user = authenticate_user(body.email, body.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"user_id": str(user["_id"])},
        expires_delta=access_token_expires
    )
    return {"token": access_token}

@router.post("/singup", response_model=Token)
async def singup(body: SingupInput):
    user = db.users.find_one({"email": body.email})
    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email",
        )

    user_id = db.users.insert_one({
        "email": str(body.email),
        "password": get_password_hash(str(body.password))
    }).inserted_id

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"user_id": str(user_id)},
        expires_delta=access_token_expires
    )

    return {"token": access_token}


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
