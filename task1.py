# Создайте класс Employee, который инкапсулирует следующие данные:

# Приватные поля __name, __position, __salary.
# Методы set_name, set_position и set_salary для изменения значений
# этих полей (например, при повышении сотрудника).
# Ограничьте прямой доступ к __salary, добавив проверку,
# чтобы зарплату можно было изменить только через метод, например,
# при повышении. Запрещается устанавливать зарплату ниже текущего значения.

# Метод get_employee_info, который возвращает информацию о сотруднике в
# виде строки.

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def change_name(self, name):
        self.__name = name

    def change_position(self, position):
        self.__position = position

    def change_salary(self, salary):
        if salary > self.__salary:
            self.__salary = salary
        else:
            raise ValueError('Так дела не делаются')

    def get_employee_info(self):
        return f'Имя: {self.__name}\nДолжность: {self.__position}\nЗарплата: {self.__salary}'


name = "Андрюшка"
position = "Тестировщик"
salary = 90_000
emp = Employee(name, position, salary)
# print(emp.get_employee_info())

emp.change_position("Старший тестировщик")
emp.change_salary(120_000)
print(emp.get_employee_info())
