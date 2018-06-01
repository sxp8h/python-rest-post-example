#!/usr/bin/python2

# Imports de distintas librerias
import random	# Incluida en python
import logging	# Incluida en python
import json 	# Incluida en python
import requests	# Descargar con PIP
import time		# Incluida con python

# Linea donde cambiamos los colores del log (no funciona en windows)
logging.addLevelName(logging.WARNING, "\033[1;93m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
logging.addLevelName(logging.ERROR, "\033[1;91m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.DEBUG, "\033[1;94m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
logging.addLevelName(logging.INFO, "\033[1;92m%s\033[1;0m" % logging.getLevelName(logging.INFO))

# Un pequeño parser para que no devuelva los numeros y nos lo devuelva en forma de texto
def status_code_parser(status):
	if status == 200:
		return "OK"
		
	if status == 201:
		return "Created"
	
	if status == 400:
		return "Bad Request"
		
	if status == 401:
		return "Unauthorized"
	
	if status == 403:
		return "Forbidden"
		
	if status == 404:
		return "Url not Found"

	if status == 409:
		return "Conflict"
		
	if status == 500:
		return "Internal Server Error"		

def main():
	# Hacemos un pequeño log para decir que empezamos a mandar alarmas
	logging.warning("[!] Sending Alerts [!]")
	
	# Inicializamos la variable URL a donde van a apuntar nuestras peticiones
	url = '<url>'
	
	patient_id = <patient_id INT>
	
	# Almacenamos nuestro token de autorización
	token = "Bearer <token>"	
	
	# Creamos los headers de la peticion HTML
	headers = {"Content-Type": "application/json", "Authorization": token}
	
	# Creamos los distintos tipos de alarmas que podemos recibir en funcion de su gravedad
	high = '{"subject": {"reference": Patient/id:"' + patient_id + '"},"payload": [{ "contentString":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus varius sodales est, id facilisis odio cursus sit amet. Maecenas sollicitudin congue arcu, in semper tellus mollis elementum. In in quam posuere, vestibulum justo sit amet, commodo risus. Nullam efficitur velit mi, in molestie magna scelerisque sit amet. Nam gravida convallis efficitur. Proin sed molestie urna. Nulla cursus, dolor nec rutrum sodales, enim elit mattis orci, quis rutrum sem ante vel massa. Maecenas condimentum sapien vitae lectus ultricies dignissim. demasiado Praesent vitae lacinia nulla. Ut sem lorem, condimentum ac fermentum ac, ullamcorper sed sem. Integer id urna vitae ligula dapibus cursus quis." }]}'
	medium = '{"subject": {"reference": "Patient/id:"' + patient_id + '"},"payload": [{ "contentString":"moderadamente Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eget nisl at lacus volutpat mollis nec id diam. Donec luctus arcu eu mauris faucibus suscipit. Donec porttitor congue orci in varius. Ut eget auctor lacus, at scelerisque lectus. Fusce vestibulum ultrices tempor. Phasellus aliquam felis nec elementum varius. Duis viverra." }]}	'
	low = '{"subject":{"reference": "Patient/id:"' + patient_id + '"},"payload": [{ "contentString":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eleifend scelerisque eros, id volutpat tortor." }]}'
	
	# Hacemos un bucle for del 1 al 50 para que nos haga 50 peticiones 
	for x in range(1, 51):
		# Creamos un numero aleatorio para que cada peticion sea distinta
		number = random.randint(1, 3)
		
		# Inicializacion de variables que se usan mas abajo y asi siguen en el scope (en la mirilla)
		# 
		# En python si las variables no estan a la misma altura no son alcanzables, que quiere decir que si type_alarm 
		# la inicializo abajo, no podria leerla desde la altura de number
		#
		#
		type_alarm = ""
		post = ""
		
		# Que decida que hace con cada petición
		if number == 1:
			# Generamos la peticion POST, con la url, la cabecera y el body del mensaje
			post = requests.post(url, headers = headers, data = high)
			type_alarm = "HIGH"
			
		if number == 2:
			# Generamos la peticion POST, con la url, la cabecera y el body del mensaje
			post = requests.post(url, headers = headers, data = medium)
			type_alarm = "MEDIUM"
			
		if number == 3:
			# Generamos la peticion POST, con la url, la cabecera y el body del mensaje
			post = requests.post(url, headers = headers, data = low)
			type_alarm = "LOW"
			
			
		# Logeamos que se ha hecho una peticion, el numero de la misma, el tipo de alarma generada y el status
		logging.warning("Petition{}, type_alarm->{}, status:{}".format(x, type_alarm, status_code_parser(post.status_code)))
		# Decansamos 5 segundos
		time.sleep(5)

# Aqui inicializamos el programa, porque es la linea de mas alto nivel junto a los imports
main()
	


