[![Pipeline](https://github.com/NicolasEzequielZulaicaRivera/aninfo_squad_2_2022_1c/actions/workflows/pipeline.yml/badge.svg?branch=master)](https://github.com/NicolasEzequielZulaicaRivera/aninfo_squad_2_2022_1c/actions/workflows/pipeline.yml)
[![](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/docs-fastapi-blue.svg)](https://fastapi.tiangolo.com/)


# Módulo de proyectos

## Links

- [🗃️ Squad Drive](https://drive.google.com/drive/folders/1tgJLJsmCotfn_13ujyAJihNR38PKLGJT)
- [👥 Tribe Repo](https://github.com/NicolasEzequielZulaicaRivera/aninfo_tribu_1_2022_1c)

## Installing the project

The only dependency required to use this template is [poetry](https://python-poetry.org). The recommended method to install it is through [pip](https://pypi.org/project/pip/).

```bash
$ pip3 install poetry
$ poetry config virtualenvs.in-project true
```

Remember to commit to the repo the `poetry.lock` file generated by `poetry install`.

### Initiating the venv

```
$ poetry shell
```

## Dependencies

The virtual environment is automatically created and activated via poetry.

```
$ cd to-project-path
$ poetry install
```

To make sure everything is set up correctly, run the following command which must show the virtual environment path:

```
$ poetry show -v
```

### Adding new dependencies

Check the [full poetry docs](https://python-poetry.org/docs/cli/), but here goes a quick reminder,

```bash
poetry add <dependency> [--dev]
```

### Style guide

This template follows [PEP8](https://www.python.org/dev/peps/pep-0008/).

For this purpose, we use:

- [black](https://github.com/psf/black): an opinionated code formatting tool
- [flake8](https://github.com/PyCQA/flake8): a tool to enforce style guide
- [pylint](https://github.com/PyCQA/pylint): a source code, bug and quality checker

**Linters**

```bash
flake8 && pylint <module_name>
```

```bash
flake8 . && pylint src
```

**Formatter**

```bash
black .
```
