Feature: asignar responsable de tarea
	"""
	Como empleado, quiero asignar un responsable a una tarea, para indicar que es
	responsable de que se realice la tarea

	- CA 1: Solicitud de datos del responsable a asignar
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
	realizar dicha acción (No MVP)

	"""
