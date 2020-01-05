#Python POO

#Ejercicio: programa que conste de una clase llamada alumno que tenga como atributos el 
# nombre y la nota del alumno.
#Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
# con el resuiltado de la nota y si ha aprobado o no

class Alumno:
    #inicializamos los atributos de alumno
    #def __init__(self, nombre, nota):
    #    self.nombre = nombre
    #    self.nota = nota

    def __init__(self):
        self.nombre = input('Nombre del alumno: ')
        self.nota = input('nota del alumno: ')

    def imprimir(self):
        print('Alumno: ', self.nombre)
        print('Nota: ', self.nota)
        print('')
    
    def resultado(self):
        if int(self.nota) <5:
            print('El alumno:  ', self.nombre, ' ha reprobado')
        else:
            print('El alumno:  ', self.nombre, ' ha aprobado con la nota de: ', self.nota)
        
alumno1 = Alumno()
alumno1.imprimir()
alumno1.resultado()
