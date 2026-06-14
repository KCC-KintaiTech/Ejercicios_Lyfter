print("*** Ejercicio #1:  Imprimir dos cosas diferentes ***")

def print_first():
    print("Esto es lo primero que se imprime")

def print_second():
    print_first()
    print("Esto se lo segund0 que se imprime")

def main_exercise_1():
    print_second()

main_exercise_1()


print("----------------------------------------")
print("*** Ejercicio #2: Referenciar una variable local afuera de funcion")
def local_variable():
    my_local_variable = "Ya le perdí el miedo a Python!"
    print("Esta es my_local_variable adentro de función: ",my_local_variable)

def main_exercise_2():
    local_variable()
    ## print("Intentando llamarla afuera detiene el programa: ",my_local_variable)

main_exercise_2()


print("----------------------------------------")
print("*** Ejercicio #3: Imprimir la suma de una lista de numeros")
def sum_list_numbers(parameter_number_list):
    item_counter = 0
    final_number = 0
    while (item_counter < len(parameter_number_list)):
        final_number = final_number + parameter_number_list[item_counter]
        item_counter = item_counter + 1
    return(final_number)

def main_exercise_3():
    number_list = [4, 6, 2, 29]
    number_aggregated = sum_list_numbers(number_list)
    print("Número total es:",number_aggregated)

main_exercise_3()


print("----------------------------------------")
print("*** Ejercicio #4: Invertir los caracteres de un string")

def reverse_string(parameter_string):
    backward_string = ""
    for index in range(len(parameter_string)-1,-1,-1):
         char_index = parameter_string[index]
         backward_string = backward_string + char_index
    return(backward_string)

def main_exercise_4():
     char_split = input("Digite la palabra que desea reversar: ")
     new_string = reverse_string(char_split)
     print("Al revés es: ",new_string)
  
main_exercise_4()


print("----------------------------------------")
print("*** Ejercicio #5: Contar mayusculas y minusculas")

def identify_upper_letters(parameter_string):
    char_counter = 0
    total_uppercase = 0
    while (char_counter < len(parameter_string)):
        char_current = parameter_string[char_counter]
        if char_current.isupper():
            total_uppercase = total_uppercase + 1
        char_counter = char_counter + 1
    return(total_uppercase)

def identify_lower_letters(parameter_string):
    char_counter = 0
    total_lowercase = 0
    while (char_counter < len(parameter_string)):
        char_current = parameter_string[char_counter]
        if char_current.islower():
            total_lowercase = total_lowercase + 1
        char_counter = char_counter + 1
    return(total_lowercase)

def main_exercise_5():
    string_to_pass = input("Digite la frase que desea evaluar: ")
    print("Total de mayúsculas: ",identify_upper_letters(string_to_pass))
    print("Total de minúsculas: ",identify_lower_letters(string_to_pass))

main_exercise_5()


print("----------------------------------------")
print("*** Ejercicio #6: Ordernar palabras separadas por guiones alfabeticamente")

def sort_word_string(parameter_word_string):
    working_list = []
    sorted_string = ""
    working_list = parameter_word_string.split("-")
    working_list.sort()
    sorted_string = "-".join(working_list)
    return(sorted_string)

def main_exercise_6():
    typed_words = input("Digite las palabras separadas con un guión entre ellas: ")
    final_string = sort_word_string(typed_words)
    print("En orden alfabético: ",final_string)

main_exercise_6()


print("----------------------------------------")
print("*** Ejercicio #7: identificar si numero es primo")

def identify_prime_number(parameter_number):
    prime_base = 3
    prime_label = "es primo"
    if parameter_number <= 1:
        prime_label = "no es primo"
    elif parameter_number in (2, 3, 5, 7): ## quitar los más bajos
        prime_label = "es primo"
    elif parameter_number != 2 and parameter_number % 2 == 0:
        prime_label = "es no primo"
    else:
        while prime_base * prime_base <= parameter_number:
            if parameter_number % prime_base == 0:
                prime_label = "es no primo"
            prime_base = prime_base + 2
    return(prime_label)
        

def main_exercise_7():
    entered_number = int(input("Digite un número entero: "))
    prime_indicator = identify_prime_number(entered_number)
    print(f"Número {entered_number} {prime_indicator}")

main_exercise_7()