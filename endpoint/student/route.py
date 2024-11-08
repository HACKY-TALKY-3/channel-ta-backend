from fastapi import APIRouter

from data.db.models import Appointment

from endpoint.student.entity import ReadStudent, CreateStudent
from endpoint.student.repository import create_student, get_student, get_students
import requests
import json
import dotenv


config = dotenv.dotenv_values('.env')


router = APIRouter(
    prefix="/student",
    tags=["student"]
)



@router.get("/")
async def root():
    return {}


@router.get("/list")
async def list_student() -> list[ReadStudent]:
    appointments = await get_students()

    return appointments


@router.get("/{student_id}")
async def read_student(student_id: int) -> ReadStudent:
    appointment = await get_student(student_id)
    return appointment



@router.post("/")
async def new_student(student_data: CreateStudent):

    student_req = {
        'name': student_data.name,
        'gender': student_data.gender
    }

    created_student = await create_student(student_req)

    return created_student


@router.delete("/{student_id}")
async def delete_appointment(student_id: int): pass

