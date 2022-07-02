Feature: editar tarea
	"""
	Como empleado, quiero editar los atributos una tarea, para actualizar la
	información de la tarea

	- [x] CA 1: Solicitud de datos de edición de tarea
	Dado que quiero editar una tarea,
	Cuando selecciono la opción "editar tarea"
	Entonces el sistema permitirá editar el nombre de la tarea, descripción, fecha
	de inicio y fecha de finalización

	- [x] CA 2: Edición de tarea exitosa
	Dado que ingresé los datos que deseo editar,
	Cuando selecciono la opción "confirmar edición",
	Entonces los cambios en la tarea se verán reflejados en el sistema

	- CA 3: Fallo al editar una tarea por fechas inválidas
	Dado que quiero editar una tarea,
	Cuando selecciono una fecha de finalización anterior a la fecha de inicio,
	Encontes el sistema deberá indicar que la modificación no puede realizarse
	porque los datos son inválidos

	- CA 4: Fallo al editar una tarea por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para editar una tarea,
	Cuando selecciono la opción "editar tarea",
	Entonces el sistema deberá indicar que no tengo los permisos necesarios para
	realizar dicha acción (No MVP)

	"""

	Scenario: Edicion del nombre de la tarea
		Given una tarea
		When cambio el nombre de la tarea a Nombre actualizado
		Then el nombre de la tarea cambió a Nombre actualizado

	Scenario: Edicion de la descripcion de la tarea
		Given una tarea
		When cambio la descripcion de la tarea a Descripcion actualizada
		Then la descripcion de la tarea cambió a Descripcion actualizada

	Scenario: Edicion de la fecha de inicio de la tarea
		Given una tarea
		When cambio la fecha de inicio de la tarea a 10/10/2020
		Then la fecha de inicio de la tarea cambió a 10/10/2020

	Scenario: Edicion de la fecha de finalizacion de la tarea
		Given una tarea
		When cambio la fecha de finalizacion de la tarea a 10/10/2022
		Then la fecha de finalizacion de la tarea cambió a 10/10/2022

	Scenario: Fallo al editar una tarea por fechas inválidas
		Given una tarea
		When cambio la fecha de finalizacion de la tarea a 10/10/2010
		Then el sistema deberá indicar que la modificación de la tarea puede realizarse porque los datos son inválidos