Feature: Crear tarea
	"""
	Como empleado, quiero crear una tarea, para poder dividir el trabajo y mejorar
	la organización de un proyecto

	- CA 1: Solicitud de datos de creación de tarea en proyecto
	Dado que quiero crear una tarea en un proyecto
	Cuando selecciono la opción "nueva tarea"
	Entonces el sistema me solicitará ingresar el nombre de la tarea, descripción,
	fecha de finalización y tiempo estimado para realizarla

	- CA 2: Solicitud de datos de creación de tarea en iteración
	Dado que quiero crear una tarea en una iteración
	Cuando selecciono la opción "nueva tarea de proyecto"
	Entonces el sistema me solicitará ingresar el nombre de la tarea, descripción,
	fecha de finalización y tiempo estimado para realizarla

	- CA 3: Creación exitosa de tarea en proyecto
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada al proyecto

	- CA 4: Creación exitosa de tarea en iteración
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada a la iteración

	- CA 5: Atributos generados durante la creación de la tarea en un proyecto
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada al proyecto con un identificador
	único, y la fecha de creación igual a la fecha en la que se creó la tarea

	- CA 6: Atributos generados durante la creación de la tarea en una iteración
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada a la iteración con un identificador
	único, y la fecha de creación igual a la fecha en la que se creó la tarea

	- CA 7: Creación fallida de tarea en proyecto
	Dado que ingresé los datos de la tarea del proyecto,
	Cuando la tarea no pueda crearse exitosamente,
	Entonces el sistema deberá informar que no se pudo crear la tarea, y deberá
	permitir crearla nuevamente

	 - CA 8: Creación fallida de tarea en iteración
	Dado que ingresé los datos de la tarea de la iteración,
	Cuando la tarea no pueda crearse exitosamente,
	Entonces el sistema deberá informar que no se pudo crear la tarea, y deberá
	permitir crearla nuevamente
	"""
