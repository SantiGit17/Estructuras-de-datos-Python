#ESTRUCTURAS DE BASES DE DATOS
#David Sanchez
#Ficha: 2502640

#Listas
instrumentos_futbol = ['Guayos','Cancha','Uniforme']

""" Para agregar un item en el final de la lista se usa: """
instrumentos_futbol.append('Balon')

""" Para extender la lista agregando todo el item como diferentes items separandolo por letra: """
instrumentos_futbol.extend('FC')

""" Para agregar un item en una posicion especifica: """
instrumentos_futbol.insert(3,'Pantaloneta')

""" Para eliminar el item elegido: """
instrumentos_futbol.remove('Uniforme')

""" Para quitar el ítem en la posición dada de la lista y lo retorna (si no se especifica se selecciona el ultimo item de la lista): """
#instrumentos_futbol.pop()

""" Para eliminar todos los elementos de la lista: """
#instrumentos_futbol.clear()

""" Para retornar el item seleccionado, si no existe lanza un error: """
print(instrumentos_futbol.index('Guayos'),"\n")

""" Para contar el numero de veces que aparece un item: """
instrumentos_futbol.count('Guayos')

""" Para ordenar la lista por ejemplo en orden alfabetico: """
instrumentos_futbol.sort()

""" Para invertir los elementos de la lista: """
instrumentos_futbol.reverse()

""" Para hacer una copia de la lista: """
instrumentos_futbol.copy()

print (instrumentos_futbol,"\n")


#Lista como pila
""" El ultimo elemento ingresado será el primero en salir lo que hace que solo se elimine los items desde el ultimo. """
instrumentos_futbol1 = [1,2]
instrumentos_futbol1.append(3)
instrumentos_futbol1.pop()

print (instrumentos_futbol1,"\n")


#Listas como colas
""" Significa que el primer elemento añadido es el primero en ser retirado, este proceso es lento ya que todos los items teendrian que correrse una posicion. Se puede usar   ya que está echa para añadir y quitar las dos puntas de la lista de forma rapida. """
from collections import deque
from xml.etree.ElementInclude import include
instrumentos_futbol2 = deque(['Color_camisa','Horario'])
instrumentos_futbol2.append	('Arbitro')
instrumentos_futbol2.popleft ()

print (instrumentos_futbol2,"\n")


#Comprension de listas
""" Se usa para crear nuevas listas donde cada elemento se usa para darle resultado a otras operaciones tambi+en sirve para crear una secuencia y poder realizar la condición determinada. """

Com = []
for x in range(10):
    Com.append(x//2)

print(Com,"\n")

""" Cosiste de corchetes que es rodeada de una expresión seguida del for o if y se pueden combinar elementos de dos o mas listas. Y puede contener expresiones complejas anidadas. """
Com_combi = []
for x in [1,2]:
    for y in [2,1]:
        if x != y:
            Com_combi.append((x,y))

print(Com_combi,"\n")


#Listas compresiones anidadas
""" Se pueden incluir diferentes listas """
includ = [1,2,3],[4,5,6],[7,8,9]
matrix = []
for i in range(3):
    matrix.append ([row[i] for row in includ])

print(matrix,"\n")



#Instrucción del
""" Existe la manera de eliminar un item de la lista dando su posición y no su valor; también puede usarse para quitar secciones de una lista o vaciar la lista completa """
eliminar= [2,4,6,8,10]
del eliminar[0]
#Para eliminar el item que esté en la primera posicion
#del eliminar[:]
#Para vaciar el toda la lista
print(eliminar,"\n")

""" También sirve para eliminar variables """
#del eliminar


#TUPLAS Y SECUENCIAS
""" La tupla es otro tipo de seciencia estandar, que consiste de un número de valores separados por comas, las tuplas siempre en salida estan entre parentesis para que se puedan interpretar bien las tuplas anidadas; las tuplas son immutable y normalmente contienen una secuencia heterogénea de elementos que son accedidos al desempaquetar; para crear una tupla vacia se ponen los parentesis vacios y para hacer una de un item se pone una coma despues del valor. 
Desempaquetado de secuencias, y funciona para cualquier secuencia en el lado derecho del igual. """
tup= 'Erick', 0, 'Mateo', 1
print (tup)

tup2=tup, 0,1,0,1
print (tup2,"\n")


#CONJUNTOS
""" Es una colección no ordenada y sin elementos repetidos; incluyen verificación de pertenencia y eliminación de entradas duplicadas, también soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica. Las llaves función set() como para crear un conjuto vacio. """
Player= {'Volante','Delantero','Defensa','Arquero'}

'Volante\n' in Player
'Boxeador' in Player
print (Player,"\n")

Playerwrd = set('Tecnico')
print (Playerwrd,"\n")


#DICCIONARIOS
""" Los diccionarios se indexan con claves, que pueden ser cualquier tipo inmutable, Las tuplas pueden usarse como claves si solamente contienen cadenas, números o tuplas; se crean con las llaves; las funciones son guardar un valor con una clave y extraer ese valor dada la clave. También es posible borrar un par clave:valor con del. Ejecutando list(d) en un diccionario retornará una lista con todas las claves usadas en el diccionario, en el orden de inserción """

Act= {'Entrenar':10,'Estirar':5}
#Para agregar una nueva clave
Act['Descansar']=5
print (Act,"\n")
#Para mostrar solo el valor de la clave
print (Act['Descansar'])
#Mostras las claves con una lista
print(list(Act))

#Para crear el diccionario directo se usa dict
#dict([('Entrenar', 10), ('Estirar', 5), ('Descansar', 5)])

#Cuando son cadenas sencillas se puede realizar directo con un signo igual
#dict(Entrenar=10, Estirar=5, Descansar=5)


#Técnicas de iteración
""" Cuando se realiza una iteración en un diccionario se puede btener al mismo tiempo la clave y su valor usando items()."""
Equipos = {'Real': 'Benzema', 'Barca': 'Pedri'}
for r, b in Equipos.items():
    print(r,b)

""" Una iteración en una secuencia se puede obtener el índice de posición junto a su valor, usando la funcion enumerate(). """
for m, o in enumerate(['manchester', 'olympus']):
    print(m,o)

""" Si iteramos sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con la funciónzip() """
reque= ['name', 'number', 'position']
juga= ['Santi', 'diez', 'volante']
for re, ju in zip(reque, juga):
    print('What is your {0}?  It is {1}.'.format(re, ju))

""" Para iterar una secuencia que vaya en reversa primero especificas en orden y luego usas la funcion   reverse(). """
for ite in reversed(range(1, 30, 3)):
    print (ite)

""" Para iterar y poner en orden alfabetico se usa la funcion sorted(). """
fut = ['balon', 'uniforme', 'cancha', 'jugadores', 'guayos', 'canilleras']
for itera in sorted(fut):
    print (itera)

""" La funcion sorted() se puede usar para eliminar elementos duplicados y se puede combinar con la funcion set() para ordenar. """
futrep = ['balon', 'uniforme', 'balon', 'uniforme', 'guayos', 'balon']
for com in sorted(set(futrep)):
    print (com)


#Mas sobre condiciones
""" while y if pueden pueden contener cualquier operador, no sólo comparaciones.
Las comparaciones pueden combinarse mediante los operadores booleanos and y or que pueden negarse con not donde not tiene mayor prioridad a la hora de ejecutarlo.
Los operadores booleanos and y or son los llamados operadores cortocircuito: sus argumentos se evalúan de izquierda a derecha, y la evaluación se detiene en el momento en que se determina su resultado. """
equip1, equip2, equip3 = '', 'Asciende', 'Desciende'
pasa = equip1 or equip2 or equip3
print (pasa)


#Comparando secuencias y otros tipos
""" Las secuencias pueden compararse con otros objetos del mismo tipo de secuencia. Si todos los ítems de dos secuencias resultan iguales, se considera que las secuencias son iguales.  """
""" [1, 2, 3] < [1, 2, 4]
'EQUIPO' < 'A' < 'Manchester' < 'Futbol' 
(1, 2, 3) == (1.0, 2.0, 3.0) """



""" https://docs.python.org/es/3/tutorial/datastructures.html# """