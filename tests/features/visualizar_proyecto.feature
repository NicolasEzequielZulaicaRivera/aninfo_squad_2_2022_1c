Feature: visualizar proyecto
	"""
	Como empleado, quiero visualizar un proyecto, para saber cuáles son sus
	atributos

	- CA 1: Visualización de atributos básicos de proyecto
	Dado que quiero visualizar un proyecto,
	Cuando selecciono el proyecto,
	Entonces el sistema deberá mostrar el identificador del proyecto, nombre,
	descripción, fecha de inicio, fecha de fin, estado, y horas totales (calculadas
	como el total de las horas trabajadas de cada una de las tareas del proyecto)

	- CA 2: Visualización de tareas de un proyecto
	Dado que quiero visualizar las tareas de un proyecto
	Cuando selecciono el proyecto,
	Entonces el sistema deberá mostrar las tareas del proyecto con su información
	básica: identificador de tarea, nombre, fecha de inicio, fecha de fin, horas
	trabajadas y (si tiene) horas estimadas

	- CA 3: Búsqueda de proyecto por nombre
	Dado que quiero visualizar un proyecto,
	Cuando busco el proyecto por nombre,
	Entonces el sistema me deberá mostrar el proyecto cuyo nombre coincide con el
	nombre ingresado
	"""
