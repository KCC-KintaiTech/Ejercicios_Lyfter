print("*** Ejercicio #3:  Adivinar # random hasta que sea correcto ***")
import random
mystery_number = random.randint(1,10)
bad_guess = True
while (bad_guess):
    guessed_number = int(input("Adivine el número del 1 al 10: "))
    if (guessed_number == mystery_number):
        bad_guess = False
print("Adivinaste bien!! El número misterioso es ", mystery_number)
