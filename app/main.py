from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import student, buspass, admins, payment

app = FastAPI(
    title="Bus Pass Management System"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student.router)
app.include_router(buspass.router)
app.include_router(admins.router)
app.include_router(payment.router)

@app.get("/")
def home():
    return {
        "message": "Bus Pass API Running"
    }