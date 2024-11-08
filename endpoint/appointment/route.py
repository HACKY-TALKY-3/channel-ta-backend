from fastapi import APIRouter

from data.db.models import Appointment

from endpoint.appointment.entity import ReadAppointment, CreateAppointment
from endpoint.appointment.repository import create_appointment, get_appointment, get_appointments, delete_appointment, get_every_appointments
import requests
import json
import dotenv


config = dotenv.dotenv_values('.env')


router = APIRouter(
    prefix="/appointment",
    tags=["appointment"]
)



@router.get("/")
async def root():
    return {}


@router.get("/list")
async def list_every_appointment() -> list[ReadAppointment]:    # 특정 학생 예약 정보 열람
    appointments = await get_every_appointments()

    return appointments


@router.get("/list/{student_id}")
async def list_appointment(student_id: int) -> list[ReadAppointment]:    # 특정 학생 예약 정보 열람
    appointments = await get_appointments(student_id)

    return appointments


@router.get("/{appointment_id}")
async def read_appointment(appointment_id: int) -> ReadAppointment:    # 예약 정보 열람
    appointment = await get_appointment(appointment_id)
    return appointment



@router.post("/")
async def new_appointment(appointment_data: CreateAppointment):

    appointment_req = {
        'student_id': appointment_data.student_id,
        'date_ymd': appointment_data.date_ymd,
        'agenda': appointment_data.agenda,
        'detail': appointment_data.detail
    }

    print(appointment_req)


    created_appointment = await create_appointment(appointment_req)

    return created_appointment


@router.delete("/{appointment_id}")
async def delete_appointment(appointment_id: int): pass

