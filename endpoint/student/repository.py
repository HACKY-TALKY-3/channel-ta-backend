from jedi.inference.value.iterable import Sequence

from data.db.database import Transactional
from data.db.models import Student
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


@Transactional()
async def create_student(student_req: dict, session: AsyncSession = None) -> None:
    _appointment: Student = Student(**student_req)

    session.add(_appointment)
    await session.commit()
    await session.refresh(_appointment)


@Transactional()
async def get_student(student_id: int, session: AsyncSession = None) -> Student:
    stmt = (
        select(Student)
        .where(Student.id == student_id)
    )
    res = await session.execute(stmt)

    return res.scalars().first()


@Transactional()
async def get_students(session: AsyncSession = None) -> list[Student]:
    stmt = (
        select(Student)
    )

    res = await session.execute(stmt)

    return res.scalars().all()


@Transactional()
async def delete_appointment(student_id: int, session: AsyncSession = None) -> None:
    stmt = (
        delete(Student)
        .where(Student.id == student_id)
    )

    await session.execute(stmt)
