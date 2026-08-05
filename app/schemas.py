from pydantic import BaseModel
from datetime import date



# =========================
# Student Schema
# =========================

class StudentCreate(BaseModel):
    name: str
    email: str
    mobile: str
    college: str
    password: str


class StudentUpdate(BaseModel):
    name: str
    email: str
    mobile: str
    college: str


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    mobile: str
    college: str

    class Config:
        from_attributes = True


class StudentLogin(BaseModel):
    email: str
    password: str


# =========================
# Bus Pass Schema
# =========================



class BusPassCreate(BaseModel):
    student_id: int
    source: str
    destination: str
    pass_type: str
    start_date: date
    end_date: date


class BusPassResponse(BaseModel):
    id: int
    student_id: int
    source: str
    destination: str
    pass_type: str
    start_date: date
    end_date: date
    status: str
    
    class Config:
        from_attributes = True


# =========================
# Admin Schema
# =========================

class AdminCreate(BaseModel):
    name: str
    email: str
    password: str


class AdminResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class AdminLogin(BaseModel):
    email: str
    password: str