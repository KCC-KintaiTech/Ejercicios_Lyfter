print("*** Ejercicio #1:  Informacion de Hotel ***")
hotel_info = {
    "nombre":"Vistas al Oceano",
    "Estrellas":"4",
    "Habitaciones":[
    {
        "Numero":"1",
        "Piso":"2",
        "Precio":100
    },
    {
        "Numero":"2",
        "Piso":"2",
        "Precio":120
    }
    ]
}
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

print("--------------------------")
print("*** Ejercicio #3:  Borrar keys de un diccionario ***")
keys_delete = ['access_level', 'age']
keys_all = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
for key in keys_delete:
    if key in keys_all:
        keys_all.pop(key)
print(keys_all)