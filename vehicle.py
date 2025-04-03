class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def start_engine(self):
        return "Engine started"


class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        super().__init__(max_speed, fuel_type)
        self.wheel_count = wheel_count

    def check_tires(self):
        return "Tires checked"


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        super().__init__(max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        return "Cargo loaded"


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        super().__init__(max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity

    def board_passengers(self):
        return "Passengers boarded"


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        WheeledVehicle.__init__(self, max_speed, fuel_type, wheel_count)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        self.max_weight = max_weight

    def reinforce_frame(self):
        return "Frame reinforced"


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        super().__init__(max_speed, fuel_type)
        self.emission_level = emission_level

    def reduce_emission(self):
        return "Emissions reduced"


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight, passenger_capacity,
                 emission_level):
        Vehicle.__init__(self, max_speed, fuel_type)  # Инициализируем базовый класс напрямую
        WheeledVehicle.__init__(self, max_speed, fuel_type, wheel_count)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        PassengerTransport.__init__(self, max_speed, fuel_type, passenger_capacity)
        EcoFriendlyVehicle.__init__(self, max_speed, fuel_type, emission_level)
        self.max_weight = max_weight

    def status(self):
        return (f"Speed: {self.max_speed}, Fuel: {self.fuel_type}, Cargo: {self.cargo_capacity}kg, "
                f"Passengers: {self.passenger_capacity}, Emissions: {self.emission_level}")


# Пример использования:
van = HybridDeliveryVan(120, "Electric", 4, 2000, 5000, 6, "Low")
print(van.start_engine())
print(van.load_cargo())
print(van.board_passengers())
print(van.reinforce_frame())
print(van.reduce_emission())
print(van.status())
