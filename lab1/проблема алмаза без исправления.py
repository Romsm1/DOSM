class Device:
    def __init__(self, power):
        self.power = power
        print(f"Инициализация Device с мощностью {self.power}")

    def turn_on(self):
        print(f"Устройство включено. Мощность: {self.power}W")

class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        Device.__init__(self, power)
        self.ip_address = ip_address
        print(f"Инициализация NetworkedDevice с IP {self.ip_address}")

    def connect(self):
        print(f"Подключено к сети через {self.ip_address}")

class PortableDevice(Device):
    def __init__(self, power, battery_level):
        Device.__init__(self, power)
        self.battery_level = battery_level
        print(f"Инициализация PortableDevice с зарядом {self.battery_level}%")

    def charge(self):
        print(f"Зарядка ({self.battery_level}%)")

class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)
        print("Инициализация SmartPhone завершена")

    def call(self):
        print("Совершение звонка")

print("\n=== Тест проблемной версии ===")
problem_phone = SmartPhone(10, "192.168.1.1", 80)