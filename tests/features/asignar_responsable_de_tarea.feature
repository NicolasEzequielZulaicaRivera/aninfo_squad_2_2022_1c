Feature: asignar responsable de tarea
	"""
	Como empleado, quiero asignar un responsable a una tarea, para indicar que es
	responsable de que se realice la tarea

	- [x] CA 1: Solicitud de datos del responsable a asignar
	Dado que quiero asignar un responsable a una tarea,
	Cuando selecciono la opción "asignar responsable",
	Entonces el sistema deberá solicitar el legajo del empleado que quiero hacer
	responsable de la tarea

	- CA 2: Asignación de responsable a una tarea sin responsable
	Dado que quiero asignar un responsable a una tarea sin responsable,
	Cuando asigno al responsable,
	Entonces el sistema deberá indicar que el responsable se asignó correctamente

	- CA 3: Fallo al asignar un responsable a una tarea con responsable
	Dado que quiero asignar un responsable a una tarea con responsable,
	Cuando selecciono la opción "asignar responsable",
	Entonces el sistema deberá indicar que no se puede asignar un responsable a una
	tarea que ya tiene un responsable

	- CA 4: Fallo al asignar un responsable por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para asignar un responsable a una
	tarea,
	Cuando selecciono la opción "asignar responsable",
	Entonces el sistema deberá indicar que no tengo los permisos necesarios para
	realizar dicha acción

	"""
	Scenario: Solicitud de datos del responsable a asignar
		Given una tarea sin responsable
		When intento asignar a un recurso sin legajo como responsable de la tarea
		Then el sistema debera solicitar el legajo del empleado que quiero hacer responsable de la tarea

	Scenario: Asignar responsable a una tarea sin responsable
		Given una tarea sin responsable
		When asigno al recurso con legajo 5 como responsable de la tarea
		Then el sistema debera indicar que el recurso con legajo 5 se asignó correctamente

	Scenario: Fallo al asignar un responsable a una tarea con responsable
		Given una tarea sin responsable
		And asigno al recurso con legajo 3 como responsable de la tarea
		When intento asignar al recurso con legajo 5 como responsable de la tarea
		Then el sistema debera indicar que no se puede asignar un responsable a una tarea que ya tiene un responsable
