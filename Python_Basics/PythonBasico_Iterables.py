** ejercicios iterables ***
print("***  Ejercicio #1:  Imprimir listas al mismo tiempo ***")
first_list = ['Hay','en','que','iteracion','indices','muy']
second_list =['casos','los','la','por','es','util']
item_counter = 0
while (item_counter < len(first_list)):
    print(first_list[item_counter])
    print(second_list[item_counter])
    item_counter = item_counter + 1
print("Listas completas")

print("----------")
print("*** Ejercicio #2: Imprimir string letra por letras *** ")
char_split = input("Digite la palabra que desea reversar: ")
for index in range(len(char_split)-1,-1,-1):
	char_index = char_split[index]
	print(char_index)

print("----------")
print("*** Ejercicio #3: Intercambiar primer y ultimo valores de una lista *** ")
my_list = ['primero', 3, 6, 1, 'ultimo']
index_last = len(my_list) - 1
first_value = my_list[0]
last_value = my_list[index_last]
print(f"Original list: {my_list}")
my_list[0] = last_value
my_list[index_last] = first_value
print(f"Updated list: {my_list}")

print("----------")
print("*** Ejercicio #4: Remover numeros impares *** ")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for list_index in range(len(my_list)-1,-1,-1):
    if my_list[list_index] %2 != 0:
        my_list.pop(list_index)
print(my_list)

print("----------")
print("*** Ejercicio #5: El mas alto de una lista de 10 numeros *** ")
number_sequence = 1
number_limit = 10
number_highest = 0
number_list = []
while number_sequence <= number_limit:
    number_new = int(input(f"Digite el número #{number_sequence}: "))
    if number_new > number_highest:
        number_highest = number_new
    number_list.append(number_new)
    number_sequence = number_sequence + 1
print(number_list)
print("El número más alto fue: ",number_highest)