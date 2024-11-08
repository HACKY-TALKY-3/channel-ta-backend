from jedi.inference.value.iterable import Sequence

from data.db.database import Transactional
from data.db.models import Appointment
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


@Transactional()
async def create_appointment(appointment_req: dict, session: AsyncSession = None) -> None:
    _appointment: Appointment = Appointment(**appointment_req)

    session.add(_appointment)
    await session.commit()
    await session.refresh(_appointment)


@Transactional()
async def get_appointment(appointment_id: int, session: AsyncSession = None) -> Appointment:
    stmt = (
        select(Appointment)
        .where(Appointment.id == appointment_id)
    )
    res = await session.execute(stmt)

    return res.scalars().first()


@Transactional()
async def get_appointments(student_id: int, session: AsyncSession = None) -> list[Appointment]:
    stmt = (
        select(Appointment)
        .where(Appointment.student_id == student_id)
    )

    res = await session.execute(stmt)

    return res.scalars().all()


@Transactional()
async def delete_appointment(appointment_id: int, session: AsyncSession = None) -> None:
    stmt = (
        delete(Appointment)
        .where(Appointment.id == appointment_id)
    )

    await session.execute(stmt)
