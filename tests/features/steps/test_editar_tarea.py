from datetime import datetime

from pytest_bdd import scenario, given, when, then, parsers

from src.constants import API_VERSION_PREFIX
from tests.features.steps.test_crear_tarea import task
from tests.features.steps.test_crear_proyecto import headers, project


@scenario("../editar_tarea.feature", "Edicion del nombre de la tarea")
def test_cambio_el_nombre_de_la_tarea():
    pass


@scenario("../editar_tarea.feature", "Edicion de la descripcion de la tarea")
def test_cambio_de_la_descripcion_de_la_tarea():
    pass


@scenario("../editar_tarea.feature", "Edicion de la fecha de inicio de la tarea")
def test_cambio_de_la_fecha_de_inicio_de_la_tarea():
    pass


@scenario("../editar_tarea.feature", "Edicion de la fecha de finalizacion de la tarea")
def test_cambio_de_la_fecha_de_finalizacion_de_la_tarea():
    pass


@scenario("../editar_tarea.feature", "Fallo al editar una tarea por fechas inválidas")
def test_fallo_al_editar_una_tarea_por_fechas_invalidas():
    pass


@given("una tarea", target_fixture="task_post_response")
def step_impl(client, task, project, headers):
    response = client.post(
        f"{API_VERSION_PREFIX}/projects/", json=project, headers=headers
    )
    project_id = response.json()["id"]
    return client.post(
        f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task, headers=headers
    )


@when(parsers.parse("cambio el nombre de la tarea a {new_name}"))
def step_impl(client, task_post_response, new_name, headers):
    task_id = task_post_response.json()["id"]
    client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
        json={"name": new_name},
        headers=headers,
    )


@then(parsers.parse("el nombre de la tarea cambió a {new_name}"))
def step_impl(client, new_name, task_post_response):
    task_id = task_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    assert response.json()["name"] == new_name


@when(parsers.parse("cambio la descripcion de la tarea a {new_description}"))
def step_impl(client, task_post_response, new_description, headers):
    task_id = task_post_response.json()["id"]
    client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
        json={"description": new_description},
        headers=headers,
    )


@then(parsers.parse("la descripcion de la tarea cambió a {new_description}"))
def step_impl(client, new_description, task_post_response):
    task_id = task_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    assert response.json()["description"] == new_description


@when(parsers.parse("cambio la fecha de inicio de la tarea a {new_initial_date}"))
def step_impl(client, task_post_response, new_initial_date, headers):
    task_id = task_post_response.json()["id"]
    new_initial_date = str(datetime.strptime(new_initial_date, "%d/%m/%Y").date())
    client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
        json={"initial_date": new_initial_date},
        headers=headers,
    )


@then(parsers.parse("la fecha de inicio de la tarea cambió a {new_initial_date}"))
def step_impl(client, new_initial_date, task_post_response):
    task_id = task_post_response.json()["id"]
    new_initial_date = str(datetime.strptime(new_initial_date, "%d/%m/%Y").date())
    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    assert response.json()["initial_date"] == new_initial_date


@when(
    parsers.parse("cambio la fecha de finalizacion de la tarea a {new_final_date}"),
    target_fixture="task_update_final_date_response",
)
def step_impl(client, task_post_response, new_final_date, headers):
    task_id = task_post_response.json()["id"]
    new_final_date = str(datetime.strptime(new_final_date, "%d/%m/%Y").date())
    return client.put(
        f"{API_VERSION_PREFIX}/tasks/{task_id}",
        json={"final_date": new_final_date},
        headers=headers,
    )


@then(parsers.parse("la fecha de finalizacion de la tarea cambió a {new_final_date}"))
def step_impl(client, new_final_date, task_post_response):
    task_id = task_post_response.json()["id"]
    new_final_date = str(datetime.strptime(new_final_date, "%d/%m/%Y").date())
    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    assert response.json()["final_date"] == new_final_date


@then(
    "el sistema deberá indicar que la modificación de la tarea puede realizarse porque los datos son inválidos"
)
def step_impl(task_update_final_date_response):
    assert task_update_final_date_response.status_code == 422
