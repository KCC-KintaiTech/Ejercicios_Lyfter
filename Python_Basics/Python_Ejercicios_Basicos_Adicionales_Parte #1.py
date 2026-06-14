print("*** Ejercicio #1:  Descuento de productos ***")
product_price = float(input("Digite el precio del producto: "))
if(product_price >= 100):
    product_discount = product_price * 0.10
else:
    product_discount = product_price * 0.02
print("El precio neto con descuento es de: ",product_price - product_discount)
print("")
print("*** Ejercicio #2:  Tiempo en segundos comparado con 10 minutos ***")
time_in_seconds = int(input("Digite cantidad de segundos: "))
time_limit = 600
if(time_in_seconds > time_limit):
    limit_label = "es mayor a 10 minutos"
elif (time_in_seconds < time_limit):
    time_remaining = time_limit - time_in_seconds
    limit_label = f" es menor a 10 minutos. Quedan {time_remaining} segundos restantes"
else:
    limit_label = " es igual a 10 minutos"
print(f"{time_in_seconds} segundos {limit_label}")
print("")
print("*** Ejercicio #3:  Numero que se suma desde 1 ***")
number_limit = int(input("Digite el número que desea se autosume: "))
number_sequence = 1
number_total = 0
if(number_limit == 0):
    print("La gracia es que sea mayor a 0")
else:
    while (number_sequence <= number_limit):
        number_total = number_total + number_sequence
        number_sequence = number_sequence + 1
print("La suma total es: ",number_total)