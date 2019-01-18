# Importamos lo necesario
from packArchivo.file import * 
from packModelado.modelo import * 


# Abrimos el archvio
data = File("data/datos.txt", "r")

# Obtenemos una lista con todos los numeros ya ordenada
myList = data.toList()

print("Lista creada con éxito: \n")  # Imprimos la lista
print(myList)

# Creamos un objeto operaciones
operar = Operations(myList)

_continue = True
while (_continue):

	target = int(input("\nIngrese el elemento a buscar: "))
	top = len(myList)-1 # Calculamos el indice del ultimo elemento
	# Llamamos al metodo de busqueda binaria
	position = operar.binarySearch(target=target, higher=top, lower=0)

	if(position != -1): # Si encontro el elemento:
		print("Elemento %d encontrado en la posicion: %d"%(target, position))
	else: # Si no
		print("Elemento no encontrado!")


	# Preguntamos si desea continuar
	answer = input("\nDesea buscar otro elemento? 1 = Si | 2 = No: ")
	if(answer == '2'):
		_continue = False
	