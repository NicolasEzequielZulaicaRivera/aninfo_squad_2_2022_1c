from datetime import date

from pytest_bdd import scenario, given, when, then
from src.main import API_VERSION_PREFIX


@scenario("../visualizar_tarea.feature", "Visualizacion de atributos basicos de tarea")
def test_visualizar_tarea():
    pass


@given("una tarea", target_fixture="task_post_response")
def step_impl(client, task):
    response = client.post(f"{API_VERSION_PREFIX}/projects/", json=task)
    project_id = response.json()["id"]
    return client.post(f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task)


@when("selecciono la tarea", target_fixture="task_get_by_id_response")
def step_impl(client, task_post_response):
    task_id = task_post_response.json()["id"]
    return client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")


@then("el sistema deberá mostrar la informacion basica de la tarea")
def step_impl(task_get_by_id_response):
    assert task_get_by_id_response.status_code == 200
    task = task_get_by_id_response.json()
    assert task["id"] is not None
    assert task["name"] == "Tarea 1"
    assert task["description"] == "Tarea de prueba"
    assert task["initial_date"] == str(date(2022, 6, 22))
    assert task["final_date"] == str(date(2022, 6, 22))
    assert task["assigned_employee"] is None
    assert len(task["collaborators"]) == 0
