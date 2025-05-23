from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee, Department, Performance
from attendance.models import Attendance
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Seed the database with random data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Departments
        departments = ['HR', 'IT', 'Finance', 'Marketing']
        for dept in departments:
            Department.objects.get_or_create(name=dept)

        for _ in range(40):
            department = random.choice(Department.objects.all())
            Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(
                    start_date='-5y', end_date='today'),
                department=department
            )

        employees = Employee.objects.all()
        for employee in employees:
            for i in range(30):
                date = datetime.now() - timedelta(days=i)
                status = random.choice(['P', 'A', 'L'])
                Attendance.objects.create(
                    employee=employee,
                    date=date,
                    status=status
                )

        # Create Performance Reviews
        for employee in employees:
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),

                review_date=fake.date_between(
                    start_date='-1y', end_date='today')
            )

        self.stdout.write(self.style.SUCCESS(
            'Seeding completed successfully!'))
