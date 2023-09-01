# Importar la librería random, que nos permitirá generar números aleatorios
import random

# Crear una lista vacía donde se almacenarán los valores numéricos
lista = []

# Utilizar un ciclo for para agregar 10 valores numéricos aleatorios a la lista
for i in range(10):
    # Generar un número aleatorio entre 1 y 100 y agregarlo a la lista
    numeroAleatorio = random.randint(1, 100)
    lista.append(numeroAleatorio)
    
# Imprimir la lista completa con los 10 valores generados aleatoriamente
print("Lista completa:", lista)

# Imprimir el valor en la posición 3 de la lista (cuarta posición en términos humanos)
valorPosicionTres = lista[3]
print("Valor en la posición 3:", valorPosicionTres)

# Eliminar el valor en la posición 3 de la lista
del lista[3]

# Imprimir la lista nuevamente, esta vez con solo 9 valores después de haber eliminado uno
print("Lista después de eliminar el valor en la posición 3:", lista)
