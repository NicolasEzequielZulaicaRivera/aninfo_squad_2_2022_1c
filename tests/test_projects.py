from src.constants import API_VERSION_PREFIX


def test_get_projects_should_return_no_projects(client):
    response = client.get(API_VERSION_PREFIX + "/projects/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_project_by_id_should_return_no_project(client):
    response = client.get(API_VERSION_PREFIX + "/projects/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_create_project_should_return_created_project(client):
    response = client.post(API_VERSION_PREFIX + "/projects/", json={
        "name": "Proyecto secreto",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-20",
        "estimated_hours": 50,
    })
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto secreto"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-20"
    assert project["estimated_hours"] == 50


def test_can_exist_projects_with_same_name(client):
    client.post(API_VERSION_PREFIX + "/projects/", json={
        "name": "Proyecto secreto",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-20",
        "estimated_hours": 50,
    })
    response = client.post(API_VERSION_PREFIX + "/projects/", json={
        "name": "Proyecto secreto",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-30",
        "estimated_hours": 50,
    })
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 2
    assert project["name"] == "Proyecto secreto"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-30"
    assert project["estimated_hours"] == 50


def test_get_project_after_it_was_created(client):
    client.post(API_VERSION_PREFIX + "/projects/", json={
        "name": "Proyecto secreto",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-20",
        "estimated_hours": 50,
    })
    response = client.get(API_VERSION_PREFIX + "/projects/1")
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto secreto"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-20"
    assert project["estimated_hours"] == 50


def test_edit_project_should_return_edited_project(client):
    client.post(API_VERSION_PREFIX + "/projects/", json={
        "name": "Proyecto secreto",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-20",
        "estimated_hours": 50,
    })
    response = client.put(API_VERSION_PREFIX + "/projects/1", json={
        "name": "Proyecto secreto editado",
        "initial_date": "2022-06-15",
        "final_date": "2022-06-25",
        "estimated_hours": 100,
    })
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto secreto editado"
    assert project["initial_date"] == "2022-06-15"
    assert project["final_date"] == "2022-06-25"
    assert project["estimated_hours"] == 100


def test_delete_project_should_not_return_project(client):
    client.post(API_VERSION_PREFIX + "/projects/", json={
        "name": "Proyecto",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-20",
        "estimated_hours": 50,
    })
    response = client.delete(API_VERSION_PREFIX + "/projects/1")
    assert response.status_code == 200
    response = client.get(API_VERSION_PREFIX + "/projects/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}






