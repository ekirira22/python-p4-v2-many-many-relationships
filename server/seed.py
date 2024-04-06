#!/usr/bin/env python3
# server/seed.py
from faker import Faker
from random import choice as rc
import datetime
from app import app
from models import db, Employee, Meeting, Project, employee_meetings, Assignment

with app.app_context():

    # Delete all rows in tables
    db.session.query(employee_meetings).delete()
    db.session.commit()

    Employee.query.delete()
    Meeting.query.delete()
    Project.query.delete()
    Assignment.query.delete()

    # Add employees
    fake = Faker()
    employees = []

    # Add meetings and projects
    meetings = []
    projects = []
    roles = ['Project manager', 'QA Tester', 'Programmer', 'Database Admin', 'IT Support']

    for n in range(10):
        employee = Employee(name=fake.name(), hire_date=fake.past_date())
        employees.append(employee)

        meeting = Meeting(topic=fake.sentence(), scheduled_time=fake.future_datetime(end_date='+30d'), location=fake.address())
        meetings.append(meeting)

        project = Project(title=fake.sentence(),  budget=fake.random_int(min=1000, max=99999))
        projects.append(project)

        assigment = Assignment(role=rc(roles), start_date=fake.future_datetime(end_date='+5d'), end_date=fake.future_datetime(end_date='+30d'), employee=rc(employees), project=rc(projects))

        # Add random meetings to employees
        rc(employees).meetings.append(meeting)

        #Add random employees to meetings
        # rc(meetings).employees.append(employee)
    
    db.session.add_all(employees)
    db.session.add_all(meetings)
    db.session.add_all(projects)
    db.session.commit()

    # Many-to-many relationship between employee and meeting
    

    # Many-to-many relationship between employee and project through assignment