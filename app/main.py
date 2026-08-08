from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import student, buspass, admins, payment


app = FastAPI(
    title="Bus Pass Management System"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://bus-pass-management-sable.vercel.app",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(student.router)
app.include_router(buspass.router)
app.include_router(admins.router)
app.include_router(payment.router)


@app.get("/")
def home():
    return {
        "message": "Bus Pass API Running"
    }