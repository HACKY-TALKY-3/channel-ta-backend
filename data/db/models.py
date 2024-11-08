from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum
from datetime import datetime

Base = declarative_base()



class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    # Relationships
    appointments = relationship("Appointment", back_populates="student")
    questions = relationship("Questions", back_populates="student")


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    date_ymd = Column(DateTime)
    agenda = Column(String)
    detail = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    student_id = Column(Integer, ForeignKey('students.id'))

    # Relationships
    student = relationship("Student", back_populates="appointments")


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    agenda = Column(String)
    detail = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    student_id = Column(Integer, ForeignKey('students.id'))

    # Relationships
    student = relationship("Student", back_populates="questions")
