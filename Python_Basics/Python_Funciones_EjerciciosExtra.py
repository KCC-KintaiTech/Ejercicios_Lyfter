print("*** Ejercicio #1:  contar cuantas veces aparece 1 letra en un string ***")

def find_letter(parameter_typed_string,parameter_wanted_letter):
    position_in_string = 0
    total_showups = 0
    while position_in_string < len(parameter_typed_string):
        if parameter_typed_string[position_in_string] == parameter_wanted_letter:
            total_showups= total_showups + 1
        position_in_string = position_in_string + 1
    print(f"Total de veces {parameter_wanted_letter} aparece en el texto: {total_showups}")
    

def main_exercise_1():
    typed_string = input("Digite el texto que desea evaluar: ")
    typed_wanted_letter = input("Digite la letra que desea encontrar: ")
    find_letter(typed_string,typed_wanted_letter)

main_exercise_1()


print("*** Ejercicio #2:  Devolver lista de palabras ***")

def count_characters(parameter_word_list, parameter_length):
    word_length = 0
    word_list_new = []
    for word_in_list in parameter_word_list:
        word_length = len(word_in_list)
        if word_length >= parameter_length:
            word_list_new.append(word_in_list)
    print(f"Palabras con {parameter_length} letras o más: {word_list_new} ")
    

def main_exercise_2():
    word_list = ["cielo", "sol", "maravilloso", "día"]
    word_length = int(input("Ingrese el numero de letras minimas en la palabra: "))
    count_characters(word_list,word_length)

main_exercise_2()


print("*** Ejercicio #3:  Contar vocales ***")

def find_vowels(parameter_typed_string):
    position_in_string = 0
    total_vowels = 0
    vowel_list = ['a','e','i','o','u','A','E','I','O','U']
    while position_in_string < len(parameter_typed_string):
        if parameter_typed_string[position_in_string] in vowel_list:
            total_vowels = total_vowels + 1
        position_in_string = position_in_string + 1
    print("Total de vocales: ",total_vowels)
    

def main_exercise_3():
    typed_string = input("Digite la palabra o frase que desea evaluar: ")
    find_vowels(typed_string)

main_exercise_3()