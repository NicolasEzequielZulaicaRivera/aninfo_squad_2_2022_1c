Feature: visualizar tarea
	"""
	Como empleado, quiero visualizar una tarea, para saber cuáles son sus atributos

	- CA 1: Visualización de atributos básicos de tarea
	Dado que quiero visualizar una tarea,
	Cuando selecciono la tarea,
	Entonces el sistema deberá mostrar el identificador de la tarea, nombre,
	descripción, fecha de inicio, fecha de fin, estado, horas trabajadas,
	colaboradores y (si tiene) horas estimadas y responsable

	- CA 2: Búsqueda de tarea por nombre
	Dado que quiero visualizar una tarea,
	Cuando busco la tarea por nombre,
	Entonces el sistema me deberá mostrar la tarea cuyo nombre coincide con el
	nombre ingresado
	"""

	Scenario: Visualizacion de atributos basicos de tarea
		Given una tarea
		When selecciono la tarea
		Then el sistema deberá mostrar la informacion basica de la tarea