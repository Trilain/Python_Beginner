# ejemplo y uso de try except
# while True:
#     try:
#         num = int(input("Ingrese un número: "))
#         break
#     except ValueError as er:
#         print("Solo números enteros")
#         print(er)
# Manejar control de números solo números enteros con ValueError

# runtime: el tiempo que se ejecuta el programa

# total = 0
# for i in range (3):
#     while True:    
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             total+=n
#             break
#         except:
#             print("Solo números decimales")
# prom=total/3
# print(f"El promedio es: {prom}")

op=0
total=0
while op!=4:
    print("1.- PC $500.000")
    print("2.- LGTV 55 pulgadas $450.000")
    print("3.- Microondas Mademsa $100.000")
    print("4.- Salir")
    print("Seleccione una opcion")
    try:
        op=int(input())
        match op:
            case 1:
                print("El total a pagar es ",500000*1.19 )
                total+=500000*1.19
            case 2:
                print("El total a pagar es ",450000*1.19 )
                total+=450000*1.19
            case 3:
                print("El total a pagar es ",100000*1.19 )
                total+=100000*1.19
            case 4:
                print("Saliendo")
                print("El total a pagar es", total)
            case _:
                print("Opción inválida")
    except ValueError as e:
        print("Error, Solo números enteros. Error: ", e)