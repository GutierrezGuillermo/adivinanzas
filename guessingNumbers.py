import random

def azar(numero):
	a = random.randint(1,9)
	b = numero
	if int(b) == 10:
		return 10
	if int(b) > a:
		return("Te pasaste de largo")
	elif int(b) < a:
		return("Te quedaste corto")
	else:
		return("Acertaste")
	

bandera = True
while bandera:	
	prueba = azar(input("Qué numero salirá? Marca 10 para salir: "))
	if prueba == 10:
		break
	else:
		print(prueba)
