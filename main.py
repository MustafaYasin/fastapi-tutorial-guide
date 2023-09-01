from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,


    )
]

@app.get("/")
async def root():
    return {"message": "Hello Mundo"} 