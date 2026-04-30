# Menú con funciones
import random as rnd
import time as tm
def juego():
    turnos = rnd.randint(1, 2)
    golpe = 0
    p1=(input("Ingrese su nombre de jugador: "))
    hp_p1=100
    p2=(input("Ingrese el segundo nombre de jugador: "))
    hp_p2=100
    while hp_p1 > 0 and hp_p2 > 0:
        golpe = rnd.randint(7,15)
        if turnos == 1:
            hp_p2 = hp_p2 - golpe
            if hp_p2 < 0:
                hp_p2 = 0
            print(f"{p1} Golpea a {p2} y hace {golpe} de daño!!")
            turnos = 2
        else:
            if turnos == 2:
                hp_p1 = hp_p1 - golpe
                if hp_p1 < 0:
                    hp_p1 = 0
                print(f"{p1} Golpea a {p2} y hace {golpe} de daño!!")
                turnos = 1
        print(f"La pelea sigue!! HP p1: {hp_p1} vs HP p2: {hp_p2}")
    if p1>p2:
        print(f"Ha ganado el jugado {p1} con {hp_p1} HP!!")
    else:
        print(f"Ha ganado el jugado {p2} con {hp_p2} HP!!")


def nombreUsuario():
    nombre=(input("Ingrese su nombre de usuario: "))
    if len(nombre) <= 4 and len(nombre) <=10:
        print("Usuario creado exitosamente.")
    else:
        print("Usuario fuera de rango preestablecido.")

def suma():
    num=int(input("Ingrese un número"))
    suma=0
    for i in range(1, num+1):
        suma=suma+i
        print("El total de la sumatoria es: ", suma)

op=0
while op != 4:
    print("1.- Juego Por Turnos")
    print("2.- Creación Nombre Usuario")
    print("3.- Sumatoria")
    print("4.- Salir")
    print("Seleccione una opción: ")
    op=int(input())
    match op:
        case 1:
            juego()
        case 2:
            nombreUsuario()
        case 3:
            suma()
        case 4:
            print("Saliendo...")
        case _:
            print("Opción Inválida")