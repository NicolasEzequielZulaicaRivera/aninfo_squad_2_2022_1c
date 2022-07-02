Feature: remover recursos de tarea
	"""
	Como empleado, quiero remover un recurso de una tarea, para indicar que ya no
	participa de dicha tarea

	- CA 1: Solicitud de datos de recurso a remover
	Dado que quiero remover un recurso de una tarea,
	Cuando selecciono la opción "remover recurso",
	Entonces el sistema deberá solicitar el legajo del recurso a remover

	- CA 2: Remoción de recurso exitosa
	Dado que ingresé los datos del recurso a remover,
	Cuando selecciono la opción "remover",
	Entonces el sistema deberá remover el recurso de la tarea

	- CA 3: Fallo al remover un recurso no asignado a una tare
	Dado que quiero remover un recurso que no se encuentra asignado a la tarea,
	Cuando selecciono la opción "remover",
	Entonces el sistema deberá indicar que no es posible remover un recurso que no
	se encuentra asignado a la tarea

	- CA 4: Fallo al remover un recurso por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para remover un recurso de una tarea,
	Cuando selecciono la opción "remover recurso",
	Entonces el sistema deberá indicar que no tengo los permisos necesarios para
	realizar dicha acción

	"""

	Scenario: Remocion de recurso de tarea en la que colabora
		Given una tarea en la que colabora el recurso con legajo 5
		When selecciono la opcion "remover recurso" e ingreso el legajo 5
		Then el sistema debera indicar que el recurso con legajo 5 ya no es colaborador de la tarea

	Scenario: Fallo al remover un recurso no asignado a una tarea
		Given una tarea sin colaboradores
		When selecciono la opcion "remover recurso" e ingreso el legajo 5
		Then el sistema debera indicar que no es posible remover un recurso que no se encuentra asignado a la tarea