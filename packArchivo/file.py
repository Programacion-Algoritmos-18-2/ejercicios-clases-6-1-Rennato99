class File:

	# Constructor
	def __init__(self, fileName, mode="r"):
		self.openFile(fileName, mode)

	# Metodo para abrir el archivo
	def openFile(self, fileName, mode):
		self.file = open(fileName, mode)

	# Metodo que retorna una lista cuyos elementos son cada line
	def getLines(self):
		return self.file.readlines()

	# Metodo para agregar informacion
	def pushData(self, data):
		if(self.mode == "r"): # Si el modo es r no dejara escribir
			print("Modo Error. Para poder agregar informacion a este archivo debe abrirlo en modo 'w' o 'a'")
			return
		# Si es 'a' o 'w' se puede escribir
		self.file.write("%s\n" % (file))

	# Metodo para cerrar el archivo
	def close(self):
		self.file.close()

	# Metodo que retorna una lista Ordenda con los datos del archivo
	def toList(self):
		myList = self.getLines()

		# Creamos otra lista donde agregaremos todos los datos
		sortedList = []
		# Recorremoso la lista
		for line in myList:
			line = line.replace("\n", "")# Removemos el salto de linea del final ('\n')
			line = line.split(",") # Dividimos cada linea por ','

			# Recorremos cada linea
			for element in line:
				# Transformamos a enteros
				numero = int(element)
				# Los agregamos a la nueva lista
				sortedList.append(numero)
		# Ordenamos la lista
		sortedList.sort()

		return sortedList
