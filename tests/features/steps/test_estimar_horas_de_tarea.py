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
    "Eliminar estimación de horas",
)
def test_eliminar_estimacion_de_horas():
    pass


@scenario(
    "../estimar_horas_de_tarea.feature",
    "Modificar estimación de horas de tarea con estimación",
)
def test_modificar_estimacion_de_horas_de_tarea_con_estimacion():
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


@when(
    "elimino la estimación de horas de la tarea", target_fixture="updated_task_response"
)
def step_impl(client, task_id, task):
    task["estimated_hours"] = None
    return client.put(API_VERSION_PREFIX + "/tasks/{}".format(task_id), json=task)


@then("el sistema deberá eliminar la estimación de horas de la tarea")
def step_impl(task, updated_task_response):
    task_info = updated_task_response.json()
    assert updated_task_response.status_code == 200
    assert task_info["name"] == task["name"]
    assert task_info["initial_date"] == task["initial_date"]
    assert task_info["final_date"] == task["final_date"]
    assert task_info["description"] == task["description"]
    assert task_info["estimated_hours"] is None


@when(
    parsers.parse("modifico una estimación de {estimated_hours:d} horas a la tarea"),
    target_fixture="updated_task_response",
)
def step_impl(client, estimated_hours, task, task_id):
    task["estimated_hours"] = estimated_hours
    return client.put(
        API_VERSION_PREFIX + "/tasks/{}".format(task_id),
        json=task,
    )


@then(
    parsers.parse(
        "el sistema deberá modificar la estimación de {new_estimated_hours:d} horas a la tarea"
    )
)
def step_impl(updated_task_response, new_estimated_hours, task):
    task_info = updated_task_response.json()
    assert updated_task_response.status_code == 200
    assert task_info["estimated_hours"] == new_estimated_hours
    assert task_info["name"] == task["name"]
    assert task_info["initial_date"] == task["initial_date"]
    assert task_info["final_date"] == task["final_date"]
    assert task_info["description"] == task["description"]
