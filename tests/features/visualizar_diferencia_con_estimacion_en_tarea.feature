Feature: visualizar diferencia con estimacion en tarea
	"""
	Como empleado, quiero ver la diferencia entre horas reales y estimadas de una
	tarea, para poder hacer un seguimiento del desarrollo del proyecto

	- CA 1:Visualización de horas estimadas en una tarea finalizada con estimación
	Dado que existe una tarea con estimación y finalizada,
	Cuando la visualizo,
	Entonces el sistema deberá informar la diferencia entre horas trabajadas y
	estimadas

	- CA 2: Visualización de horas estimadas en una tarea finalizada sin estimación
	Dado que existe una tarea sin estimación y finalizada,
	Cuando la visualizo,
	Entonces el sistema deberá informar las horas trabajadas y advertir que no es
	posible visualizar la diferencia con las horas estimadas ya que la tarea no
	tiene una estimación

	- CA 3: Visualización de horas estimadas en una tarea no finalizada con
	estimación
	Dado que existe una tarea con estimación y no finalizada,
	Cuando la visualizo,
	Entonces el sistema deberá informar la diferencia entre horas trabajadas y
	estimadas

	- CA 4: Visualización de horas estimadas en una tarea no finalizada sin
	estimación
	Dado que existe una tarea sin estimación y no finalizada,
	Cuando la visualizo,
	Entonces el sistema deberá informar las horas trabajadas y advertir que no es
	posible visualizar la diferencia con las horas estimadas ya que la tarea no
	tiene una estimación
	"""
