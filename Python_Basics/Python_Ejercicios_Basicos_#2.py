print("*** Ejercicio #2: Calcular etapa de vida de persona ***")
person_age = int(input("Digite los años cumplidos: "))
if (person_age <= 1):
    stage_of_life = "Bebé"
elif (person_age <= 8):
    stage_of_life = "Niñez"
elif (person_age <= 12):
    stage_of_life = "pre-adolescente"
elif (person_age <= 17):
    stage_of_life = "Adolescente"
elif (person_age <= 29):
    stage_of_life = "Adulto joven"
elif (person_age <= 64):
    stage_of_life = "Adulto"
else:
    stage_of_life = "Adulto mayor"
print("Esa edad corresponde a un ", stage_of_life)