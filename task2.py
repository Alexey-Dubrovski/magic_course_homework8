# Создайте класс Vehicle, представляющий транспортное средство.
# Этот класс должен содержать:

# Поля make, model и year.
# Метод get_info, возвращающий строку с информацией о транспортном средстве.

# Затем создайте подклассы Car и Motorcycle, которые расширяют класс Vehicle:
# Класс Car должен иметь поле number_of_doors и метод get_info,
# который добавляет информацию о количестве дверей.
# Класс Motorcycle должен иметь поле has_sidecar (True или False)
# и метод get_info, который указывает, есть ли у мотоцикла коляска.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return (
            f'Производитель: {self.make}\nМодель: {self.model}\n'
            f'Год выпуска: {self.year}'
            )


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return (
            f'Производитель: {self.make}\nМодель: {self.model}\n'
            f'Год выпуска: {self.year}\n'
            f'Количество дверей: {self.number_of_doors}'
            )


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        if self.has_sidecar:
            return (
                f'Производитель: {self.make}\nМодель: {self.model}\n'
                f'Год выпуска: {self.year}\nС коляской: Да'
                )
        else:
            return (
                f'Производитель: {self.make}\nМодель: {self.model}\n'
                f'Год выпуска: {self.year}\nС коляской: Нет'
                )


car = Car("Жига", "2107", 1987, 4)
print(car.get_info(), '\n')

motorcycle = Motorcycle("Урал", "М-66", 1975, True)
print(motorcycle.get_info(), '\n')

motorcycle = Motorcycle("Урал", "М-66", 1975, False)
print(motorcycle.get_info(), '\n')
