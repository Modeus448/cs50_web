#ООП Повторення
class Flight():
    def __init__(self, capacity): #створення об'єкта з атрибутом місткості
        self.capacity = capacity #кількість місць на рейсі
        self.passengers = [] #список пасажирів, який починається порожнім

    def add_passenger(self, name):
        if not self.open_seats(): #перевіряємо чи є вільні місця
            return False
        self.passengers.append(name) #додаємо пасажира до списку
        return True

    def open_seats(self): #метод для визначення кількості вільних місць
        return self.capacity - len(self.passengers) #кількість вільних місць

flight = Flight(3) #ліміт пасажипів на рейсі

people = ["Harry", "Ron", "Hermione", "Draco"] #список пасажирів
for person in people: #зикл для перевірки місця для кожного пасажира
    success = flight.add_passenger(person) #додаємо пасажирів до рейсу
    if success:
        print(f"Added {person} to flaght successfully.")
    else:
        print(f"No available seats for {person}.")
