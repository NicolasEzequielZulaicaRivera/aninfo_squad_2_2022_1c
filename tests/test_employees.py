from src.constants import API_VERSION_PREFIX


def test_add_employee_to_task_should_return_task_with_employee_id(client):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto A",
            "description": "Descripcion del proyecto A",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )
    project_id = response.json()["id"]
    response_post = client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )
    task_id = response_post.json()["id"]
    response = client.post(
        API_VERSION_PREFIX + f"/tasks/{task_id}/employees/", json={"employee_id": 25}
    )
    assert response.status_code == 200
