import pytest
from pytest_bdd import scenario, given, when, then, parsers

from src.constants import TODAY_DATE
from src.main import API_VERSION_PREFIX
from datetime import datetime, date, timedelta


@scenario("../crear_proyecto.feature", "Creacion exitosa de proyecto")
def test_create_project():
    pass


@scenario(
    "../crear_proyecto.feature",
    "Creacion fallida de proyecto por fechas de inicio y finalizacion inválidas",
)
def test_create_project_with_invalid_dates_should_fail():
    pass


@pytest.fixture
def project():
    return {
        "name": "Proyecto de prueba",
        "description": "Proyecto de prueba",
        "initial_date": str(date(2022, 6, 22)),
        "final_date": str(date(2022, 6, 22)),
    }


@pytest.fixture
def headers():
    return {
        "api_key": "key",
    }


@given("quiero crear un proyecto")
def step_impl(project):
    pass


@given(parsers.parse("quiero crear un proyecto llamado {name}"))
def step_imp(project, name):
    project["name"] = name


@given(parsers.parse("la descripcion es {description}"))
@given(parsers.parse("con descripcion {description}"))
def step_imp(project, description):
    project["description"] = description


@given(parsers.parse("la fecha de inicio es {initial_date}"))
@given(parsers.parse("con fecha de inicio {initial_date}"))
def step_imp(project, initial_date):
    project["initial_date"] = str(datetime.strptime(initial_date, "%d/%m/%Y").date())


@given(parsers.parse("la fecha de finalizacion es {final_date}"))
@given(parsers.parse("con fecha de finalizacion {final_date}"))
def step_imp(project, final_date):
    project["final_date"] = str(datetime.strptime(final_date, "%d/%m/%Y").date())


@when('selecciono la opción "nuevo proyecto"', target_fixture="response")
def response(client, headers, project):
    return client.post(f"{API_VERSION_PREFIX}/projects/", json=project, headers=headers)


@then("se deberá crear el proyecto con los datos ingresados")
def step_imp(client, headers, response, project):
    assert response.status_code == 200
    project_id = response.json()["id"]

    response = client.get(
        f"{API_VERSION_PREFIX}/projects/{project_id}", headers=headers
    )
    assert response.status_code == 200
    returned_project = response.json()
    assert returned_project["name"] == project["name"]
    assert returned_project["description"] == project["description"]
    assert returned_project["initial_date"] == project["initial_date"]
    assert returned_project["final_date"] == project["final_date"]


@then(
    "el sistema debera indicar que no fue posible crear el proyecto porque los datos son inválidos"
)
def step_impl(response):
    assert response.status_code == 422


@given("la fecha de finalizacion esta en el pasado")
def step_impl():
    project["final_date"] = str(TODAY_DATE - timedelta(days=1))
