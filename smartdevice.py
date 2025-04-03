class Device:
    def __init__(self, power):
        self.power = power
    
    def turn_on(self):
        print("Device is turning on.")

class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        super().__init__(power)
        self.ip_address = ip_address
    
    def connect(self):
        print(f"Connecting to network at {self.ip_address}.")

class PortableDevice(Device):
    def __init__(self, power, battery_level):
        super().__init__(power)
        self.battery_level = battery_level
    
    def charge(self):
        print("Charging device.")

class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)
    
    def call(self):
        print("Making a phone call.")

# Демонстрация
phone = SmartPhone(10, "192.168.1.1", 80)
phone.turn_on()
phone.connect()
phone.charge()
phone.call()

# Решение проблемы алмаза: использование super() во всех конструкторах
class Device:
    def __init__(self, power):
        self.power = power
        print("Device initialized")
    
    def turn_on(self):
        print("Device is turning on.")

class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        super().__init__(power)
        self.ip_address = ip_address
        print("NetworkedDevice initialized")
    
    def connect(self):
        print(f"Connecting to network at {self.ip_address}.")

class PortableDevice(Device):
    def __init__(self, power, battery_level):
        super().__init__(power)
        self.battery_level = battery_level
        print("PortableDevice initialized")
    
    def charge(self):
        print("Charging device.")

class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        super().__init__(power)
        self.ip_address = ip_address
        self.battery_level = battery_level
        print("SmartPhone initialized")
    
    def call(self):
        print("Making a phone call.")

# Демонстрация правильного использования super()
print("\nUsing super() to resolve diamond problem:")
phone = SmartPhone(10, "192.168.1.1", 80)
phone.turn_on()
phone.connect()
phone.charge()
phone.call()
