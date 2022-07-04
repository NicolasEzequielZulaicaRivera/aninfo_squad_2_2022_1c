from src.main import API_VERSION_PREFIX


def post_project(
    client,
    name="Proyecto A",
    description="Descripcion del proyecto A",
    initial_date="2022-06-12",
    final_date="2022-06-20",
    estimated_hours=50,
    unwrap_id=True,
):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": name,
            "description": description,
            "initial_date": initial_date,
            "final_date": final_date,
            "estimated_hours": estimated_hours,
        },
    )
    if unwrap_id:
        return response.json()["id"]
    return response


def get_project(client, project_id, unwrap=True):
    response = client.get(API_VERSION_PREFIX + f"/projects/{project_id}")
    if unwrap:
        return response.json()
    return response


def get_projects(client, unwrap=True):
    response = client.get(API_VERSION_PREFIX + "/projects/")
    if unwrap:
        return response.json()
    return response


def delete_project(client, project_id):
    response = client.delete(API_VERSION_PREFIX + f"/projects/{project_id}")
    return response


def post_task(
    client,
    project_id,
    name="Actualizar dependencias del proyecto",
    description="Actualizar dependencias del proyecto",
    initial_date="2022-06-12",
    final_date="2022-06-20",
    estimated_hours=50,
    assigned_employee=None,
    unwrap_id=True,
):
    response = client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": name,
            "description": description,
            "initial_date": initial_date,
            "final_date": final_date,
            "estimated_hours": estimated_hours,
            "assigned_employee": assigned_employee,
        },
    )

    if unwrap_id:
        return response.json()["id"]
    return response


def delete_task(
    client,
    task_id,
):
    response = client.delete(API_VERSION_PREFIX + f"/tasks/{task_id}")
    return response


def assign_employee_to_task(client, task_id, employee_id):
    response = client.post(
        API_VERSION_PREFIX + f"/tasks/{task_id}/employees/",
        json={"employee_id": employee_id},
    )
    return response


def remove_assigned_employee_from_task(client, task_id):
    response = client.delete(API_VERSION_PREFIX + f"/tasks/{task_id}/employees/")
    return response


def get_task(client, task_id, unwrap=True):
    response = client.get(API_VERSION_PREFIX + f"/tasks/{task_id}")
    if unwrap:
        return response.json()
    return response


def add_collaborator_to_task(
    client,
    task_id,
    employee_id,
    unwrap_id=True,
):
    response = client.post(
        API_VERSION_PREFIX + f"/tasks/{task_id}/collaborators/",
        json={"employee_id": employee_id},
    )
    if unwrap_id:
        return response.json()["id"]
    return response


def remove_collaborator_from_task(client, task_id, collaborator_id):
    response = client.delete(
        API_VERSION_PREFIX + f"/tasks/{task_id}/collaborators/{collaborator_id}"
    )
    return response
