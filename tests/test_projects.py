from src.constants import API_VERSION_PREFIX
from tests import utils


def test_get_projects_should_return_no_projects(client):
    response = utils.get_projects(client, unwrap=False)
    assert response.status_code == 200
    assert response.json() == []


def test_get_project_by_id_should_return_no_project(client):
    response = utils.get_project(client, 1, unwrap=False)
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_create_project_should_return_created_project_with_no_tasks(client):
    response = utils.post_project(
        client,
        name="Proyecto secreto",
        description="Descripcion del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
        unwrap_id=False,
    )
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto secreto"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-20"
    assert project["tasks"] == []


def test_can_exist_projects_with_same_name(client):
    utils.post_project(
        client,
        name="Proyecto secreto",
        description="Descripcion del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
    )

    response = utils.post_project(
        client,
        name="Proyecto secreto",
        description="Descripcion del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-30",
        unwrap_id=False,
    )

    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 2
    assert project["name"] == "Proyecto secreto"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-30"
    assert project["tasks"] == []


def test_get_project_after_it_was_created(client):
    project_id = utils.post_project(
        client,
        name="Proyecto secreto",
        description="Descripcion del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
    )

    response = utils.get_project(client, project_id, unwrap=False)
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto secreto"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-20"
    assert project["tasks"] == []


def test_edit_project_should_return_edited_project(client):
    project_id = utils.post_project(
        client,
        name="Proyecto secreto",
        description="Descripcion del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
    )

    response = client.put(
        f"{API_VERSION_PREFIX}/projects/{project_id}",
        json={
            "name": "Proyecto secreto editado",
            "description": "Descripcion actualizada",
            "initial_date": "2022-06-15",
            "final_date": "2022-06-25",
        },
    )
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto secreto editado"
    assert project["description"] == "Descripcion actualizada"
    assert project["initial_date"] == "2022-06-15"
    assert project["final_date"] == "2022-06-25"
    assert project["tasks"] == []


def test_delete_project_should_not_return_project(client):
    project_id = utils.post_project(
        client,
        name="Proyecto",
        description="Descripcion del proyecto",
        initial_date="2022-06-12",
        final_date="2022-06-20",
    )

    response = utils.delete_project(client, project_id)
    assert response.status_code == 200
    response = utils.get_project(client, project_id, unwrap=False)
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}
