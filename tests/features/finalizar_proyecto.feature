Feature: finalizar proyecto
	"""
	Como empleado, quiero finalizar un proyecto, para marcarlo como finalizado

	- CA 1: Finalización de proyecto sin finalizar sin tareas no finalizadas
	Dado que existe un proyecto sin finalizar sin tareas no finalizadas,
	Cuando selecciono la opción "finalizar proyecto",
	Entonces el sistema deberá marcar el proyecto como "finalizado"

	- CA 2: Advertencia al finalizar un proyecto ya finalizado
	Dado que existe un proyecto finalizado,
	Cuando selecciono la opción "finalizar proyecto",
	Entonces el sistema deberá advertirme que estoy intentando finalizar un
	proyecto ya finalizado

	- CA 3: Advertencia al finalizar un proyecto con tareas no finalizadas
	Dado que existe un proyecto sin finalizar con tareas no finalizadas,
	Cuando selecciono la opción "finalizar proyecto",
	Entonces el sistema deberá advertirme que estoy intentando finalizar un
	proyecto con tareas no finalizadas

	- CA 4: Fallo al finalizar un proyecto por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para finalizar un proyecto,
	Cuando selecciono la opción "finalizar proyecto",
	Entonces el sistema deberá indicar que no tengo permisos para realizar dicha
	acción
	"""

	Scenario: Finalizar proyecto no finalizado
		Given un proyecto creado
		When selecciono la opción "finalizar proyecto"
		Then el sistema deberá marcar el proyecto como "finalizado"
