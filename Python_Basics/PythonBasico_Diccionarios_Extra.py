print("*** Ejercicio #1:  Ventas por Articulo ***")
sales_ticket = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
item_sales_summary = {}
for sales_row in sales_ticket:
    for product in sales_row['items']:
        item_code = product.get('upc','Sin código')
        item_price = product.get('unit_price',0)
        if item_code in item_sales_summary:
            item_sales_summary[item_code] = item_sales_summary[item_code] + item_price
        else:
            item_sales_summary[item_code] = item_price
print(item_sales_summary)

print("---------------------------------------------------")
print("*** Ejercicio #2:  Agrupar Empleados por Departamento ***")
employees_data = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
employees_department = {}
for employee_individual in employees_data:
    department_name = employee_individual.get('department',"Not assigned yet")
    if department_name not in employees_department:
        employees_department[department_name] = []
    employees_department[department_name].append(employee_individual)
print(employees_department)

print("---------------------------------------------------")
print("*** Ejercicio #3:  Totales por Categoria ***")
products_catalog = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
category_summary = {}
for product_row in products_catalog:
    product_category = product_row.get('category','No categorizado')
    product_price = product_row.get('price',0)
    if product_category not in category_summary:
        category_summary[product_category] = product_price
    else:
        category_summary[product_category] = category_summary[product_category] + product_price
print(category_summary)