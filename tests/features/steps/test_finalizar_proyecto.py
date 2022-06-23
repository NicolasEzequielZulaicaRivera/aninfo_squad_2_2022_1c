from pytest_bdd import scenario, given, when, then
from tests.features.steps.test_crear_proyecto import headers, project
from tests.features.steps.test_crear_tarea import task
from src.constants import API_VERSION_PREFIX


@scenario("../finalizar_proyecto.feature", "Finalizar proyecto no finalizado")
def test_finalizar_proyecto_no_finalizado():
    pass


@scenario(
    "../finalizar_proyecto.feature", "Fallo al finalizar un proyecto ya finalizado"
)
def test_fallo_al_finalizar_un_proyecto_ya_finalizado():
    pass


@scenario(
    "../finalizar_proyecto.feature",
    "Fallo al finalizar un proyecto con tareas no finalizadas",
)
def test_fallo_al_finalizar_un_proyecto_con_tareas_no_finalizadas():
    pass


@given("un proyecto creado", target_fixture="project_post_response")
def step_impl(client, headers, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project, headers=headers)


@given("el proyecto ya está finalizado", target_fixture="project_finalize_response")
@when(
    'selecciono la opción "finalizar proyecto"',
    target_fixture="project_finalize_response",
)
def step_impl(client, project_post_response):
    project_id = project_post_response.json()["id"]
    return client.put(
        f"{API_VERSION_PREFIX}/projects/{project_id}", json={"finished": True}
    )


@then('el sistema deberá marcar el proyecto como "finalizado"')
def step_impl(client, project_finalize_response):
    assert project_finalize_response.status_code == 200
    project_id = project_finalize_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")

    returned_project = response.json()
    assert response.status_code == 200
    assert returned_project["finished"] == True


@then("el sistema deberá indicar que no es posible finalizar un proyecto ya finalizado")
def step_impl(project_finalize_response):
    assert project_finalize_response.status_code == 400


@given("el proyecto tiene tareas no finalizadas")
def step_impl(client, project_post_response, task):
    project_id = project_post_response.json()["id"]
    client.post(
        f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/",
        json=task,
    )


@then(
    "el sistema deberá indicar que no es posible finalizar un proyecto con tareas no finalizadas"
)
def step_impl(project_finalize_response):
    assert project_finalize_response.status_code == 400
