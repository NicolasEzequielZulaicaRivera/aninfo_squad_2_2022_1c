from pytest_bdd import scenario, given, when, then, parsers
from src.main import API_VERSION_PREFIX


@scenario(
    "../asignar_responsable_de_tarea.feature",
    "Asignar responsable a una tarea sin responsable",
)
def test_asignar_responsable_de_tarea_sin_responsable():
    pass


@scenario(
    "../asignar_responsable_de_tarea.feature",
    "Fallo al asignar un responsable a una tarea con responsable",
)
def test_fallo_al_asignar_un_responsable_a_una_tarea_con_responsable():
    pass


@scenario(
    "../asignar_responsable_de_tarea.feature",
    "Solicitud de datos del responsable a asignar",
)
def test_solicitud_de_datos_del_responsable_a_asignar():
    pass


@given("una tarea sin responsable", target_fixture="task_post_response")
def step_impl(client, task, project):
    response = client.post(f"{API_VERSION_PREFIX}/projects/", json=project)
    project_id = response.json()["id"]
    return client.post(f"{API_VERSION_PREFIX}/projects/{project_id}/tasks/", json=task)


@when(
    parsers.parse(
        "intento asignar al recurso con legajo {legajo:d} como responsable de la tarea"
    ),
    target_fixture="task_assign_employee_response",
)
@given(
    parsers.parse(
        "asigno al recurso con legajo {employee_id:d} como responsable de la tarea"
    ),
    target_fixture="task_assign_employee_response",
)
@when(
    parsers.parse(
        "asigno al recurso con legajo {employee_id:d} como responsable de la tarea"
    ),
    target_fixture="task_assign_employee_response",
)
def step_impl(client, task_post_response, employee_id):
    task_id = task_post_response.json()["id"]
    return client.post(
        f"{API_VERSION_PREFIX}/tasks/{task_id}/employees/",
        json={"employee_id": employee_id},
    )


@then(
    parsers.parse(
        "el sistema debera indicar que el recurso con legajo {employee_id:d} se asignó correctamente"
    )
)
def step_impl(client, task_assign_employee_response, task_post_response, employee_id):
    assert task_assign_employee_response.status_code == 200
    task_id = task_post_response.json()["id"]

    response = client.get(f"{API_VERSION_PREFIX}/tasks/{task_id}")
    returned_task = response.json()
    assert response.status_code == 200
    assert returned_task["assigned_employee"]["id"] == employee_id


@given("una tarea con responsable")
def step_impl(client, task_post_response):
    task_id = task_post_response.json()["id"]
    client.post(
        f"{API_VERSION_PREFIX}/tasks/{task_id}/employees/",
        json={"employee_id": 1},
    )


@then(
    "el sistema debera indicar que no se puede asignar un responsable a una tarea que ya tiene un responsable"
)
def step_impl(task_assign_employee_response):
    assert task_assign_employee_response.status_code == 409


@when(
    "intento asignar a un recurso sin legajo como responsable de la tarea",
    target_fixture="task_assign_employee_response",
)
def step_impl(client, task_post_response):
    task_id = task_post_response.json()["id"]
    return client.post(f"{API_VERSION_PREFIX}/tasks/{task_id}/employees/", json={})


@then(
    "el sistema debera solicitar el legajo del empleado que quiero hacer responsable de la tarea"
)
def step_impl(task_assign_employee_response):
    assert task_assign_employee_response.status_code == 422
