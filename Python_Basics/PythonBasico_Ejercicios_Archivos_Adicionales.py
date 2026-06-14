print("*** #1: Leer archivo con lineas quitar salto y  escribir archivo con una linea***")
print("------------------------------------------")

def read_file():
   try:
    file_name = r"\Publico\VariasLineas.txt"
    row_list_source = []
    with open(file_name,encoding="utf-8") as file:
        for line in file.readlines():
            row_list_source.append(line.strip())
    return row_list_source
   
   except FileNotFoundError as fnf_error:
      print(f"Archivo{file_name} no se encontró en ruta anotada")
      return None
   
def write_file(parameter_row_list):
   try:
      new_file_name = r"\Publico\UnaLinea.txt"
      with open(new_file_name, "w", encoding="utf-8") as new_file:
         for read_line in parameter_row_list:
            new_file.write(read_line + " ")
      return new_file_name
  
   except FileNotFoundError as fnf_error:
    print(f"Archivo {new_file_name} no se encontró en ruta descrita")
    return None

def read_file_main():
   row_list_file = read_file()
   if row_list_file:
    write_file(row_list_file)
    print("Nuevo archivo con una linea listo")
    print("")

read_file_main()


print("*** Ejercicio #2: Leer archivo con lineas quitar salto y  escribir archivo con una linea***")
print("------------------------------------------")

def read_words():
   try:
    file_name = r"\Publico\CuentaPalabras.txt"
    with open(file_name,encoding="utf-8") as file:
        file_content = file.read()
        all_words = file_content.split()
    return all_words
   
   except FileNotFoundError as fnf_error:
      print(f"Archivo{file_name} no se encontró en ruta anotada")
      return None
  
def count_words_main():
   
   words_string = read_words()
   if words_string:
    print(f"El archivo contiene {len(words_string)} palabras")
   else:
    print("El archivo no tiene contenido o no se encontró")
    print("")

count_words_main()


print("*** Ejercicio #3: De minusculas a Mayusculas ***")
print("------------------------------------------")

def read_file_lower():
   try:
    lower_file_name = r"\Publico\Minusculas.txt"
    lower_rows = []
    with open(lower_file_name,encoding="utf-8") as lower_file:
        for lower_line in lower_file.readlines():
            lower_rows.append(lower_line.strip())
    return lower_rows
   
   except FileNotFoundError as fnf_error:
      print(f"Archivo{lower_file_name} no se encontró en ruta anotada")
      return None
   
def write_file_upper(parameter_lower_rows):
   try:
      upper_file_name = r"\Publico\Mayusculas.txt"
      with open(upper_file_name, "w", encoding="utf-8") as upper_file:
         for upper_line in parameter_lower_rows:
            upper_file.write(upper_line.upper() + "\n")
      return upper_file_name
  
   except FileNotFoundError as fnf_error:
    print(f"Archivo {upper_file_name} no se encontró en ruta descrita")
    return None

def lower_to_upper_main():
   lower_lines = read_file_lower()
   if lower_lines:
    upper_file_name =  write_file_upper(lower_lines)
    print(f"Nuevo archivo {upper_file_name} convertido a mayusculas esta listo")
    print("")

lower_to_upper_main()


print("*** Ejercicio #4: Agregar lineas a un archivo ***")
print("------------------------------------------")

def append_file(parameter_input_text):
   try:
      append_file_name = r"\Publico\AgregarTexto.txt"
      with open(append_file_name, "a", encoding="utf-8") as append_file:
        append_file.write("\n" + parameter_input_text)
      return append_file_name
  
   except FileNotFoundError as fnf_error:
    print(f"Archivo {append_file_name} no se encontró en ruta descrita")
    return None

def append_line_main():
   input_text = input("Escriba el texto que desea agregar al archivo: ")
   if len(input_text)>0:
    upper_file_name =  append_file(input_text)
    print(f"Se ha agregado texto a {upper_file_name}.")
    print("")

append_line_main()