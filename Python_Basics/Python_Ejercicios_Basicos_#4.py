print("*** Ejercicio #4: Calcular # mayor en una lista de 3 números ***")
expected_entries = 3
entry_counter = 1
entry_highest = 0
while (entry_counter <= expected_entries):
    entry_intake = int(input(f"Digite número entero #{entry_counter} "))
    if (entry_intake>=entry_highest):
        entry_highest = entry_intake
    entry_counter = entry_counter + 1
print("El mayor número digitado fue ",entry_highest)
