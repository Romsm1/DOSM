class Device:
    def __init__(self, power):
        self.power = power
        print(f"Инициализация Device с мощностью {self.power}")

    def turn_on(self):
        print(f"Базовое включение. Мощность: {self.power}W")

class NetworkedDevice(Device):
    def __init__(self, power, ip_address, **kwargs):
        super().__init__(power, **kwargs)
        self.ip_address = ip_address
        print(f"Инициализация NetworkedDevice с IP {self.ip_address}")

    def connect(self):
        print(f"Сетевое подключение: {self.ip_address}")

class PortableDevice(Device):
    def __init__(self, power, battery_level, **kwargs):
        super().__init__(power, **kwargs)
        self.battery_level = battery_level
        print(f"Инициализация PortableDevice. Заряд: {self.battery_level}%")

    def charge(self):
        print(f"Процесс зарядки ({self.battery_level}%)")

class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        super().__init__(power=power, ip_address=ip_address, battery_level=battery_level)
        print("Инициализация SmartPhone завершена")

    def turn_on(self):
        print("=== Процесс включения ===")
        super().turn_on()
        print("Дополнительные системы активированы")

    def call(self):
        print("🔊 Совершение звонка")

print("\n=== Тест исправленной версии ===")
good_phone = SmartPhone(15, "192.168.1.2", 85)
good_phone.turn_on()
good_phone.call()
