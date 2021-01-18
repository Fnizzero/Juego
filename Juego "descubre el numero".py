numero = 467
usuario = 0
while usuario != numero:
    usuario = int(input("cual es el número?"))
    if usuario > numero:
        print("digita un número menor")
    elif usuario < numero:
        print("digita un número mayor")
    else:
        print("correcto!")
