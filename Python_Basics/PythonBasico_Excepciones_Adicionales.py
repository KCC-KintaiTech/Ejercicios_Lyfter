print("*** Ejercicio #1: Pide nombre, edad ***")
print("---------------------------------------")

def analyze_name(parameter_name):
    try:
        entered_name = parameter_name
        if entered_name.isdigit():
            raise ValueError()
        else:
            return entered_name
        
    except ValueError as nve:
        print(f"Entrada de nombre no válida. El nombre no puede contener números solamente")
        return "No Definido"
    
def analyze_age(parameter_age):
    try:
        entered_age = int(parameter_age)
        return entered_age
          
    except ValueError as ave:
        print("Entrada de edad no válida. Debe contener números solamente")
        return "No definida"      
    
def name_age_main():
     
    name_input = input("Digite su nombre: ") 
    age_input = input("Digite su edad cumplida: ")

    name_out = analyze_name(name_input)
    age_out = analyze_age(age_input)

    print(f"Su nombre es: {name_out} y su edad es {age_out}.")

name_age_main()

print("*** Ejercicio #2: convertir lista a integer ***")
print("-----------------------------------------------")

def convert_value(parameter_value):
    try:
        value_integer = int(parameter_value)
        print(f"{parameter_value} se convirtió a {value_integer}")
    
    except ValueError:
        print(f"{parameter_value} no se pudo convertir")

def convert_main():
    value_list = ['4', 'hola', '10', '5.2']
    value_row = 0
    print("Resultado:")
    print("")
    while value_row < len(value_list):
        value_pulled = value_list[value_row]
        convert_value(value_pulled)
        value_row = value_row + 1
    print("")
convert_main()


print("*** Ejercicio #3: sumar floats ***")
print("-----------------------------------------------")

def convert_float(parameter_value):
    try:
        value_float = float(parameter_value)
        print(f"{parameter_value} se sumó correctamente")
        return value_float
    
    except ValueError:
        print(f"{parameter_value} no se pudo sumar")
        return 0
    
def float_main():
    value_list = ['10', 'manzana', '5.5', '3', 'n/a']
    value_row = 0
    total_floats = 0
    print("Resultado Suma Floats:")
    print("")
    while value_row < len(value_list):
        value_pulled = value_list[value_row]
        total_floats = total_floats + convert_float(value_pulled)
        value_row = value_row + 1
    print("Suma final es: ",total_floats) 

float_main()