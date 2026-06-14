print("*** #1: Leer archivo, escribir archivo ***")
print("------------------------------------------")

def read_file():
   try:
    file_name = r"\Publico\Canciones.txt"
    songs_list_source = []
    with open(file_name,encoding="utf-8") as file:
        for line in file.readlines():
            songs_list_source.append(line.strip())
    songs_list_source.sort()
    return songs_list_source
   
   except FileNotFoundError as fnf_error:
      print(f"Archivo{file_name} no se encontró en ruta anotada")
      return ["Nothing found"]
   
def write_file(parameter_new_list):
   try:
      new_file_name = r"\Publico\CancionesOrdenadas.txt"
      with open(new_file_name, "w", encoding="utf-8") as new_file:
         for song in parameter_new_list:
            new_file.write(song+"\n")
      return new_file_name
  
   except FileNotFoundError as fnf_error:
    print(f"Archivo {new_file_name} no se encontró en ruta descrita")
    return ["Nothing found"]

def read_file_main():
   sorted_songs = []
   sorted_songs = read_file()
   write_file(sorted_songs)
   print("Nuevo archivo con canciones ordenadas listo")
   print("")


read_file_main()
