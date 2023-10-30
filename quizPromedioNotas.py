#Quiz ciclo for en python
#Usando for y una lista con sus notas y los promedios, calcule, su nota definitiva a la fecha

notas = [15,15,15,49,0,15]
porcentajes = [5,10,20,6,3,3]
promedio=0

#El for almacena en n los valores de la lista notas y en p almacena los porcentajes
#La función zip() recorre ambas listas simultaneamente y la variable promedio almacena el total del promedio

for n , p in zip(notas,porcentajes):
    promedio+=n*(p/100)
    
#Imprimimos el valor del promedio divido en 100
print("El promedio de notas del estudiante Nicolas Rojas Castro es = " +str(promedio))