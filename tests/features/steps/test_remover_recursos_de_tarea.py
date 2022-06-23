from pytest_bdd import scenario, given, when, then, parsers
from src.main import API_VERSION_PREFIX
from tests.features.steps.test_crear_proyecto import project
from tests.features.steps.test_crear_tarea import task


@scenario(
    "../remover_recursos_de_tarea.feature",
    "Remocion de recurso de tarea en la que colabora",
)
def test_remover_recursos_de_tarea():
    pass


@scenario(
    "../remover_recursos_de_tarea.feature",
    "Fallo al remover un recurso no asignado a una tarea",
)
def test_fallo_al_remover_recurso_no_asignado_a_una_tarea():
    pass


@given(
    parsers.parse(
        "una tarea en la que colabora el recurso con legajo {collaborator_id}"
    ),
    target_fixture="task_id",
)
def step_impl(client, project, task, collaborator_id):
    response = client.post(API_VERSION_PREFIX + "/projects/", json=project)
    project_id = response.json()["id"]

    response_post = client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/", json=task
    )
    task_id = response_post.json()["id"]

    client.post(
        API_VERSION_PREFIX + f"/tasks/{task_id}/collaborators/",
        json={"employee_id": collaborator_id},
    )
    return task_id


@when(
    parsers.parse(
        'selecciono la opcion "remover recurso" e ingreso el legajo {collaborator_id}'
    ),
    target_fixture="task_remove_collaborator_response",
)
def step_impl(client, collaborator_id, task_id):
    return client.delete(
        API_VERSION_PREFIX + f"/tasks/{task_id}/collaborators/{collaborator_id}"
    )


@then(
    parsers.parse(
        "el sistema debera indicar que el recurso con legajo {collaborator_id} ya es colaborador de la tarea"
    )
)
def step_impl(client, task_id, task_remove_collaborator_response, collaborator_id):
    assert task_remove_collaborator_response.status_code == 200

    response = client.get(API_VERSION_PREFIX + f"/tasks/{task_id}")

    assert response.status_code == 200
    assert not any(
        collaborator["id"] == collaborator_id
        for collaborator in response.json()["collaborators"]
    )


@given("una tarea sin colaboradores", target_fixture="task_id")
def step_impl(client, task, project):
    response = client.post(API_VERSION_PREFIX + "/projects/", json=project)
    project_id = response.json()["id"]

    response_post = client.post(
        API_VERSION_PREFIX + f"/projects/{project_id}/tasks/", json=task
    )
    task_id = response_post.json()["id"]
    return task_id


@then(
    "el sistema debera indicar que no es posible remover un recurso que no se encuentra asignado a la tarea"
)
def step_impl(task_remove_collaborator_response):
    assert task_remove_collaborator_response.status_code == 400
