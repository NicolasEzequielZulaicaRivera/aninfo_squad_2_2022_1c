from src.constants import API_VERSION_PREFIX
from tests import utils


def test_create_task_on_project_should_return_task(client):
    project_id = utils.post_project(client, name="Proyecto 1")

    response = utils.post_task(
        client,
        project_id,
        name="Actualizar dependencias del proyecto",
        description="Actualizar dependencias del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
        estimated_hours=50,
        unwrap_id=False,
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
    project_id = utils.post_project(client, name="Proyecto A")

    utils.post_task(
        client,
        project_id,
        name="Actualizar dependencias del proyecto",
        description="Actualizar dependencias del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
        estimated_hours=50,
        unwrap_id=False,
    )

    response = utils.get_task(client, 1, unwrap=False)
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
    project_id = utils.post_project(client, name="Proyecto A")

    task_id = utils.post_task(
        client,
        project_id,
        name="Actualizar dependencias del proyecto",
        description="Actualizar dependencias del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
        estimated_hours=50,
    )

    response = client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
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
    project_id = utils.post_project(client, name="Proyecto A")

    utils.post_task(
        client,
        project_id,
    )

    response = utils.delete_task(client, 1)
    assert response.status_code == 200

    response = utils.get_task(client, 1, unwrap=False)
    assert response.status_code == 404


def test_add_collaborator_to_task(client):
    project_id = utils.post_project(client, name="Proyecto A")

    task_id = utils.post_task(client, project_id)

    response = utils.add_collaborator_to_task(client, task_id, 153038, unwrap_id=False)
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    task = utils.get_task(client, task_id)

    assert task["collaborators"][0]["id"] == collaborator_id


def test_add_collaborator_to_task_two_times_should_return_error(client):
    project_id = utils.post_project(
        client,
        name="Proyecto A",
    )

    task_id = utils.post_task(client, project_id)

    response = utils.add_collaborator_to_task(client, task_id, 153038, unwrap_id=False)
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    task = utils.get_task(client, task_id)
    assert task["collaborators"][0]["id"] == collaborator_id

    response = utils.add_collaborator_to_task(client, task_id, 153038, unwrap_id=False)
    assert response.status_code == 409


def test_remove_collaborator_from_task(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)

    client.post(
        f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/",
        json={
            "name": "Actualizar dependencias del proyecto",
            "description": "Actualizar dependencias del proyecto",
            "initial_date": "2022-06-12",
            "final_date": "2022-06-20",
            "estimated_hours": 50,
        },
    )

    response = utils.add_collaborator_to_task(client, task_id, 153038, unwrap_id=False)
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    task = utils.get_task(client, task_id)
    assert task["collaborators"][0]["id"] == collaborator_id

    response = utils.remove_collaborator_from_task(client, task_id, 153038)
    assert response.status_code == 200

    task = utils.get_task(client, task_id)

    assert len(task["collaborators"]) == 0


def test_remove_collaborator_not_in_task_should_return_error(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)

    response = utils.add_collaborator_to_task(client, task_id, 153038, unwrap_id=False)
    assert response.status_code == 200
    collaborator_id = response.json()["id"]

    task = utils.get_task(client, task_id)
    assert task["collaborators"][0]["id"] == collaborator_id

    response = utils.remove_collaborator_from_task(client, task_id, 153038)
    assert response.status_code == 200

    response = utils.remove_collaborator_from_task(client, task_id, 153038)
    assert response.status_code == 400


def test_delete_task_with_collaborators(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    utils.add_collaborator_to_task(client, task_id, 25)
    utils.add_collaborator_to_task(client, task_id, 30)

    response = utils.delete_task(client, task_id)

    assert response.status_code == 200
    response = utils.get_task(client, task_id, unwrap=False)
    assert response.status_code == 404


def test_delete_project_with_task_with_collaborators(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    utils.add_collaborator_to_task(client, task_id, 25)
    utils.add_collaborator_to_task(client, task_id, 30)

    response = utils.delete_project(client, project_id)

    assert response.status_code == 200
    response = utils.get_task(client, task_id, unwrap=False)
    assert response.status_code == 404


def test_delete_task_with_collaborator_that_is_collaborator_in_another_task(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    utils.add_collaborator_to_task(client, task_id, 25)
    utils.add_collaborator_to_task(client, task_id, 30)

    task_id_2 = utils.post_task(client, project_id)
    utils.add_collaborator_to_task(client, task_id_2, 25)

    response = utils.delete_task(client, task_id)

    assert response.status_code == 200
    response = utils.get_task(client, task_id, unwrap=False)
    assert response.status_code == 404

    response = utils.get_task(client, task_id_2, unwrap=False)
    assert response.status_code == 200
    assert response.json()["collaborators"][0]["id"] == 25


def test_delete_task_with_collaborator_that_is_assigned_to_task(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    task_id_2 = utils.post_task(client, project_id)

    utils.add_collaborator_to_task(client, task_id, 25)
    utils.assign_employee_to_task(client, task_id_2, 25)

    response = utils.delete_task(client, task_id)

    assert response.status_code == 200
    response = utils.get_task(client, task_id, unwrap=False)
    assert response.status_code == 404
