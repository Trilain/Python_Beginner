import random as rnd
import time
#print(rnd.randint(1,10))

# num=rnd.randint(1,10)

# for i in range(num):
#     print("hola daniel")

# vamos a crear un dado

# dado=rnd.randint(1,6)

# print(f"el dado salió: {dado}")

# p1 = rnd.randint(60,190)
# p2 = rnd.randint(60,190)
# p3 = rnd.randint(60,190)
# print(f"El jugador 1 lanzo la pelota: {p1}m.")
# print(f"El jugador 2 lanzo la pelota: {p2}m.")
# print(f"El jugador 3 lanzo la pelota: {p3}m.")

# if p1>p2 or p1>p3:
#     print("El jugador 1 ganó")
# elif p2>p3:
#     print("El jugador 2 ganó")
# else:
def barra_vida(hp, max_hp=100):
    porcentaje = hp / max_hp
    bloques = int(porcentaje * 20)
    barra = "█" * bloques + "░" * (20 - bloques)
    color = ""
    if porcentaje > 0.5:
        color = "\033[92m"  # verde
    elif porcentaje > 0.25:
        color = "\033[93m"  # amarillo
    else:
        color = rgb(FF0000)  # rojo
    reset = "\033[0m"
    return f"{color}[{barra}]{reset} {hp}/100 HP"

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
        print("La pelea sigue!!")
        print(barra_vida(hp_p1))
        print(barra_vida(hp_p2))
        time.sleep(2)
    if p1>p2:
        print(f"Ha ganado el jugado {p1} con {hp_p1} HP!!")
    else:
        print(f"Ha ganado el jugado {p2} con {hp_p2} HP!!")

juego()
