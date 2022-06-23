from src.constants import API_VERSION_PREFIX


def test_create_task_on_project_should_return_task(client):
    response_post = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto 1",
            "description": "Descripcion del proyecto 1",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    project_id = response_post.json()["id"]
    response = client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1
    assert task["name"] == "Actualizar dependencias del proyecto"
    assert task["initial_date"] == "2022-06-12"
    assert task["final_date"] == "2022-06-20"
    assert task["project"]["id"] == 1
    assert task["project"]["name"] == "Proyecto 1"


def test_get_task_by_id_should_return_task(client):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto A",
            "description": "Descripcion del proyecto A",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    project_id = response.json()["id"]
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1
    assert task["name"] == "Actualizar dependencias del proyecto"
    assert task["initial_date"] == "2022-06-12"
    assert task["final_date"] == "2022-06-20"
    assert task["estimated_hours"] == 50
    assert task["project"]["id"] == 1
    assert task["project"]["name"] == "Proyecto A"
    assert task["collaborators"] == []
    assert task["assigned_employee"] is None


def test_edit_task_by_id_should_return_task(client):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto A",
            "description": "Descripcion del proyecto A",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    project_id = response.json()["id"]
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )

    response = client.put(
        API_VERSION_PREFIX + "/tasks/1",
        json={
            "name": "Actualizar dependencias del proyecto - actualizado",
            "description": "Actualizar infraestructura del proyecto",
            "initial_date": "2022-06-20",
            "final_date": "2022-06-23",
            "estimated_hours": None,
        },
    )

    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["id"] == 1
    assert updated_task["name"] == "Actualizar dependencias del proyecto - actualizado"
    assert updated_task["initial_date"] == "2022-06-20"
    assert updated_task["final_date"] == "2022-06-23"
    assert updated_task["estimated_hours"] is None
    assert updated_task["project"]["id"] == 1
    assert updated_task["project"]["name"] == "Proyecto A"
    assert updated_task["collaborators"] == []
    assert updated_task["assigned_employee"] is None


def test_delete_task_by_id_should_not_return_task(client):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto A",
            "description": "Descripcion del proyecto A",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    project_id = response.json()["id"]
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )

    response = client.delete(API_VERSION_PREFIX + "/tasks/1")
    assert response.status_code == 200

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    assert response.status_code == 404


def test_add_collaborator_to_task(client):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto A",
            "description": "Descripcion del proyecto A",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    project_id = response.json()["id"]
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    response = client.post(
        API_VERSION_PREFIX + "/tasks/1/collaborators/", json={"employee_id": 153038}
    )
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    task = response.json()

    assert task["collaborators"][0]["id"] == collaborator_id


def test_add_collaborator_to_task_two_times_should_return_error(client):
    response = client.post(
        API_VERSION_PREFIX + "/projects/",
        json={
            "name": "Proyecto A",
            "description": "Descripcion del proyecto A",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
        },
    )
    project_id = response.json()["id"]
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )

    response = client.post(
        API_VERSION_PREFIX + "/tasks/1/collaborators/", json={"employee_id": 153038}
    )
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    task = response.json()

    assert task["collaborators"][0]["id"] == collaborator_id

    response = client.post(
        API_VERSION_PREFIX + "/tasks/1/collaborators/", json={"employee_id": 153038}
    )
    assert response.status_code == 409


def test_remove_collaborator_from_task(client):
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
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )

    response = client.post(
        API_VERSION_PREFIX + "/tasks/1/collaborators/", json={"employee_id": 153038}
    )
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    task = response.json()

    assert task["collaborators"][0]["id"] == collaborator_id

    response = client.delete(API_VERSION_PREFIX + "/tasks/1/collaborators/153038")
    assert response.status_code == 200

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    task = response.json()

    assert len(task["collaborators"]) == 0


def test_remove_collaborator_not_in_task_should_return_error(client):
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
    client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )

    response = client.post(
        API_VERSION_PREFIX + "/tasks/1/collaborators/", json={"employee_id": 153038}
    )
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    response = client.get(API_VERSION_PREFIX + "/tasks/1")
    task = response.json()

    assert task["collaborators"][0]["id"] == collaborator_id

    response = client.delete(API_VERSION_PREFIX + "/tasks/1/collaborators/153038")
    assert response.status_code == 200

    response = client.delete(API_VERSION_PREFIX + "/tasks/1/collaborators/153038")
    assert response.status_code == 400
