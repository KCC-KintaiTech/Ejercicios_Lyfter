print("*** Python Intermedio - Ejercicio #1:  Calcular area de un circulo ***")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

input_radius = float(input("Enter the circle's radius: "))
my_circle = Circle(input_radius)
print("Area of the circle:", my_circle.area())  

print("*** Python Intermedio - Ejercicio #2:  Subir pasajeros de un bus si no esta lleno y Bajar los que estan en el bus ***")

class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger} subió al bus.")
        else:
            print("El bus está lleno.")

    def disembark_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger} bajó del bus.")
        else:
            print(f"{passenger} no está en el bus.")
            