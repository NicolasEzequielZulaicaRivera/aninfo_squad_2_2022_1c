Feature: asignar recursos a una tarea
	"""
	Como empleado, quiero asignar recursos a una tarea, para que puedan participar
	del desarrollo de la tarea

	- CA 1: Solicitud de datos del recurso a asignar
	Dado que quiero asignar un recurso a una tarea,
	Cuando selecciono la opción "asignar recursos" en la tarea,
	Entonces el sistema deberá solicitar el ingreso del legajo del recurso a
	asignar

	- CA 2: Asignación de recursos exitosa
	Dado que ingresé los datos del recurso a asignar,
	Cuando selecciono la opción "asignar recurso",
	Entonces se deberá asignar el recurso a la tarea

	- CA 3: Fallo en la asignación por datos inválidos
	Dado que quiero asignar un recurso a una tarea,
	Cuando ingreso un legajo inválido,
	Entonces el sistema deberá indicar que el recurso es invalido

	- CA 4: Fallo en la asignación por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para asignar un recurso a una tarea,
	Cuando selecciono la opción "asignar recursos",
	Entonces el sistema deberá indicar que no tengo permisos para realizar dicha
	acción
	"""

	Scenario: Asignación de recursos a una tarea sin recursos
		Given una tarea sin recursos
		When asigno al recurso con legajo 5 como colaborador de la tarea
		Then el sistema debera indicar que el recurso con legajo 5 es colaborador de la tarea

	Scenario: Asignación de recursos a una tarea con recursos
		Given una tarea sin recursos
		And asigno al recurso con legajo 5 como colaborador de la tarea
		When asigno al recurso con legajo 6 como colaborador de la tarea
		Then el sistema debera indicar que el recurso con legajo 6 es colaborador de la tarea

	Scenario: Fallo en la asignación por datos inválidos
		Given una tarea sin recursos
		When asigno al recurso con legajo x como colaborador de la tarea
		Then el sistema debera indicar que el recurso con legajo x es invalido