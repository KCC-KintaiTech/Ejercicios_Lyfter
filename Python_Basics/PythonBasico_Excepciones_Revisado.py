print("*** Ejercicio Calculadora ***")

def sum_numbers(parameter_actual_number,parameter_new_number):
    try:
        sum_actual_number = parameter_actual_number + parameter_new_number
        return sum_actual_number
    except ValueError as wv:
        print(f"Entrada no válida: {wv}")
    except TypeError as wt:
        print(f"No se pueden sumar dos tipos diferentes de datos: {wt}")

def subtract_numbers(parameter_actual_number,parameter_new_number):
    try:
        sub_actual_number = parameter_actual_number - parameter_new_number
        return sub_actual_number
    except ValueError as wv:
        print(f"Entrada no válida: {wv}")
    except TypeError as wt:
        print(f"No se pueden restar dos tipos diferentes de datos: {wt}")
   

def multiply_numbers(parameter_actual_number,parameter_new_number):
    try:
        mul_actual_number = parameter_actual_number * parameter_new_number
        return mul_actual_number

    except ValueError as wv:
        print(f"Entrada no es válida: {wv}")
    except TypeError as wt:
        print(f"No se puede multiplicar dos tipos de datos diferentes: {wt}")
    
def divide_numbers(parameter_actual_number,parameter_new_number):
    try:
        div_actual_number = parameter_actual_number / parameter_new_number
        return div_actual_number

    except ValueError as wv:
        print(f"Entrada no es válida: {wv}")
    except TypeError as wt:
        print(f"No se pueden dividir dos tipos de datos diferentes: {wt}")
    except ZeroDivisionError as wz:
        print("No se puede dividir entre 0")
        return parameter_actual_number
        
        
def clean_up_numbers(parameter_actual_number):
    parameter_actual_number = 0.0
    return parameter_actual_number

def calculate_new_number():
    try:
        actual_number = 0.0
        calculated_number = 0.0
        keep_calculating = True
        actual_number = float(input("Digite el primer número: "))
        
        while keep_calculating:
            try:
                print("1. Sumar")
                print("2. Restar")
                print("3. Multiplicar")
                print("4. Dividir")
                print("5. Borrar Resultado")
                print("6. Salir")
                print("")
                
                selected_option = int(input("Digite el # de operación que desea aplicar: "))
                if selected_option in [1,2,3,4]:
                    new_number = float(input("Digite el siguiente número: "))    
                    if selected_option == 1:
                        actual_number = sum_numbers(actual_number,new_number)
                    elif selected_option == 2:
                        actual_number = subtract_numbers(actual_number,new_number)
                    elif selected_option == 3:
                        actual_number = multiply_numbers(actual_number,new_number)
                    else:
                        actual_number = divide_numbers(actual_number,new_number)
                elif selected_option == 5:
                    actual_number = clean_up_numbers(actual_number)
                elif selected_option == 6:
                    keep_calculating = False
                else:
                    print("Opcion seleccionada no valida. Intente otra vez")
                    print("")
                
                print("El resultado es: ",actual_number)
                print("---------------------------------")
                print("")
            except ValueError as v:
                print(f"Opción no es válida. Intente nuevamente")

    except ValueError as v:
        print(f"Entrada no es válida, solo acepta números. Inicie nuevamente")
    
 
def calculadora_main():

    print(" ----------------------------------------")
    print(" ***** Calculadora Mi Abaco ***** ")
    print("-----------------------------------------")
    calculate_new_number()

calculadora_main()
