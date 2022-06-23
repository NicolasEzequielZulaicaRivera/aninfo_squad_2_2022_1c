from pytest_bdd import scenario, given, when, then
from tests.features.steps.test_crear_proyecto import headers, project
from tests.features.steps.test_crear_tarea import task
from src.main import API_VERSION_PREFIX


@scenario("../finalizar_tarea.feature", "Finalizar tarea sin finalizar")
def test_finalizar_tarea_sin_finalizar():
    pass


@scenario("../finalizar_tarea.feature", "Fallo al finalizar una tarea ya finalizada")
def test_fallo_al_finalizar_una_tarea_ya_finalizada():
    pass


@given("una tarea sin finalizar", target_fixture="task_post_response")
def step_impl(client, project, task):
    response = client.post(
        f"{API_VERSION_PREFIX}/projects/", json=project
    )

    project_id = response.json()["id"]
    return client.post(
        f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task
    )


@given('selecciono la opción "finalizar tarea"', target_fixture="task_finalize_response")
@when('selecciono la opción "finalizar tarea"', target_fixture="task_finalize_response")
def step_impl(client, task_post_response):
    task_id = task_post_response.json()["id"]
    return client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
        json={"finished": True},
    )


@then('el sistema deberá modificar el estado de la tarea a "finalizada"')
def step_impl(client, task_finalize_response):
    assert task_finalize_response.status_code == 200
    task_id = task_finalize_response.json()["id"]

    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    returned_task = response.json()
    assert response.status_code == 200
    assert returned_task["finished"] == True


@given("una tarea finalizada")
def step_impl(client, task_post_response):
    task_id = task_post_response.json()["id"]
    client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
        json={"finished": True},
    )


@then("el sistema deberá indicar que no es posible finalizar una tarea ya finalizada")
def step_impl(task_finalize_response):
    assert task_finalize_response.status_code == 400
