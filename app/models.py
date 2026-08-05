from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


# =========================
# Student Model
# =========================

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    mobile = Column(String)
    college = Column(String)
    password = Column(String)

    bus_passes = relationship("BusPass", back_populates="student")


# =========================
# Bus Pass Model
# =========================

class BusPass(Base):
    __tablename__ = "bus_passes"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    source = Column(String)
    destination = Column(String)
    pass_type = Column(String)

    start_date = Column(String)
    end_date = Column(String)

    status = Column(
        String,
        default="Pending"
    )

    student = relationship(
        "Student",
        back_populates="bus_passes"
    )


# =========================
# Admin Model
# =========================

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)


# =========================
# Bus Model
# =========================

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)

    bus_number = Column(String, unique=True)
    driver_name = Column(String)
    route = Column(String)
    capacity = Column(Integer)






class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer)

    pass_id = Column(Integer)

    amount = Column(Integer)

    payment_method = Column(String)

    transaction_id = Column(String)

    payment_status = Column(String)

    payment_date = Column(DateTime)