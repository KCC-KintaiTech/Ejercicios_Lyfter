print("*** Ejercicio Calculadora ***")
def calculate_new_number():
    try:
        actual_number = 0.0
        calculated_number = 0.0
        keep_calculating = True
        actual_number = float(input("Digite el primer número: "))
        
        while keep_calculating:
            try:
            
                print("1-Sumar     2-Restar     3-Multiplicar     4-Dividir     5-Borrar Resultado    6-Salir")
                selected_option = int(input("Digite el # de opción que desea ejecutar: "))

                if selected_option in [1,2,3,4]:
                    new_number = float(input("Digite otro número: "))
                    if selected_option == 1:
                        actual_number = actual_number + new_number
                    elif selected_option == 2:
                        actual_number = actual_number - new_number
                    elif selected_option == 3:
                        actual_number = actual_number * new_number
                    else:
                        actual_number = actual_number / new_number
                elif selected_option == 5:
                    actual_number = 0.0
                elif selected_option == 6:
                    keep_calculating = False
                else:
                    print("Opcion seleccionada no valida. Intente otra vez")
                print("El resultado es: ",actual_number)

            except ValueError as wv:
                print(f"Entrada no es válida: {wv}")
            except TypeError as wt:
                print(f"Entrada no es válida: {wt}")
            except ZeroDivisionError as wz:
                print("No se puede dividir entre 0")



    except ValueError as v:
            print(f"Entrada no es válida, solo acepta números. Inicie nuevamente")
    except TypeError as t:
            print(f"Entrada no es válida, verifique que son números.: {t}")
    
        


def calculadora_main():

    print(" ----------------------------------------")
    print(" ***** Calculadora Mi Abaco ***** ")
    print("-----------------------------------------")
    calculate_new_number()

calculadora_main()
