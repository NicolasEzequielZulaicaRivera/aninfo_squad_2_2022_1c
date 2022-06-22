from pytest_bdd import scenario, given, when, then
from src.constants import API_VERSION_PREFIX


@scenario("features/crear_proyecto.feature", "Creacion exitosa")
def test_crear_proyecto():
    pass


# Target fixture works as a dependency for the next step, i.e, project_data is available
# for the 'when' step as a parameter.
@given("ingrese los datos del proyecto", target_fixture="project_data")
def set_up_project():
    return {
        "name": "Proyecto 1",
        "description": "Descripcion del proyecto 1",
        "initial_date": "2022-06-12",
        "final_date": "2022-06-20",
        "estimated_hours": 100,
    }


@when('selecciono la opcion "crear proyecto"', target_fixture="response")
def send_project(client, project_data):
    return client.post(API_VERSION_PREFIX + "/projects/", json=project_data)


@then("se debera crear el proyecto con los datos correspondientes")
def project_is_created(response):
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == 1
    assert project["name"] == "Proyecto 1"
    assert project["initial_date"] == "2022-06-12"
    assert project["final_date"] == "2022-06-20"
