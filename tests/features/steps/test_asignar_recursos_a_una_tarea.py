from pytest_bdd import scenario, given, when, then, parsers
from src.main import API_VERSION_PREFIX
from tests.features.steps.test_crear_proyecto import headers, project
from tests.features.steps.test_crear_tarea import task


@scenario(
    "../asignar_recursos_a_una_tarea.feature",
    "Asignación de recursos a una tarea sin recursos",
)
def test_asignar_recursos_a_una_tarea_sin_recursos():
    pass


@scenario(
    "../asignar_recursos_a_una_tarea.feature",
    "Asignación de recursos a una tarea con recursos",
)
def test_asignar_recursos_a_una_tarea_con_recursos():
    pass


@scenario(
    "../asignar_recursos_a_una_tarea.feature",
    "Fallo en la asignación por datos inválidos",
)
def test_fallo_en_la_asignacion_por_datos_invalidos():
    pass


@given("una tarea sin recursos", target_fixture="task_post_response")
def step_impl(client, task, project):
    response = client.post(f"{API_VERSION_PREFIX}/projects/", json=project)
    project_id = response.json()["id"]
    return client.post(f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task)


@given(
    parsers.parse(
        "asigno al recurso con legajo {employee_id:d} como colaborador de la tarea"
    ),
    target_fixture="task_assign_collaborator_response",
)
@when(
    parsers.parse(
        "asigno al recurso con legajo {employee_id} como colaborador de la tarea"
    ),
    target_fixture="task_assign_collaborator_response",
)
def step_impl(client, task_post_response, employee_id):
    task_id = task_post_response.json()["id"]
    return client.post(
        f"{API_VERSION_PREFIX}/tasks/{task_id}/collaborators/",
        json={"employee_id": employee_id},
    )


@then(
    parsers.parse(
        "el sistema debera indicar que el recurso con legajo {employee_id:d} es colaborador de la tarea"
    )
)
def step_impl(
    client, task_assign_collaborator_response, task_post_response, employee_id
):
    assert task_assign_collaborator_response.status_code == 200
    task_id = task_post_response.json()["id"]

    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    collaborators = response.json()["collaborators"]
    assert any(collaborator["id"] == employee_id for collaborator in collaborators)


@then(
    parsers.parse(
        "el sistema debera indicar que el recurso con legajo {employee_id} es invalido"
    )
)
def step_impl(task_assign_collaborator_response, employee_id):
    assert task_assign_collaborator_response.status_code == 422
