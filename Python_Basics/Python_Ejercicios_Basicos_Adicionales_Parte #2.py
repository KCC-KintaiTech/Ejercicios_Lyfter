print("*** Ejercicio #1:  Adivinar número random hasta que sea correcto ***")
import random
mystery_number = random.randint(1,10)
bad_guess = True
while (bad_guess):
    guessed_number = int(input("Adivine el número del 1 al 10: "))
    if (guessed_number == mystery_number):
        bad_guess = False
print("Adivinaste bien!! El número misterioso es ", mystery_number)
print("---")
print("*** Ejercicio #2: numero 30 o suma numeros = 30 ***")
number_limit = 3
number_total = 0
number_counter = 1
number_30 = False
while (number_counter <= number_limit):
    number_entered = int(input(f"Digite el número #{number_counter} "))
    number_total = number_total + number_entered
    if (number_entered == 30):
        number_30 = True
    number_counter = number_counter + 1
if (number_30 or number_total == 30):
    print("Correcto")
else:
    print("Incorrecto")
print("---")
print("*** Ejercicio #3: Convertidor de Temperaturas ***")
temperature_entered = float(input(f"Ingrese temperatura en celsius "))
temperature_Fahrenheit = (temperature_entered * 1.8) + 32
temperature_Kelvin = temperature_entered + 273.15
print("Fahrenheit: ",temperature_Fahrenheit)
print("Kelvin: ",temperature_Kelvin)
print("---")
print("*** Ejercio #4: Tabla de Multiplicar ***")
number_sequence = 1
number_entered = int(input("Digite un número entero del 1 al 10: "))
while (number_sequence <= 12):
    print(f"{number_entered} x {number_sequence} = {number_entered * number_sequence}")
    number_sequence = number_sequence + 1