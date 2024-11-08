from datetime import datetime

from pydantic import BaseModel


class ReadAppointment(BaseModel):
    id: int
    date_ymd: datetime
    agenda: str
    detail: str

    created_at: datetime
    updated_at: datetime

    student_id: int


class CreateAppointment(BaseModel):
    date_ymd: datetime
    agenda: str
    detail: str

    student_id: int
