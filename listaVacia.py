# Importamos la libreria random
import random

# Creamos una lista vacia
lista = []

# Imprimimos el valor que se encuentra en la posicion 3 de la lista
print("Valor en la posición 3 de la lista:", lista[3])

# Creamos un ciclo for para que se repita 10 veces
for i in range(10):
    # Agregamos a la lista un valor numerico aleatorio entre 1 y 100
    numeroAleatorio = random.randint(1, 100)  # Generamos un número aleatorio entre 1 y 100
    lista.append(numeroAleatorio)  # Agregamos el número aleatorio a la lista

# Imprimimos la lista sin el valor que se encuentra en la posicion 3 y diciendo que posición ocupa cada numero
for i in range(len(lista)): # Creamos un ciclo for para que se repita la longitud que tiene la lista
    if i != 3:  # Excluimos la posición 3 de la lista para que no se imprima
        posicion_actual = i  # Guardamos el valor actual de 'i' como la posición actual en la lista
        valorActual = lista[i]  # Obtenemos el valor actual en la lista
        print("Posicion", posicion_actual, ":", valorActual)  # Imprimimos la posición y el valor en esa posición
