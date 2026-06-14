print("*** Ejercicio #5:  Calcular materias ganadas y perdidas ***")
grades_total = int(input("Cuántas notas va a digitar? "))
grade_entered = 0
grade_counter = 1
grades_passed_qty = 0 
grades_failed_qty = 0
grades_passed_sum = 0
grades_failed_sum = 0
grades_all_qty = 0
grades_all_sum = 0
while (grade_counter<=grades_total):
    grade_entered = int(input(f"Digite Nota #{grade_counter} "))
    grades_all_qty = grades_all_qty + 1
    grades_all_sum = grades_all_sum + grade_entered
    if (grade_entered>=70):
        grades_passed_qty = grades_passed_qty + 1
        grades_passed_sum = grades_passed_sum + grade_entered
    else:
        grades_failed_qty = grades_failed_qty + 1
        grades_failed_sum = grades_failed_sum + grade_entered
    grade_counter = grade_counter + 1
print(f"La cantidad de Notas Aprobadas es {grades_passed_qty} cuyo promedio es {grades_passed_sum/grades_passed_qty}.")
print(f"La cantidad de Notas Perdidas es {grades_failed_qty} cuyo promedio es {grades_failed_sum/grades_failed_qty}.")
print(f"El promedio general es de {grades_all_sum/grades_all_qty}")