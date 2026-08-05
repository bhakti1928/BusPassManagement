from sqlalchemy.orm import Session
from app import models, schemas

from fastapi import HTTPException

# =========================
# STUDENT CRUD OPERATIONS
# =========================

# Create Student
def create_student(
    db: Session,
    student: schemas.StudentCreate
):
    new_student = models.Student(
        name=student.name,
        email=student.email,
        mobile=student.mobile,
        college=student.college,
        password=student.password
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Get All Students
def get_students(
    db: Session
):
    return db.query(
        models.Student
    ).all()


# Get Student By ID
def get_student_by_id(
    db: Session,
    student_id: int
):
    return db.query(
        models.Student
    ).filter(
        models.Student.id == student_id
    ).first()


# Update Student
def update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentUpdate
):
    db_student = db.query(
        models.Student
    ).filter(
        models.Student.id == student_id
    ).first()

    if db_student is None:
        return None

    db_student.name = student.name
    db_student.email = student.email
    db_student.mobile = student.mobile
    db_student.college = student.college

    db.commit()
    db.refresh(db_student)

    return db_student


# Delete Student
def delete_student(
    db: Session,
    student_id: int
):
    student = db.query(
        models.Student
    ).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        return False

    db.delete(student)
    db.commit()

    return True


# Student Login
def student_login(
    db: Session,
    login: schemas.StudentLogin
):
    student = db.query(
        models.Student
    ).filter(
        models.Student.email == login.email,
        models.Student.password == login.password
    ).first()

    return student


# =========================
# BUS PASS CRUD OPERATIONS
# =========================

# Apply Bus Pass
def create_bus_pass(
    db: Session,
    bus_pass: schemas.BusPassCreate
):
    print("CRUD create_bus_pass called")
    print(bus_pass)

    new_pass = models.BusPass(
        student_id=bus_pass.student_id,
        source=bus_pass.source,
        destination=bus_pass.destination,
        pass_type=bus_pass.pass_type,
        start_date=bus_pass.start_date,
        end_date=bus_pass.end_date,
        status="Pending"
    )

    db.add(new_pass)
    db.commit()
    db.refresh(new_pass)

    return new_pass

# Get All Bus Passes
def get_bus_passes(
    db: Session
):
    return db.query(
        models.BusPass
    ).all()


# Get Bus Pass By ID
def get_bus_pass_by_id(
    db: Session,
    pass_id: int
):
    return db.query(
        models.BusPass
    ).filter(
        models.BusPass.id == pass_id
    ).first()


# Get Bus Passes By Student ID
def get_student_pass(
    db: Session,
    student_id: int
):
    return db.query(
        models.BusPass
    ).filter(
        models.BusPass.student_id == student_id
    ).all()


# Update Bus Pass Status
def update_pass_status(
    db: Session,
    pass_id: int,
    status: str
):
    bus_pass = db.query(
        models.BusPass
    ).filter(
        models.BusPass.id == pass_id
    ).first()

    if bus_pass is None:
        return None

    bus_pass.status = status

    db.commit()
    db.refresh(bus_pass)

    return bus_pass


# Delete Bus Pass
def delete_bus_pass(
    db: Session,
    pass_id: int
):
    bus_pass = db.query(
        models.BusPass
    ).filter(
        models.BusPass.id == pass_id
    ).first()

    if bus_pass is None:
        return False

    db.delete(bus_pass)
    db.commit()

    return True

# =========================
# ADMIN CRUD OPERATIONS
# =========================

# Create Admin
def create_admin(
    db: Session,
    admin: schemas.AdminCreate
):
    new_admin = models.Admin(
        name=admin.name,
        email=admin.email,
        password=admin.password
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return new_admin



# Admin Login
def admin_login(
    db: Session,
    login: schemas.AdminLogin
):

    print("LOGIN EMAIL:", login.email)
    print("LOGIN PASSWORD:", login.password)

    admin = db.query(
        models.Admin
    ).filter(
        models.Admin.email == login.email,
        models.Admin.password == login.password
    ).first()

    print("ADMIN FOUND:", admin)

    if not admin:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    return admin