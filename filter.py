from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, StudentSubject, Subject

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

existing_student = session.query(Student).filter_by(name='John Doe').first()

if not existing_student:
    english_subject = Subject(name='English')
    john_doe = Student(name='John Doe', age=20)
    john_english = StudentSubject(student=john_doe, subject=english_subject)

    session.add_all([john_doe, english_subject, john_english])
    session.commit()
    print("Student added to database.")
else:
    print("The student already exists in the database.")

english_students = (
    session.query(Student)
    .join(StudentSubject)
    .join(Subject)
    .filter(Subject.name == 'English')
    .all()
)

for student in english_students:
    print(student.name)
