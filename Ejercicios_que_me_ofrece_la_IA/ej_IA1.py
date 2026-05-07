'''
Problema: Sistema de Clasificación y Logística de Exportación de Café
1. Captura y Validación de Datos (Entrada):
Solicitar al usuario el porcentaje de humedad del lote de café.
Validar que el valor esté entre 7% y 15%. Si el valor es menor a 7 o mayor a 15, mostrar "Error: Fuera de rango" 
y solicitarlo nuevamente.

Solicitar el tipo de grano:
1 para Arábica.
2 para Robusta.
Validar que solo se ingresen estas dos opciones.

Solicitar el destino del envío:
1 para Europa.
2 para Asia.
Validar que solo se ingresen estas dos opciones.

2. Clasificación de Empaque (Lógica de Humedad):
10% o menos: Clasificar como "Saco de Yute".
Entre 10% y 12%: Clasificar como "Bolsa Vacuum".
Más de 12% (hasta 15%): Clasificar como "Contenedor Refrigerado".

3. Asignación de Etiquetas y Costos (Lógica de Negocio):
Si el grano es Arábica: Asignar etiqueta "Premium".
Si el grano es Robusta: Asignar etiqueta "Estándar".

Costo de envío:
Si el destino es Europa, el costo es de 500 USD.
Si el destino es Asia, el costo es de 800 USD.

4. Resultado (Salida):
Imprimir un resumen final que combine: el tipo de empaque, la etiqueta del grano, el destino elegido y el costo total del envío.
'''

import random as rnd
import time
hume = rnd.randint(6,15)
while 6 >= hume or hume > 15:
    print("Fuera de rango")
    hume = rnd.randint(6,15)
    time.sleep(1)
else:
    print(f"La humedad del grano es de: {hume}")
if hume <= 10:
    cafe = "Saco de Yute"
elif hume <= 10 or hume <= 12:
    cafe = "Bolsa Vacuum"
else:
    cafe = "Contenedor Refrigerado"

gran = int(input("¿Que tipo de grano quiere? 1.- Arábica, 2.- Robusta: "))
while gran != 1 and gran != 2:
    print("Fuera de rango")
    gran = int(input("¿Que tipo de grano quiere? 1.- Arábica, 2.- Robusta: "))
if gran == 1:
    sticker = "Premium"
else:
    sticker = "Estándar"
print(f"El tipo de grano que escogió fue: {sticker}")


dest = int(input("¿A que destino desea enviar el grano de café? 1.- Europa 2.- Asia: "))
while dest != 1 and dest != 2:
    print("Error, Seleccione un destino 1.- Europa 2.- Asia")
    dest = int(input("¿A que destino desea enviar el grano de café? 1.- Europa 2.- Asia: "))

if dest == 1:
    destino = "Europa"
    costo = 500
else:
    destino = "Asia"
    costo = 800

print(f"{cafe} {sticker} {destino} {costo}")