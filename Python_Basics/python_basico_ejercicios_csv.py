print("*** Exercise #1: Generate CSV with game names using commas***")
print("*************************************************")

import csv

def input_game_list():
    game_list = []
    game_quantity = 0
    game_number = 1

    while True:
        try:
            game_quantity = int(input("Digite cuántos juegos va a registrar:  "))
            if game_quantity <= 0:
                print("Cantidad no es válida")
                continue
            break
        except ValueError:
            print("Cantidad no es válida. Deber ser un número entero.")

    while game_number <= game_quantity:
        print("------------------------")
        print(f"** Juego #{game_number}")
        game_name = input("Name of the game: ").strip()
        game_category = input("Category (Action,Sports,RPG): ").strip()
        game_developer = input("Developer: ").strip()
        game_classification  = input("Clasification ESRB (E, E10+, T, M, R): ").strip()
        game_list.append({
            "name": game_name,
            "genre": game_category,
            "developer": game_developer,
            "clasification": game_classification
        })
        game_number = game_number + 1

    return game_list

def record_csv(parameter_game_list ):
    csv_file_name =r"c:\publico\List_games_with_commas.csv"
    csv_columns = ["name", "genre", "developer", "clasification"]

    with open(csv_file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(parameter_game_list)
    print("")
    print(f"Archivo CSV generado como: {csv_file_name}")

def csv_games_main():
    game_list_entered = input_game_list()
    record_csv(game_list_entered)

csv_games_main()

print("*** Exercise #2: Generate CSV with game names using tabs***")
print("***********************************************************")

import csv

def input_game_list_tabs():
    game_list = []
    game_quantity = 0
    game_number = 1

    while True:
        try:
            game_quantity = int(input("Digite cuántos juegos va a registrar:  "))
            if game_quantity <= 0:
                print("Cantidad no es válida")
                continue
            break
        except ValueError:
            print("Cantidad no es válida. Deber ser un número entero.")

    while game_number <= game_quantity:
        print("------------------------")
        print(f"** Juego #{game_number}")
        game_name = input("Nombre del juego: ").strip()
        game_category = input("Categoría (Acción,Deportes,RPG): ").strip()
        game_developer = input("Desarrollador: ").strip()
        game_classification  = input("Clasificación ESRB (E, E10+, T, M, R): ").strip()
        game_list.append({
            "nombre": game_name,
            "genero": game_category,
            "desarrollador": game_developer,
            "clasificacion": game_classification
        })
        game_number = game_number + 1

    return game_list

def record_csv_tabs(parameter_game_list ):
    csv_file_name =r"c:\publico\Lista_juegos_con_tabs.csv"
    csv_columns = ["nombre", "genero", "desarrollador", "clasificacion"]

    with open(csv_file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns,delimiter="\t")
        writer.writeheader()
        writer.writerows(parameter_game_list)
    print("")
    print(f"Archivo CSV con tabs generado como: {csv_file_name}")

def csv_games_main_tabs():
    game_list_entered = input_game_list_tabs()
    record_csv_tabs(game_list_entered)

csv_games_main_tabs()

