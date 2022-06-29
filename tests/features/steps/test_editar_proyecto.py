from datetime import datetime

from pytest_bdd import scenario, given, when, then, parsers
from src.constants import API_VERSION_PREFIX


@scenario("../editar_proyecto.feature", "Edicion del nombre del proyecto")
def test_cambio_el_nombre_del_proyecto():
    pass


@scenario("../editar_proyecto.feature", "Edicion de la descripción del proyecto")
def test_cambio_de_la_descripcion_del_proyecto():
    pass


@scenario("../editar_proyecto.feature", "Edicion de la fecha de inicio del proyecto")
def test_cambio_de_la_fecha_de_inicio_del_proyecto():
    pass


@scenario(
    "../editar_proyecto.feature", "Edicion de la fecha de finalización del proyecto"
)
def test_cambio_de_la_fecha_de_finalizacion_del_proyecto():
    pass


@given("un proyecto creado", target_fixture="project_post_response")
def step_impl(client, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project)


@when(parsers.parse("cambio el nombre del proyecto a {new_name}"))
def step_impl(client, project, new_name, project_post_response):
    project_id = project_post_response.json()["id"]
    client.put(f"{API_VERSION_PREFIX}/projects/{project_id}", json={"name": new_name})


@then(parsers.parse("el nombre del proyecto cambió a {new_name}"))
def step_impl(client, new_name, project_post_response):
    project_id = project_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")
    assert response.json()["name"] == new_name


@when(parsers.parse("cambio la descripción del proyecto a {new_description}"))
def step_impl(client, project, new_description, project_post_response):
    project_id = project_post_response.json()["id"]
    client.put(
        f"{API_VERSION_PREFIX}/projects/{project_id}",
        json={"description": new_description},
    )


@then(parsers.parse("la descripción del proyecto cambió a {new_description}"))
def step_impl(client, new_description, project_post_response):
    project_id = project_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")
    assert response.json()["description"] == new_description


@when(parsers.parse("cambio la fecha de inicio del proyecto a {new_initial_date}"))
def step_impl(client, project, new_initial_date, project_post_response):
    project_id = project_post_response.json()["id"]
    new_initial_date = str(datetime.strptime(new_initial_date, "%d/%m/%Y").date())
    client.put(
        f"{API_VERSION_PREFIX}/projects/{project_id}",
        json={"initial_date": new_initial_date},
    )


@then(parsers.parse("la fecha de inicio del proyecto cambió a {new_initial_date}"))
def step_impl(client, new_initial_date, project_post_response):
    new_initial_date = str(datetime.strptime(new_initial_date, "%d/%m/%Y").date())
    project_id = project_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")
    assert response.json()["initial_date"] == new_initial_date


@when(
    parsers.parse("cambio la fecha de finalización del proyecto a {new_final_date}"),
    target_fixture="project_put_final_date_response",
)
def step_impl(client, project, new_final_date, project_post_response):
    project["final_date"] = str(datetime.strptime(new_final_date, "%d/%m/%Y").date())
    project_id = project_post_response.json()["id"]
    client.put(f"{API_VERSION_PREFIX}/projects/{project_id}", json=project)


@then(parsers.parse("la fecha de finalización del proyecto es {new_final_date}"))
@then(parsers.parse("la fecha de finalización del proyecto cambió a {new_final_date}"))
def step_impl(client, new_final_date, project_post_response):
    new_final_date = str(datetime.strptime(new_final_date, "%d/%m/%Y").date())
    project_id = project_post_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")
    assert response.json()["final_date"] == new_final_date


@then(
    "el sistema deberá indicar que la modificación no puede realizarse porque los datos son inválidos"
)
def step_impl(project_put_final_date_response):
    assert project_put_final_date_response.status_code == 422
