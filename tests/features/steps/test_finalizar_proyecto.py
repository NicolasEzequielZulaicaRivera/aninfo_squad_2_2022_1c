from pytest_bdd import scenario, given, when, then
from src.constants import API_VERSION_PREFIX


@scenario("../finalizar_proyecto.feature", "Finalizar proyecto no finalizado")
def test_finalizar_proyecto_no_finalizado():
    pass


@given("un proyecto creado", target_fixture="project_post_response")
def step_impl(client, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project)


@when(
    'selecciono la opción "finalizar proyecto"',
    target_fixture="project_finalize_response",
)
def step_impl(client, project_post_response):
    project_id = project_post_response.json()["id"]
    return client.put(
        f"{API_VERSION_PREFIX}/projects/{project_id}", json={"state": "finalizado"}
    )


@then('el sistema deberá marcar el proyecto como "finalizado"')
def step_impl(client, project_finalize_response):
    assert project_finalize_response.status_code == 200
    project_id = project_finalize_response.json()["id"]
    response = client.get(f"{API_VERSION_PREFIX}/projects/{project_id}")

    returned_project = response.json()
    assert response.status_code == 200
    assert returned_project["state"] == "finalizado"
