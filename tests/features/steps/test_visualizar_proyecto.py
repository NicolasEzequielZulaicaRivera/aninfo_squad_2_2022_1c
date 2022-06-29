from datetime import date

from pytest_bdd import scenario, given, when, then
from src.main import API_VERSION_PREFIX


@scenario(
    "../visualizar_proyecto.feature", "Visualizacion de atributos basicos de proyecto"
)
def test_visualizar_proyecto():
    pass


@scenario("../visualizar_proyecto.feature", "Visualizacion de tareas de un proyecto")
def test_visualizar_tareas():
    pass


@given("un proyecto creado", target_fixture="project_post_response")
def step_impl(client, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project)


@when("selecciono el proyecto", target_fixture="project_get_by_id_response")
def step_impl(client, project_post_response):
    project_id = project_post_response.json()["id"]
    return client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")


@then("el sistema debera mostrar la informacion basica del proyecto")
def step_impl(project_get_by_id_response):
    project_info = project_get_by_id_response.json()
    assert project_get_by_id_response.status_code == 200
    assert project_info["name"] == "Proyecto de prueba"
    assert project_info["initial_date"] == str(date(2022, 6, 22))
    assert project_info["final_date"] == str(date(2022, 6, 22))
    assert "id" in project_info


@given("el proyecto tiene tareas")
def step_impl(client, project_post_response, task):
    project_id = project_post_response.json()["id"]
    client.post(f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task)


@then("el sistema debera mostrar las tareas del proyecto con su informacion basica")
def step_impl(client, project_post_response):
    project_id = project_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")
    tasks = response.json()["tasks"]
    assert response.status_code == 200
    assert len(tasks) == 1
    task = tasks[0]
    assert task["name"] == "Tarea 1"
    assert task["initial_date"] == str(date(2022, 6, 22))
    assert task["final_date"] == str(date(2022, 6, 22))
    assert "id" in task
