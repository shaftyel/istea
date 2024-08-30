import json
import os
import unidecode

class Libro:
	
	def __init__ (self):		
		self.limpiar()
		name=input("Por favor ingrese su nombre: ")
		while True:
			self.limpiar()
			print(f"Bienvenido al recomendador de libros {name}")
			print(f"Que desea hacer:\n1 - Agregar\n2 - Buscar\n3 - Recomendación\n4 - Salir")
			option=input("Ingrese la opción deseada: ")
		
			if option.isdigit():
				option=int(option)
				if option>0 and option <5:
					if option==1:
						self.agregar()
					elif option==2:
						self.buscar()
					elif option==3:
						self.recomendar()
					else:
						break
				else:
					self.limpiar()
					print("Ingresar una opción válida")
					self.pausa()
			else:
				self.limpiar()
				print("Ingresar número de opción correcta")
				self.pausa()

		self.titulo=""
		self.autor=""
		self.genero=""
		self.puntuacion=""	
		
	def limpiar(self):
		os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
		
	def pausa(self):
		input("\tPresione enter para continuar")  
		
	def agregar(self):
		self.limpiar()
		while True:
			self.limpiar()
			self.titulo=input("Ingrese el título del libro o la palabra 'salir' para volver al menú anterior: ")
			if self.titulo.upper()=="SALIR":
				break
			self.autor=input("Ingrese el autor del libro: ")
			self.genero=input("Ingrese el género del libro: ")
			self.puntuacion=input("Ingrese la puntuación del libro:" )
			if self.puntuacion.replace('.','').replace(',','').isdigit():
				self.limpiar()
				librito={
					"Titulo":self.titulo,
					"Autor":self.autor,
					"Genero":self.genero,
					"Puntuación":self.puntuacion
				}
				if os.path.exists("libreria.json"):
					with open("libreria.json", "r", encoding='utf8') as j:
						libros = json.load(j)
				else:
					libros = []
				libros.append(librito)
				with open("libreria.json", "w", encoding='utf8') as j:
					json.dump(libros, j, indent=4, ensure_ascii=False)
				print(f"Se ingresó correctamente el libro:\nTitulo: {self.titulo}\nAutor: {self.autor}\nGenero: {self.genero}\nPuntuacion: {self.puntuacion}\n")
				self.pausa()
			else:
				self.limpiar()
				print("Se ingresó una puntuación incorrecta.")
				self.pausa()			
		return	
		
	def buscar(self):
		while True:
			self.limpiar()
			self.genero=input("Ingrese el género de libros a recomendar o la palabra 'salir' para volver al menú anterior: ")
			if self.genero.upper()=="SALIR":
				break
			self.limpiar()
			genero_normalizado=unidecode.unidecode(self.genero.lower())
			print(f"El género buscado es: {self.genero}")
			with open("libreria.json", "r", encoding='utf8') as j:
				libros = json.load(j)
			resultado =[]
			for dic in libros:
				if any(genero_normalizado in unidecode.unidecode(str(valor).lower()) for valor in dic.values()):
					resultado.append(dic)
			if resultado:
				print("Se encontraron los siguientes resultados: \n")
				for libro in resultado:
					print()
					for clave, valor in libro.items():
						print(f"{clave}: {valor}")
			else:
				print("No se encontraron libros para este género.")
					
			self.pausa()
		return
		
	def recomendar(self):	
		while True:
			self.limpiar()
			self.genero=input("Ingrese el género de libros a buscar o la palabra 'salir' para volver al menú anterior: ")
			if self.genero.upper()=="SALIR":
				break
			self.limpiar()
			genero_normalizado=unidecode.unidecode(self.genero.lower())
			print(f"El género buscado es: {self.genero}")
			with open("libreria.json", "r", encoding='utf8') as j:
				libros = json.load(j)
			resultado =[]
			for dic in libros:
				if any(genero_normalizado in unidecode.unidecode(str(valor).lower()) for valor in dic.values()):
					resultado.append(dic)
			if resultado:
				libro_puntuacion_alta=None
				puntuacion_libro=-1
				for libro in resultado:
					puntuacion = libro.get("puntuación",0)
					if puntuacion > puntuacion_libro:
						puntuacion_libro=puntuacion
						libro_puntuacion_alta = libro
				
				if libro_puntuacion_alta:
					print("Se encontraron los siguientes resultados: \n")
					for clave, valor in libro_puntuacion_alta.items():
						print(f"{clave}: {valor}")
			else:
				print("No se encontraron libros para este género.")	
			self.pausa()
		return
libro1 = Libro()		
# ~ libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
# ~ libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
# ~ libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
# ~ libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
# ~ libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
# ~ libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
# ~ libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
# ~ libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
# ~ libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
# ~ libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)
