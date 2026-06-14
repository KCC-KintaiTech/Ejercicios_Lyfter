print("*** Exercise #4: List games by Developer name ***")
print("***********************************************************")


import csv

def read_videogames_developer(param_file_name):
    # 1. Pedir al usuario el desarrollador que desea buscar
    # Usamos .strip() para limpiar espacios y .lower() para una búsqueda más flexible
    search_dev = input("Digite el nombre del desarrollador que desea buscar (Ej: Ubisoft): ").strip().lower()
    
    try:
        with open(param_file_name, mode='r', encoding='utf-8') as open_file:
            reader_csv = csv.reader(open_file)
            
            # Saltamos el encabezado
            file_header = next(reader_csv)
            
            # Buscamos el nombre original para el título (opcional, para estética)
            print(f"\nVideojuegos desarrollados por {search_dev.title()}:")
            dev_found = False
            
            # 2. Recorrer el archivo y filtrar
            for game_row in reader_csv:
                # nombre (0), genero (1), desarrollador (2), clasificacion (3)
                nombre, genero, desarrollador, clasificacion = game_row
                
                # Comparamos el desarrollador en minúsculas para que no importe si escriben "Ubisoft" o "ubisoft"
                if desarrollador.strip().lower() == search_dev:
                    # Formato legible según tu ejemplo
                    print(f"- {nombre} (Clasificación: {clasificacion}, Género: {genero})")
                    dev_found = True
            
            # 3. Mensaje en caso de no encontrar coincidencias
            if not dev_found:
                print(f"No se encontraron videojuegos desarrollados por '{search_dev}'.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{param_file_name}'.")

def filter_games_developer_main():
    # Asegúrate de que la ruta sea correcta para tu sistema
    csv_file_name = r"c:\publico\Lista_juegos_con_comas.csv"
    read_videogames_developer(csv_file_name)

filter_games_developer_main()