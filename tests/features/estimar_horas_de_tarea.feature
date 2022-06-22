Feature: estimar horas de tarea
	"""
	Como Empleado, quiero estimar las horas de una tarea, para poder planificar el
	desarrollo del proyecto

	- CA 1: Agregar estimación de horas
	Dado que quiero agregar una estimación de horas a una tarea sin estimación
	Cuando agrego una estimación de horas
	Entonces el sistema deberá agregar la estimación de horas a la tarea

	- CA 2: Fallo al agregar una estimación de horas a una tarea con estimación
	Dado que quiro agregar una estimación de horas a una tarea con estimación
	Cuando intento agregar una estimación de horas
	Entonces el sistema deberá indicar que no es posible agregar una estimación a
	una tarea que ya tiene una estimación, sino que se debe modificar la estimación
	existente

	- CA 3: Fallo al agregar una estimación de horas a una tarea por valor inválido
	Dado que quiero agregar una estimación de horas a una tarea sin estimación
	Cuando las horas trabajadas en la tarea es superior a las horas estimadas
	Entonces el sistema deberá indicar que no fue posible agregar la estimación
	porque las horas trabajadas hasta el momento es superior a la estimación

	- CA 4: Modificar estimación de horas de tarea con estimación
	Dado que quiero modificar la estimación de horas de una tarea que ya tiene
	estimación
	Cuando modifico la estimación de horas
	Entonces el sistema deberá modificar la estimación de horas de la tarea

	- CA 5: Fallo al modificar la estimación de horas de una tarea sin estimación
	Dado que quiero modificar la estimación de horas de una tarea que sin
	estimación
	Cuando intento modificar la estimación de horas
	Entonces el sistema deberá indicar que no es posible modificar la estimación de
	una tarea que no tiene una estimación

	- CA 6: Fallo al modificar la estimación de horas por valor inválido
	Dado que quiero modificar la estimación de horas de una tarea que ya tiene
	estimación
	Cuando las horas trabajadas en la tarea es superior a las horas estimadas
	Entonces el sistema deberá indicar que no es posible modificar la estimación
	porque las horas trabajadas hasta el momento es superior a la estimación

	- CA 7:  Eliminar estimación de horas
	Dado que quiero eliminar la estimación de horas de una tarea que tiene una
	estimación
	Cuando elimino la estimación de horas
	Entonces el sistema deberá eliminar la estimación de horas de la tarea
	"""
