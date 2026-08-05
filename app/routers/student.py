from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)

# =========================
# Register Student
# =========================

@router.post("/register", response_model=schemas.StudentResponse)
def register_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


# =========================
# Get All Students
# =========================

@router.get("/", response_model=list[schemas.StudentResponse])
def get_all_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


# =========================
# Get Student By ID
# =========================

@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student_by_id(db, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# =========================
# Update Student
# =========================

@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(
        db,
        student_id,
        student
    )

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


# =========================
# Delete Student
# =========================

@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_student(db, student_id)

    if result:
        return {
            "message": "Student deleted successfully"
        }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# =========================
# Student Login
# =========================

@router.post("/login")
def login_student(
    login: schemas.StudentLogin,
    db: Session = Depends(get_db)
):
    student = crud.student_login(db, login)

    if student:
        return {
            "message": "Login Successful",
            "student": student
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid Email or Password"
    )