Feature: Crear proyecto
	"""
	Como empleado, quiero crear un proyecto, para poder dar inicio al proyecto

	- CA 1: Solicitud de datos durante la creación
	Dado que quiero crear un proyecto
	Cuando selecciono la opción "nuevo proyecto"
	Entonces el sistema me solicitará el ingreso del nombre del proyecto,
	descripción, fecha de inicio, fecha de finalización y horas totales estimadas
	para completar el proyecto

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
	"""
	Scenario: Creacion exitosa
		Given ingrese los datos del proyecto
		When selecciono la opcion "crear proyecto"
		Then se debera crear el proyecto con los datos correspondientes
