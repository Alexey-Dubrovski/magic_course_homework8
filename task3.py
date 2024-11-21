# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.

class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return (
            f'Производитель — {self.brand}\n'
            f'Модель — {self.model}\n'
            f'Цена — {self.price}'
        )


class Laptop(Device):
    def __init__(self, brand, model, price, ram, storage):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def get_info(self):
        return (
            f'Производитель — {self.brand}\n'
            f'Модель — {self.model}\n'
            f'Цена — {self.price}\n'
            f'Оперативная память — {self.ram}\n'
            f'Объем памяти — {self.storage}'
        )


class Smartphone(Device):
    def __init__(
            self, brand, model, price,
            camera_megapixels, battery_capacity
            ):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    def get_info(self):
        return (
            f'Производитель — {self.brand}\n'
            f'Модель — {self.model}\n'
            f'Цена — {self.price}\n'
            f'Камера — {self.camera_megapixels}\n'
            f'Емкость батареи — {self.battery_capacity}'
        )


class Store:
    def __init__(self):
        self.device = []

    def add_device(self, device):
        self.device.append(device)

    def list_device(self):
        for device in self.device:
            print(device.get_info(), '\n')


store = Store()

laptop = Laptop("Motorolla", "Pip 1", 100, 16, 512)
# print(laptop.get_info(), '\n')
smartphone = Smartphone("Яблочко", "iЯблочко 11", 10000, 12, 1024)
# print(smartphone.get_info(), '\n')

store.add_device(laptop)
store.add_device(smartphone)
store.list_device()
