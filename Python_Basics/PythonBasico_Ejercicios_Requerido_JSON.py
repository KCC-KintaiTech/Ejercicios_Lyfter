print("*** Exercise #1: Read existing JSON file and add one item  ***")
print("***********************************************************")


import json
import os

# --- RUTINA 1: LEER EL ARCHIVO ---
def Load_pokemons(param_file_name):
    """Lee el archivo JSON y devuelve la lista de pokémones."""
    if os.path.exists(param_file_name):
        with open(param_file_name, 'r', encoding='utf-8') as pokemon_file:
            try:
                return json.load(pokemon_file)
            except json.JSONDecodeError:
                return []
    return []

# --- RUTINA 2: PEDIR DATOS AL USUARIO ---
def request_new_pokemon():
    """Interactúa con el usuario y devuelve un diccionario con el nuevo Pokémon."""
    print("\n--- Registro de Nuevo Pokemon ---")
    pokemon_name = input("Nombre: ")
    pokemon_level = int(input("Nivel: "))
    
    pokemon_types_input = input("Tipos (separados por coma, ej: Agua, Fuego): ")
    pokemon_types_clean = [t.strip().capitalize() for t in pokemon_types_input.split(',')]

    print("\n Estadísticas del Pokemon:")
    pokemon_stats = {
        "HP": int(input(" HP: ")),
        "Attack": int(input(" Attack: ")),
        "Defense": int(input(" Defense: ")),
        "Sp. Attack": int(input(" Sp. Attack: ")),
        "Sp. Defense": int(input(" Sp. Defense: ")),
        "Speed": int(input(" Speed: "))
    }

    # Retornamos el objeto siguiendo exactamente tu estructura JSON
    return {
        "name": {"english": pokemon_name},
        "level": pokemon_level,
        "type": pokemon_types_clean,
        "base": pokemon_stats
    }

# --- RUTINA 3: GUARDAR EN EL ARCHIVO ---
def save_new_pokemon_list(param_file_name, param_new_list):

    """Sobrescribe el archivo con la lista completa de pokémones."""
    with open(param_file_name, 'w', encoding='utf-8') as archivo:
        json.dump(param_new_list, archivo, indent=2, ensure_ascii=False)
    print(f"\n¡Archivo '{param_file_name}' ha sido actualizado correctamente.")

# --- FUNCIÓN PRINCIPAL (MAIN) ---
def manage_pokemon_main():

    pokemon_file_name = r"c:\publico\pokemon_list.json"
    
    # Paso 1: Importar existentes
    pokemons_loaded = Load_pokemons(pokemon_file_name)

    print(f"Se han cargado {len(pokemons_loaded)} pokemones.")

    # Paso 2: Obtener nueva información
    pokemon_new_data = request_new_pokemon()
    
    # Agregar el nuevo a la lista cargada
    pokemons_loaded.append(pokemon_new_data)

    # Paso 3: Guardar cambios
    save_new_pokemon_list(pokemon_file_name, pokemons_loaded)

manage_pokemon_main()

