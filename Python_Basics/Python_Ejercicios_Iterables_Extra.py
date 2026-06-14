print('*** Ejercicio #1:  Cuantas veces aparece un numero ***')
my_list = [4,2,7,2,8,2,1,9,1,3,0,7,8,1,9]
number_wanted = int(input("Digite número a buscar: "))
number_counter = 0
for number_list in my_list:
    if(number_list == number_wanted):
        number_counter = number_counter + 1
print(f"El número {number_wanted} fue encontrado {number_counter} veces")

print("****************************")
print('*** Ejercicio #2:  Encontrar si hay número negativo ***')
my_list = [4,2,7,-2,8,2,1,9,1,-3,0,7,8,1,9]
number_negative = 0
number_counter = 0
for number_list in my_list:
    if(number_list * -1 > 0):
        number_counter = number_counter + 1
print(f"Se encontraron {number_counter} números negativos")

print("****************************")
print('*** Ejercicio #3:  Desplegar el número más  bajo ***')
my_list = [4,2,7,42,8,2,1,9,1,-15,0,7,8,1,9]
number_lowest = 0
number_counter = 0
for number_list in my_list:
    if(number_list < number_lowest):
        number_lowest = number_list
print(f"El número más bajo es: {number_lowest} ")

print("****************************")
print('*** Ejercicio #4:  Promedio y listar números mayores a él ***')
my_list = [4,2,7,42,8,2,12,9,21,7,8,15,9]
number_average = sum(my_list) / len(my_list)
number_counter = 1
my_average_list = []
for number_list in my_list:
    if(number_list > number_average):
        my_average_list.append(number_list)
print("El promedio de la lista original es: ",number_average)
print("La nueva lista con números mayores al promedio es:",my_average_list)

print("****************************")
print('*** Ejercicio #5:  Palabras con mas de 4 letras ***')
word_counter = 1
word_list = 5
word_length = 4
word_list_output = []
while word_counter <= word_list:
    word_entry = input(f"Digite la palabra #{word_counter} de {word_list}: ")
    if (len(word_entry) > word_length):
        word_list_output.append(word_entry)
    word_counter = word_counter + 1
print(f"Las palabras mayores a {word_length} letras son: ",word_list_output)