import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime

from school.models import Student, Course, Registration


def creating_students(number_of_students: int) -> None:
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(number_of_students):
        cpf = CPF()
        name = fake.name()
        rg = f"{random.randrange(10,99)}{random.randrange(100,999)}{random.randrange(100,999)}{random.randrange(0,9)}"
        cpf = cpf.generate()
        birth_date = fake.date_between(start_date="-18y", end_date="today")
        student = Student(
            name=name,
            rg=rg,
            cpf=cpf,
            birth_date=birth_date
        )
        student.save()


def creating_courses(number_of_courses: int) -> None:
    for _ in range(number_of_courses):
        course_code = f"{random.choice('ABCDEF')}{random.randrange(10,99)}-{random.randrange(1,9)}"
        descriptions = ['Python Fundamentals', 'Intermediate Python', 
                        'Advanced Python', 'Python for Data Science', 
                        'Python/React']
        description = random.choice(descriptions)
        level = random.choice("BIA")
        course = Course(
            course_code=course_code,
            description=description,
            level=level,
        )
        course.save()



if __name__ == "__main__":
    creating_students(200)
    creating_courses(10)
    