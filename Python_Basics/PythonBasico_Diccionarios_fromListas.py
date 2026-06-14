print("--------------------------")
print("*** Ejercicio #2:  Crear diccionario con listas ***")
list_keys = ["first_name","last_name","role"]
list_values = ["Kattia","Chavarria","Software Engineer"]
list_pointer = 0
dictionary_content = ""
dictionary_final = {}
while list_pointer < len(list_keys):
    key_name = list_keys[list_pointer]
    key_value = list_values[list_pointer]
    if key_name not in dictionary_final:
        dictionary_final[key_name] = key_value
        list_pointer = list_pointer + 1
print(dictionary_final)