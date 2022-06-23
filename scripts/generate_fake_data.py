import json
import threading

import faker
from random import randint, choice
import requests

API_VERSION_PREFIX = "/api/v1"
URL_BASE = "https://aninfo-projects.herokuapp.com" + API_VERSION_PREFIX

employees = json.loads(open("scripts/fake_database.json").read())
fake = faker.Faker()


class Task:
    def __init__(self, project):
        self.name = fake.sentence(nb_words=randint(3, 5)).replace(".", "")
        self.description = "\n".join(fake.paragraphs(nb=5))
        self.initial_date = fake.date_between(
            start_date=project.initial_date, end_date=project.final_date
        )
        self.final_date = fake.date_between(
            start_date=self.initial_date, end_date=project.final_date
        )

        if randint(0, 4) == 0:
            self.estimated_hours = None
        else:
            self.estimated_hours = randint(1, 500)

        if randint(0, 1) == 0:
            self.assigned_employee = {"legajo": choice(employees)["legajo"]}
        else:
            self.assigned_employee = None

        self.collaborators_ids = []
        for _ in range(randint(0, 10)):
            self.collaborators_ids.append(choice(employees)["legajo"])
        self.collaborators_ids = list(set(self.collaborators_ids))

    def __str__(self):
        value = f"  Task: {self.name} - Start: {self.initial_date} - Finish: {self.final_date}\n"
        if self.assigned_employee:
            value += f"  Assigned to {self.assigned_employee['Nombre']} {self.assigned_employee['Apellido']}\n"
        else:
            value += "  No assigned employee\n"
        if self.collaborators_ids:
            value += "  Collaborators:\n"
        for collaborator in self.collaborators_ids:
            value += f"  - {collaborator['Nombre']} {collaborator['Apellido']}\n"
        if not self.collaborators_ids:
            value += "  No collaborators\n"
        if self.estimated_hours:
            value += f"  Estimated hours: {self.estimated_hours}\n"
        else:
            value += "  No estimated hours\n"
        return value

    def post(self, project_id):
        url = f"{URL_BASE}/projects/{project_id}/tasks/"
        data = {
            "name": self.name,
            "description": self.description,
            "initial_date": str(self.initial_date),
            "final_date": str(self.final_date),
            "estimated_hours": self.estimated_hours,
        }
        response = requests.post(url, json=data)
        print(response.json())
        assert response.status_code == 200
        task_id = response.json()["id"]

        for collaborator_id in self.collaborators_ids:
            url = f"{URL_BASE}/tasks/{task_id}/collaborators/"
            data = {"employee_id": collaborator_id}
            response = requests.post(url, json=data)
            print(response.json())
            assert response.status_code == 200

        if self.assigned_employee:
            url = f"{URL_BASE}/tasks/{task_id}/employees/"
            data = {"employee_id": self.assigned_employee["legajo"]}
            response = requests.post(url, json=data)
            print(response.json())
            assert response.status_code == 200


class Project:
    def __init__(self):
        self.name = fake.sentence(nb_words=randint(3, 5)).replace(".", "")
        self.description = "\n".join(fake.paragraphs(nb=5))
        self.initial_date = fake.date_between(start_date="-3y", end_date="now")
        self.final_date = fake.date_between(
            start_date=self.initial_date, end_date="+3y"
        )
        self.tasks = []
        for i in range(randint(0, 50)):
            print(f"Adding task {i}")
            self.tasks.append(Task(self))

    def __str__(self):
        value = f"Project: {self.name} - Start: {self.initial_date} - Finish: {self.final_date}"
        value += "\n"
        for task in self.tasks:
            value += task.__str__()
        return value

    def post(self):
        url = f"{URL_BASE}/projects/"
        data = {
            "name": self.name,
            "description": self.description,
            "initial_date": str(self.initial_date),
            "final_date": str(self.final_date),
        }
        response = requests.post(url, json=data)
        print(response.json())
        assert response.status_code == 200

        for task in self.tasks:
            task.post(response.json()["id"])


def add_projects():
    for i in range(10):
        Project().post()


for _ in range(5):
    threading.Thread(target=add_projects).start()
