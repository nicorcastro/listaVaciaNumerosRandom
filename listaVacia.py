#Crear una lista vacia en la cual se vayan agregando 10 valores numericos de manera aleatoria
#Luego imprimir la lista, excepto el valor que se encuentra en la posición 3 y comentar cada paso

#Importar librerias
import random

#Crear lista vacia
lista = []

#Crear ciclo for para agregar 10 valores numericos de manera aleatoria
for i in range(10):
    lista.append(random.randint(1, 100))
    
#Imprimir lista
print(lista)

#Imprimir valor en la posición 3
print(lista[3])

#Eliminar valor en la posición 3
del lista[3]

#Imprimir lista
print(lista)



