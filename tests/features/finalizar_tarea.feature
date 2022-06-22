Feature: finalizar tarea
	"""
	Como empleado, quiero finalizar una tarea, para marcarla como finalizada

	- CA 1: Finalización de tarea sin finalizar
	Dado que existe una tarea sin finalizar
	Cuando selecciono la opción "finalizar tarea"
	Entonces el sistema deberá modificar el estado de la tarea a "finalizada"

	- CA 2: Fallo al finalizar una tarea ya finalizada
	Dado que existe una tarea finalizada
	Cuando selecciono la opción "finalizar tarea"
	Entonces el sistema deberá indicar que no es posible finalizar una tarea ya
	finalizada
	"""
