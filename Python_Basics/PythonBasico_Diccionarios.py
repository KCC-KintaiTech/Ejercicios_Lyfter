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
while list_pointer < len(list_keys):
    dictionary_content = f"{dictionary_content}'{list_keys[list_pointer]}':'{list_values[list_pointer]}'"
    if(list_pointer<len(list_keys)-1):
        dictionary_content = f"{dictionary_content},"
    list_pointer = list_pointer + 1
dictionary_final = "{"+ dictionary_content + "}"
print(dictionary_final)


print("--------------------------")
print("*** Ejercicio #2: Alternativa que crea un diccionario que se pueda usar ***")
list_keys = ["first_name","last_name","role"]
list_values = ["Kattia","Chavarria","Software Engineer"]

# Con este comando se crea el diccionario que se pueda referenciar, el anterior crea un string
# Lo que pasa es que todavia no se ha visto este contenido en clase
dictionary_real = dict(zip(list_keys, list_values))
print("Diccionario real: ",dictionary_real)

print("--------------------------")
print("*** Ejercicio #3:  Borrar keys de un diccionario ***")
keys_delete = ['access_level', 'age']
keys_all = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
for key in keys_delete:
    if key in keys_all:
        keys_all.pop(key)
print(keys_all)