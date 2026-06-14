print("*** Exercise #1: Read CSV with game names using commas***")
print("*************************************************")

import csv

def read_videogames_file(param_file_name):
    try:
        with open(param_file_name, mode='r', encoding='utf-8') as open_file:

            reader_csv = csv.reader(open_file)

            file_header = next(reader_csv)
            
            print(f"{'*** Lista de Juegos ***':^40}\n")
            
            for game_row in reader_csv:
                nombre, genero, desarrollador, clasificacion = game_row
                print(f"Nombre: {nombre}")
                print(f"Género: {genero}")
                print(f"Desarrollador: {desarrollador}")
                print(f"Clasificación: {clasificacion}")
                print("-" * 30) # sirve para separar visualmente los juegos

    except FileNotFoundError:
        print(f"Error: El archivo '{param_file_name}' no se encontró en  la ruta especificada.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def read_csv_games_main():
    csv_file_name =r"c:\publico\Lista_juegos_con_comas.csv"
    read_videogames_file(csv_file_name)

read_csv_games_main()


print("*** Exercise #2: Generate CSV with game names using tabs***")
print("***********************************************************")


import csv

def read_videogames_category(param_file_name):
    
    search_category = input("Digite la clasificación ESRB que desea filtrar (Ej: E, T, M): ").strip().upper()
    
    try:
        with open(param_file_name, mode='r', encoding='utf-8') as open_file:
            reader_csv = csv.reader(open_file)
            
            file_header = next(reader_csv)
            
            print(f"\n--- Juegos con clasificación: {search_category} ---")
            category_found = False
            
            for game_row in reader_csv:
                nombre, genero, desarrollador, clasificacion = game_row
                
                if clasificacion.upper() == search_category:
                    print(f"Nombre: {nombre} | Género: {genero} | Desarrollador: {desarrollador}")
                    category_found = True
            
            if not category_found:
                print(f"No se encontró videojuegos con la clasificación '{search_category}'.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{param_file_name}'.")

def filter_games_category_main():
   csv_file_name =r"c:\publico\Lista_juegos_con_comas.csv"
   read_videogames_category(csv_file_name)

filter_games_category_main()


print("*** Exercise #3: Count game genres and display totals ***")
print("***********************************************************")


import csv

def count_videogames_genres(param_file_name):
    genre_count = {}       
    try:
        with open(param_file_name, mode='r', encoding='utf-8') as open_file:
            reader_csv = csv.reader(open_file)
           
            next(reader_csv)
          
            for game_row in reader_csv:
                genero = game_row[1].strip()
                if genero in genre_count:
                    genre_count[genero] = genre_count + 1
                else:
                    genre_count[genero] = 1

        genres_sorted = sorted(genre_count.keys())        
        print(" Géneros encontrados:  ")

        for genero in genres_sorted:
            cantidad = genre_count[genero]
            print(f"  {genero}: {cantidad}")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{param_file_name}'.")

def count_game_genres_main():
   csv_file_name =r"c:\publico\Lista_juegos_con_comas.csv"
   count_videogames_genres(csv_file_name)

count_game_genres_main()


print("*** Exercise #4: List games by Developer name ***")
print("***********************************************************")


import csv

def read_videogames_developer(param_file_name):
    search_dev = input("Digite el nombre del desarrollador que desea buscar (Ej: Ubisoft): ").strip().lower()
    
    try:
        with open(param_file_name, mode='r', encoding='utf-8') as open_file:
            reader_csv = csv.reader(open_file)
            file_header = next(reader_csv)
            
            print(f"\nVideojuegos desarrollados por {search_dev.title()}:")
            dev_found = False
            
            for game_row in reader_csv:
                nombre, genero, desarrollador, clasificacion = game_row
                
                if desarrollador.strip().lower() == search_dev:
                    print(f"- {nombre} (Clasificación: {clasificacion}, Género: {genero})")
                    dev_found = True
            
            if not dev_found:
                print(f"No se encontraron videojuegos desarrollados por '{search_dev}'.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{param_file_name}'.")

def filter_games_developer_main():
    csv_file_name = r"c:\publico\Lista_juegos_con_comas.csv"
    read_videogames_developer(csv_file_name)

filter_games_developer_main()

