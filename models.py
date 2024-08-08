from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    subjects = relationship('StudentSubject', back_populates='student')


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship('StudentSubject', back_populates='subject')


class StudentSubject(Base):
    __tablename__ = 'student_subject'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    student = relationship('Student', back_populates='subjects')
    subject = relationship('Subject', back_populates='students')
