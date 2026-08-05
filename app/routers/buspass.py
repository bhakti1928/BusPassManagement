from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud


router = APIRouter(
    prefix="/buspass",
    tags=["Bus Pass"]
)


# Apply Bus Pass
@router.post("/apply")
def apply_pass(
    buspass: schemas.BusPassCreate,
    db: Session = Depends(get_db)
):
    print("BUS PASS DATA:", buspass)
    return crud.create_bus_pass(db, buspass)

# Get All Bus Passes
@router.get("/", response_model=list[schemas.BusPassResponse])
def get_passes(
    db: Session = Depends(get_db)
):
    return crud.get_bus_passes(db)






# Get Student Bus Pass
@router.get("/student/{student_id}", response_model=list[schemas.BusPassResponse])
def get_student_pass(
    student_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_student_pass(db, student_id)







# Get Bus Pass By ID
@router.get("/{pass_id}", response_model=schemas.BusPassResponse)
def get_pass_by_id(
    pass_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_bus_pass_by_id(db, pass_id)



# Update Bus Pass Status
@router.put("/{pass_id}")
def update_status(
    pass_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    return crud.update_pass_status(
        db,
        pass_id,
        status
    )



# Delete Bus Pass
@router.delete("/{pass_id}")
def delete_pass(
    pass_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_bus_pass(
        db,
        pass_id
    )