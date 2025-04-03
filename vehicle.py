class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Engine started for {self.__class__.__name__}.")

    def __str__(self):
        return f"{self.__class__.__name__}: Max Speed={self.max_speed}, Fuel Type={self.fuel_type}"


class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        super().__init__(max_speed, fuel_type)
        self.wheel_count = wheel_count

    def check_tires(self):
        print(f"Checking tires for {self.__class__.__name__}. All {self.wheel_count} tires are in good condition.")


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        super().__init__(max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            print(f"Loaded {weight} kg of cargo into {self.__class__.__name__}.")
        else:
            print(f"Cargo capacity exceeded! Cannot load {weight} kg.")


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        super().__init__(max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity

    def board_passengers(self, passengers):
        if passengers <= self.passenger_capacity:
            print(f"Boarded {passengers} passengers into {self.__class__.__name__}.")
        else:
            print(f"Passenger capacity exceeded! Cannot board {passengers} passengers.")


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        # Вызываем конструкторы родительских классов через super()
        super().__init__(max_speed, fuel_type, wheel_count)  # Для WheeledVehicle
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)  # Явно вызываем CargoTransport
        self.max_weight = max_weight

    def reinforce_frame(self):
        print(f"Reinforcing frame for {self.__class__.__name__} to handle up to {self.max_weight} kg.")


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        super().__init__(max_speed, fuel_type)
        self.emission_level = emission_level

    def reduce_emission(self):
        print(f"Reducing emissions for {self.__class__.__name__} to {self.emission_level} level.")


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight, passenger_capacity, emission_level):
        # Вызываем конструкторы родительских классов через super()
        super().__init__(
            max_speed=max_speed,
            fuel_type=fuel_type,
            wheel_count=wheel_count,
            cargo_capacity=cargo_capacity,
            max_weight=max_weight
        )
        PassengerTransport.__init__(self, max_speed, fuel_type, passenger_capacity)  # Явно вызываем PassengerTransport
        EcoFriendlyVehicle.__init__(self, max_speed, fuel_type, emission_level)  # Явно вызываем EcoFriendlyVehicle

    def status(self):
        print("Hybrid Delivery Van Status:")
        print(f"- Max Speed: {self.max_speed}")
        print(f"- Fuel Type: {self.fuel_type}")
        print(f"- Wheel Count: {self.wheel_count}")
        print(f"- Cargo Capacity: {self.cargo_capacity} kg")
        print(f"- Max Weight: {self.max_weight} kg")
        print(f"- Passenger Capacity: {self.passenger_capacity}")
        print(f"- Emission Level: {self.emission_level}")


# Создание гибридного фургона
hybrid_van = HybridDeliveryVan(
    max_speed=120,
    fuel_type="Electric/Hybrid",
    wheel_count=4,
    cargo_capacity=1000,
    max_weight=2000,
    passenger_capacity=4,
    emission_level="Low"
)

# Проверка методов
hybrid_van.start_engine()
hybrid_van.check_tires()
hybrid_van.load_cargo(800)
hybrid_van.board_passengers(3)
hybrid_van.reinforce_frame()
hybrid_van.reduce_emission()
hybrid_van.status()

# Попытка загрузить слишком много груза или пассажиров
hybrid_van.load_cargo(1500)  # Превышение грузоподъемности
hybrid_van.board_passengers(5)  # Превышение вместимости пассажиров