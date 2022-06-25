from pytest_bdd import scenario, given, when, then, parsers

from src.constants import API_VERSION_PREFIX


@scenario(
    "../estimar_horas_de_tarea.feature",
    "Agregar estimación de horas",
)
def test_agregar_estimacion_de_horas():
    pass


@scenario(
    "../estimar_horas_de_tarea.feature",
    "Fallo al agregar una estimación de horas a una tarea con estimación",
)
def test_fallo_agregar_estimacion_de_horas_a_tarea_con_estimacion():
    pass


@given("un proyecto creado", target_fixture="project_post_response")
def step_impl(client, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project)


@given("una tarea sin estimacion", target_fixture="task_id")
def step_impl(client, task):
    response = client.post(
        API_VERSION_PREFIX + "/projects/{}/tasks/".format(1), json=task
    )
    return response.json()["id"]


@when(
    parsers.parse("agrego una estimación de {estimated_hours:d} horas a la tarea"),
    target_fixture="estimated_hours_response",
)
def step_impl(client, estimated_hours, task, task_id):
    task["estimated_hours"] = estimated_hours
    return client.put(
        API_VERSION_PREFIX + "/tasks/{}".format(task_id),
        json=task,
    )


@then(
    parsers.parse(
        "el sistema deberá agregar la estimación de {estimated_hours:d} horas a la tarea"
    )
)
def step_impl(estimated_hours_response, estimated_hours, task):
    task_info = estimated_hours_response.json()
    assert estimated_hours_response.status_code == 200
    assert task_info["estimated_hours"] == estimated_hours
    assert task_info["name"] == task["name"]
    assert task_info["initial_date"] == task["initial_date"]
    assert task_info["final_date"] == task["final_date"]


@given(
    parsers.parse("una tarea con estimacion de {estimated_hours:d} horas"),
    target_fixture="task_id",
)
def step_impl(client, task, estimated_hours):
    task["estimated_hours"] = estimated_hours
    response = client.post(
        API_VERSION_PREFIX + "/projects/{}/tasks/".format(1), json=task
    )
    return response.json()["id"]


@then(
    "el sistema deberá indicar que no es posible agregar una estimación a una tarea que ya tiene una estimación"
)
def step_impl(estimated_hours_response):
    assert estimated_hours_response.status_code == 400
