Feature: crear tarea
	"""
	Como empleado, quiero crear una tarea, para poder dividir el trabajo y mejorar
	la organización de un proyecto

	- CA 1: Solicitud de datos de creación de tarea en proyecto
	Dado que quiero crear una tarea en un proyecto
	Cuando selecciono la opción "nueva tarea"
	Entonces el sistema me solicitará ingresar el nombre de la tarea, descripción y
	fecha de finalización

	- CA 2: Solicitud de datos de creación de tarea en iteración (no MVP)
	Dado que quiero crear una tarea en una iteración
	Cuando selecciono la opción "nueva tarea de proyecto"
	Entonces el sistema me solicitará ingresar el nombre de la tarea, descripción,
	fecha de finalización y tiempo estimado para realizarla

	- CA 3: Creación exitosa de tarea en proyecto
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada al proyecto

	- CA 4: Creación exitosa de tarea en iteración (No MVP)
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada a la iteración

	- CA 5: Atributos generados durante la creación de la tarea en un proyecto
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada al proyecto con un identificador
	único, y la fecha de creación igual a la fecha en la que se creó la tarea

	- CA 6: Atributos generados durante la creación de la tarea en una iteración
	(no MVP)
	Dado que ingresé los datos de la tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces se deberá crear la tarea asociada a la iteración con un identificador
	único, y la fecha de creación igual a la fecha en la que se creó la tarea

	- CA 7: Creación fallida de tarea en proyecto
	Dado que ingresé los datos de la tarea del proyecto,
	Cuando la tarea no pueda crearse exitosamente,
	Entonces el sistema deberá informar que no se pudo crear la tarea, y deberá
	permitir crearla nuevamente

	 - CA 8: Creación fallida de tarea en iteración (No MVP)
	Dado que ingresé los datos de la tarea de la iteración,
	Cuando la tarea no pueda crearse exitosamente,
	Entonces el sistema deberá informar que no se pudo crear la tarea, y deberá
	permitir crearla nuevamente

	- CA 9: Fallo en la creación por permisos inválidos (No MVP)
	Dado que no tengo los permisos necesarios para crear una tarea,
	Cuando selecciono la opción "crear tarea",
	Entonces el sistema deberá indicar que no tengo permisos para realizar dicha
	acción
	"""

	Background:
		Given un proyecto creado

	Scenario: Solicitud de datos de creación de tarea en proyecto
		Given quiero crear una tarea en un proyecto con datos vacios
		When selecciono la opcion "nueva tarea"
		Then el sistema me solicitará ingresar el nombre de la tarea, descripción y fecha de finalización

	Scenario: Crear tarea en proyecto
		Given quiero crear una tarea en un proyecto
		And el nombre de la tarea es Tarea 1
		And la descripcion de la tarea es Tarea de prueba
		And la fecha de inicio de la tarea es 01/01/2020
		And la fecha de finalizacion de la tarea es 01/01/2020
		When selecciono la opcion "nueva tarea"
		Then se debera crear la tarea con los datos ingresados

	Scenario: Creacion fallida de tarea en proyecto
		Given quiero crear una tarea en un proyecto
		And la tarea no puede crearse exitosamente
		When selecciono la opcion "nueva tarea"
		Then el sistema debera informar que no se pudo crear la tarea, y debera permitir crearla nuevamente

	Scenario: Fallo en la creacion por fecha de incio posterior a la fecha de finalizacion
		Given quiero crear una tarea en un proyecto
		And la fecha de inicio de la tarea es 01/01/2020
		And la fecha de finalizacion de la tarea es 01/01/2019
		When selecciono la opcion "nueva tarea"
		Then el sistema debera informar que no se pudo crear la tarea, y debera permitir crearla nuevamente

	Scenario: Fallo en la creacion por fecha de inicio posterior a la fecha de finalizacion del proyecto
		Given quiero crear una tarea en un proyecto
		And la fecha de inicio de la tarea es 01/01/2025
		And la fecha de finalizacion de la tarea es 01/05/2025
		When selecciono la opcion "nueva tarea"
		Then el sistema debera informar que no se pudo crear la tarea, y debera permitir crearla nuevamente