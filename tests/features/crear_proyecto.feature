Feature: crear proyecto
	"""
	Como empleado, quiero crear un proyecto, para poder dar inicio al proyecto

	- CA 1: Solicitud de datos durante la creación
	Dado que quiero crear un proyecto
	Cuando selecciono la opción "nuevo proyecto"
	Entonces el sistema me solicitará el ingreso del nombre del proyecto,
	descripción, fecha de inicio y fecha de finalización

	- CA 2: Creación exitosa
	Dado que ingresé los datos del proyecto,
	Cuando selecciono la opción "crear proyecto",
	Entonces se deberá crear el proyecto con los datos ingresados

	- CA 3: Creación fallida
	Dado que ingresé los datos del proyecto,
	Cuando el proyecto no se pueda crear exitosamente,
	Entonces el sistema deberá informar "no se ha podido crear el proyecto" y
	deberá permitir crearlo nuevamente

	- CA 4: Fallo de creación por fecha de inicio inválida
	Dado que quiero crear un proyecto,
	Cuando intento crear un proyecto con una fecha de inicio anterior al día de la
	fecha,
	Entonces el sistema no deberá crear el proyecto e indicará que no es posible
	crear un proyecto con fecha de inicio anterior a la de hoy

	- CA 5: Fallo de creación por fecha de finalización inválida
	Dado que quiero crear un proyecto,
	Cuando intento crear un proyecto con una fecha de finalización anterior al día
	de la fecha,
	Entonces el sistema no deberá crear el proyecto e indicará que no es posible
	crear un proyecto con fecha de finalización anterior a la de hoy

	- CA 6: Fallo de cración por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para crear un proyecto,
	Cuando selecciono la opción "crear proyecto",
	Entonces el sistema deberá indicar que no tengo permisos para realizar dicha
	acción

	"""

	Scenario: Creacion exitosa de proyecto
		Given quiero crear un proyecto llamado Proyecto 1
		And la descripcion es Proyecto de prueba
		And la fecha de inicio es 01/01/2020
		And la fecha de finalizacion es 01/05/2021
		When selecciono la opción "nuevo proyecto"
		Then se deberá crear el proyecto con los datos ingresados

	Scenario: Creacion fallida de proyecto por fechas de inicio y finalizacion inválidas
		Given quiero crear un proyecto
		And la fecha de inicio es 01/05/2020
		And la fecha de finalizacion es 01/01/2020
		When selecciono la opción "nuevo proyecto"
		Then el sistema debera indicar que no fue posible crear el proyecto porque los datos son inválidos

	Scenario: Creacion fallida de proyecto por fecha de finalizacion anterior a la actual
		Given quiero crear un proyecto
		And la fecha de finalizacion esta en el pasado
		When selecciono la opción "nuevo proyecto"
		Then el sistema debera indicar que no fue posible crear el proyecto porque los datos son inválidos


