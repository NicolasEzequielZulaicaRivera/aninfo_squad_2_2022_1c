Feature: estimar horas de tarea
	"""
	Como Empleado, quiero estimar las horas de una tarea, para poder planificar el
	desarrollo del proyecto

	- CA 1: Agregar estimación de horas
	Dado que quiero agregar una estimación de horas a una tarea sin estimación
	Cuando agrego una estimación de horas
	Entonces el sistema deberá agregar la estimación de horas a la tarea

	- CA 2: Fallo al agregar una estimación de horas a una tarea por valor inválido
	Dado que quiero agregar una estimación de horas a una tarea sin estimación
	Cuando intento agregar una estimación de horas menor a 0
	Entonces el sistema deberá indicar que no fue posible agregar la estimación porque esta debe ser mayor o igual a 0

	- CA 3: Modificar estimación de horas de tarea con estimación
	Dado que quiero modificar la estimación de horas de una tarea que ya tiene
	estimación
	Cuando modifico la estimación de horas
	Entonces el sistema deberá modificar la estimación de horas de la tarea

	- CA 4: Fallo al modificar la estimación de horas de una tarea sin estimación
	Dado que quiero modificar la estimación de horas de una tarea que sin
	estimación
	Cuando intento modificar la estimación de horas
	Entonces el sistema deberá indicar que no es posible modificar la estimación de
	una tarea que no tiene una estimación

	- CA 5: Fallo al modificar la estimación de horas por valor inválido
	Dado que quiero modificar la estimación de horas de una tarea que ya tiene estimación
	Cuando intento modificar la estimación de horas con un valor menor a 0
	Entonces el sistema deberá indicar que no fue posible modificar la estimación porque esta debe ser mayor o igual a 0

	- CA 6:  Eliminar estimación de horas
	Dado que quiero eliminar la estimación de horas de una tarea que tiene una
	estimación
	Cuando elimino la estimación de horas
	Entonces el sistema deberá eliminar la estimación de horas de la tarea
	"""

	Background:
		Given un proyecto creado

	Scenario: Agregar estimación de horas
		Given una tarea sin estimacion
		When agrego una estimación de 40 horas a la tarea
		Then el sistema deberá agregar la estimación de 40 horas a la tarea

	Scenario: Eliminar estimación de horas
		Given una tarea con estimacion de 40 horas
		When elimino la estimación de horas de la tarea
		Then el sistema deberá eliminar la estimación de horas de la tarea

	Scenario: Modificar estimación de horas de tarea con estimación
		Given una tarea con estimacion de 20 horas
		When modifico una estimación de 40 horas a la tarea
		Then el sistema deberá modificar la estimación de 40 horas a la tarea

	Scenario: Fallo al agregar una estimación de horas a una tarea por valor inválido
		Given una tarea sin estimacion
		When agrego una estimación de -8 horas a la tarea
		Then el sistema deberá indicar que no fue posible agregar la estimación porque esta debe ser mayor o igual a 0

