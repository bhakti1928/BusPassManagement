from fastapi import APIRouter

router = APIRouter(
    prefix="/payment",
    tags=["Payment"]
)

@router.post("/")
def payment():
    return {
        "message": "Payment Successful",
        "status": "Paid"
    }