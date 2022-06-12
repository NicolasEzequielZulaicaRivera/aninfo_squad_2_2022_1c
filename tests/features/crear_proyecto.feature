Feature: Crear proyecto
	"""
	Como empleado, quiero crear un proyecto, para así poder dar inicio al proyecto

	CA 1: Solicitud de datos durante la creación

	- Dado que quiero crear un proyecto, cuando selecciono la opción "crear un
	nuevo proyecto", entonces el sistema me solicitará el ingreso de las fechas de
	inicio y fin del proyecto, y las horas totales estimadas para completar el
	proyecto

	CA 2: Creación exitosa

	- Dado que ingresé los datos del proyecto, cuando selecciono la opción "crear
	proyecto", entonces se deberá crear el proyecto con los datos correspondientes

	CA 3: Creación fallida

	- Dado que ingresé los datos del proyecto, cuando el proyecto no se pueda crear
	exitosamente, el sistema deberá informar "no se ha podido crear el proyecto" y
	deberá permitir crearlo nuevamente
	"""
	Scenario: Creacion exitosa
		Given ingrese los datos del proyecto
		When selecciono la opcion "crear proyecto"
		Then se debera crear el proyecto con los datos correspondientes
