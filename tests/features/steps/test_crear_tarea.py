from datetime import date, datetime
from pytest_bdd import scenario, given, when, then, parsers
import pytest

from src.constants import API_VERSION_PREFIX
from tests.features.steps.test_crear_proyecto import headers, project


@scenario("../crear_tarea.feature", "Crear tarea en proyecto")
def test_crear_tarea_en_proyecto():
    pass


@scenario("../crear_tarea.feature", "Creacion fallida de tarea en proyecto")
def test_crear_tarea_en_proyecto_fallida():
    pass


@scenario(
    "../crear_tarea.feature",
    "Fallo en la creacion por fecha de incio posterior a la fecha de finalizacion",
)
def test_fallo_en_la_creacion_por_fecha_de_inicio_posterior_a_la_fecha_de_finalizacion():
    pass


@scenario(
    "../crear_tarea.feature",
    "Fallo en la creacion por fecha de inicio posterior a la fecha de finalizacion del proyecto",
)
def test_fallo_en_la_creacion_por_fecha_de_inicio_posterior_a_la_fecha_de_finalizacion_del_proyecto():
    pass


@pytest.fixture
def task():
    return {
        "name": "Tarea 1",
        "description": "Tarea de prueba",
        "initial_date": str(date(2022, 6, 22)),
        "final_date": str(date(2022, 6, 22)),
    }


@given("un proyecto creado", target_fixture="project_post_response")
def step_impl(client, headers, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project, headers=headers)


@given("quiero crear una tarea en un proyecto")
def step_impl():
    pass


@given(parsers.parse("el nombre de la tarea es {name}"))
def step_impl(task, name):
    task["name"] = name


@given(parsers.parse("la descripcion de la tarea es {description}"))
def step_impl(task, description):
    task["description"] = description


@given(parsers.parse("la fecha de inicio de la tarea es {initial_date}"))
def step_impl(task, initial_date):
    task["initial_date"] = str(datetime.strptime(initial_date, "%d/%m/%Y").date())


@given(parsers.parse("la fecha de finalizacion de la tarea es {final_date}"))
def step_impl(task, final_date):
    task["final_date"] = str(datetime.strptime(final_date, "%d/%m/%Y").date())


@when('selecciono la opcion "nueva tarea"', target_fixture="task_post_response")
def response(client, headers, task, project_post_response):
    project_id = project_post_response.json()["id"]
    return client.post(
        f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task, headers=headers
    )


@then("se debera crear la tarea con los datos ingresados")
def step_impl(client, headers, task_post_response, task):
    assert task_post_response.status_code == 200
    task_id = task_post_response.json()["id"]

    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}", headers=headers)
    returned_task = response.json()
    assert response.status_code == 200
    assert returned_task["name"] == task["name"]
    assert returned_task["description"] == task["description"]
    assert returned_task["initial_date"] == task["initial_date"]
    assert returned_task["final_date"] == task["final_date"]


@given("la tarea no puede crearse exitosamente")
def step_impl(task):
    task["final_date"] = ""


@then(
    "el sistema debera informar que no se pudo crear la tarea, y debera permitir crearla nuevamente"
)
def step_impl(task_post_response):
    assert task_post_response.status_code == 422
