from tests import utils


def test_assign_employee_to_task_should_return_task_with_employee_id(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    response = utils.assign_employee_to_task(client, task_id, 25)

    assert response.status_code == 200
    task = utils.get_task(client, task_id)
    assert task["assigned_employee"] == 25


def test_remove_assigned_employee_from_task_should_remove_assigned_employee_from_task(
    client,
):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    utils.assign_employee_to_task(client, task_id, 25)

    response = utils.remove_assigned_employee_from_task(client, task_id)

    assert response.status_code == 200
    task = utils.get_task(client, task_id)
    assert task["assigned_employee"] is None


def test_remove_assigned_employee_from_task_without_assigned_employee_should_fail(
    client,
):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)

    response = utils.remove_assigned_employee_from_task(client, task_id)

    assert response.status_code == 400


def test_assign_employee_to_task_that_already_has_an_employee_should_fail(client):
    project_id = utils.post_project(client)

    task_id = utils.post_task(client, project_id)
    utils.assign_employee_to_task(client, task_id, 25)

    response = utils.assign_employee_to_task(client, task_id, 30)

    assert response.status_code == 409


def test_assign_employee_to_task_that_does_not_exist_should_fail(client):
    response = utils.assign_employee_to_task(client, 1, 30)

    assert response.status_code == 404


def test_remove_assigned_employee_from_task_that_does_not_exist_should_fail(client):
    response = utils.remove_assigned_employee_from_task(client, 1)

    assert response.status_code == 404
