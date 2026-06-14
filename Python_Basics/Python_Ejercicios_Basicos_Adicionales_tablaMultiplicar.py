print("*** Ejercio #4: Tabla de Multiplicar ***")
number_sequence = 1
number_entered = int(input("Digite un número entero del 1 al 10: "))
while (number_sequence <= 12):
    print(f"{number_entered} x {number_sequence} = {number_entered * number_sequence}")
    number_sequence = number_sequence + 1