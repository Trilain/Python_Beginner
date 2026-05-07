'''
Ejercicio con abs

1.- Generar una temperatura aleatoria entre 30 y 40 grados
2.- Calcular la diferencia absoluta entre la temperatura generada y la ideal (35)
3.- Si esa diferencia es mayor a 2, imprimir "ALERTA: Temperatura fuera de rango".
4.- Si no, imprimir "Temperatura estable"
'''

import random as rnd

ideal = 35
temp = rnd.randint(30,40)

t_gen = temp

t_calc = abs(t_gen - ideal)

if t_calc > 2:
    print("ALERTA: Temperatura fuera de rango")
else:
    print("Temperatura estable")