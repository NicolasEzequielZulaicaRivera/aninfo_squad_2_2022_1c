Feature: Crear tarea
	"""
	Como empleado, quiero agregar tareas a una fase, para dividir el trabajo dentro
	de una misma fase

	CA 1: Solicitud de datos de tarea

	- Dado que quiero crear una tarea en una iteración, cuando selecciono la opción
	"agregar nueva tarea", entonces el sistema me solicitará ingresar el tiempo
	estimado para realizar la tarea

	CA 2: Creación de tarea exitosa

	- Dado que ingresé los datos de la tarea, cuando selecciono la opción "crear
	tarea", entonces se deberá crear la tarea asociada a la iteración
	correspondiente

	CA 3: Creación de tarea fallida

	- Dado que ingresé los datos de la tarea, cuando la tarea no pueda crearse
	exitosamente, entonces el sistema deberá informar "no se pudo crear la tarea" y
	deberá permitir crearla nuevamente
	"""
