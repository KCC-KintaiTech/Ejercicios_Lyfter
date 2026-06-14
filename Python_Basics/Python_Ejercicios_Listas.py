print('*** Ejercicio #1:  Imprimir listas al mismo tiempo')
first_list = ['Hay', 'en', 'que','iteracion','indices', 'muy']
second_list = ['casos','los','la','por', 'es','util']
item_counter = 0
while item_counter < len(first_list):
    print(first_list[item_counter])
    print(second_list[item_counter])
    item_counter = item_counter + 1
print("Listas completas", item_counter)