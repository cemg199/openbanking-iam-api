from fastapi import APIRouter, Depends
from app.auth import (
    get_current_token,
    require_customer_role,
)

router = APIRouter()


@router.get("/balance")
def get_balance(
    claims: dict = Depends(get_current_token)
):
    require_customer_role(claims)

    return {
        "account": "123456789",
        "owner": "Alice Johnson",
        "balance": 2450.75,
        "currency": "CAD"
    }
