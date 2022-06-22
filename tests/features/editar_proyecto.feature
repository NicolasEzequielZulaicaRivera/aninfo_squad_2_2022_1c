Feature: editar proyecto
	"""
	Como empleado, quiero editar los atributos un proyecto, para actualizar la
	información del proyecto

	- CA 1: Solicitud de datos de edición de proyecto
	Dado que quiero editar un proyecto
	Cuando selecciono la opción "editar proyecto"
	Entonces el sistema permitirá editar el nombre del proyecto, descripción, fecha
	de inicio y fecha de finalización

	- CA 2: Edición de proyecto exitosa
	Dado que ingresé los datos que deseo editar,
	Cuando selecciono la opción "confirmar edición",
	Entonces los cambios en el proyecto se verán reflejados en el sistema

	- CA 3: Fallo al editar un proyecto por fechas inválidas
	Dado que quiero editar un proyecto,
	Cuando selecciono una fecha de finalización anterior a la fecha de inicio,
	Encontes el sistema deberá indicar que la modificación no puede realizarse
	porque los datos son inválidos

	- CA 4: Fallo al editar un proyecto por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para editar un proyecto,
	Cuando selecciono la opción "editar proyecto",
	Entonces el sistema deberá indicar que no tengo los permisos necesarios para
	realizar dicha acción (No MVP)

	"""

	Scenario: Edicion del nombre del proyecto
		Given un proyecto creado
		When cambio el nombre del proyecto a Nombre actualizado
		Then el nombre del proyecto cambió a Nombre actualizado

	Scenario: Edicion de la descripción del proyecto
		Given un proyecto creado
		When cambio la descripción del proyecto a Descripción actualizada
		Then la descripción del proyecto cambió a Descripción actualizada

	Scenario: Edicion de la fecha de inicio del proyecto
		Given un proyecto creado
		When cambio la fecha de inicio del proyecto a 05/05/2022
		Then la fecha de inicio del proyecto cambió a 05/05/2022

	Scenario: Edicion de la fecha de finalización del proyecto
		Given un proyecto creado
		When cambio la fecha de finalización del proyecto a 05/05/2023
		Then la fecha de finalización del proyecto cambió a 05/05/2023

	Scenario: Fallo al editar un proyecto por fechas inválidas
		Given un proyecto creado
		When cambio la fecha de finalización del proyecto a 05/05/2000
		Then el sistema deberá indicar que la modificación no puede realizarse porque los datos son inválidos
		And la fecha de finalizacion es 22/06/2022