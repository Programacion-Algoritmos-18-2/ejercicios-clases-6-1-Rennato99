class Operations:

	# Constructor
	def __init__(self, myList=[]):
		self.myList = myList

	# Metodo que hace una busqueda binaria (Recursividad)
	def binarySearch(self, target, higher, lower=0):
		middle = int((lower + higher + 1) / 2)

		if(target == self.myList[middle]): # Si elemento esta en el medio
			position = middle
			return position # Retorna la posicion del elemento

		elif(target < self.myList[middle] and lower < higher):
			higher = middle - 1 # Eliminamos la mitad superior

			# LLamamos de nuevo al metodo la mitad superior no sera tomada en cuenta
			return self.binarySearch(target, higher, lower) 

		elif(target > self.myList[middle] and lower < higher):
			lower = middle + 1 # Eliminamos la mitat inferior

			# LLamamos de nuevo al metodo la mitad inferior no sera tomada en cuenta
			return self.binarySearch(target, higher, lower)

		else:
			# "Error. Elemento no encontrado!"
			return -1

		