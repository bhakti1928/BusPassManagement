from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# Admin Register
@router.post("/register", response_model=schemas.AdminResponse)
def register_admin(
    admin: schemas.AdminCreate,
    db: Session = Depends(get_db)
):
    return crud.create_admin(db, admin)



# Admin Login
@router.post("/login", response_model=schemas.AdminResponse)
def login_admin(
    login: schemas.AdminLogin,
    db: Session = Depends(get_db)
):
    return crud.admin_login(db, login)


# View All Bus Passes

@router.get("/buspasses")
def view_bus_passes(
    db: Session = Depends(get_db)
):
    return crud.get_bus_passes(db)


# Approve / Reject Bus Pass

@router.put("/buspass/{pass_id}")
def update_buspass_status(
    pass_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    return crud.update_pass_status(
        db,
        pass_id,
        status
    )

# Get All Bus Passes (Admin)
@router.get("/buspasses")
def get_all_bus_passes(
    db: Session = Depends(get_db)
):
    return crud.get_bus_passes(db)