class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Двигатель запущен.")

    def __str__(self):
        return f"Макс. скорость={self.max_speed}, Тип топлива={self.fuel_type}"


class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        Vehicle.__init__(self, max_speed, fuel_type)  # Явный вызов конструктора Vehicle
        self.wheel_count = wheel_count

    def check_tires(self):
        print(f"Проверка шин. Все {self.wheel_count} шин в хорошем состоянии.")


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)  # Явный вызов конструктора Vehicle
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            print(f"Загружено {weight} кг груза.")
        else:
            print(f"Превышена грузоподъемность! Невозможно загрузить {weight} кг.")


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)  # Явный вызов конструктора Vehicle
        self.passenger_capacity = passenger_capacity

    def board_passengers(self, passengers):
        if passengers <= self.passenger_capacity:
            print(f"Посадили {passengers} пассажиров.")
        else:
            print(f"Превышена вместимость! Невозможно посадить {passengers} пассажиров.")


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        # Явный вызов конструкторов родительских классов
        WheeledVehicle.__init__(self, max_speed, fuel_type, wheel_count)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        self.max_weight = max_weight

    def reinforce_frame(self):
        print(f"Усиление рамы для нагрузки до {self.max_weight} кг.")


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        Vehicle.__init__(self, max_speed, fuel_type)  # Явный вызов конструктора Vehicle
        self.emission_level = emission_level

    def reduce_emission(self):
        print(f"Снижение выбросов до уровня {self.emission_level}.")


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight, passenger_capacity, emission_level):
        # Явный вызов конструкторов родительских классов
        HeavyDutyVehicle.__init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight)
        PassengerTransport.__init__(self, max_speed, fuel_type, passenger_capacity)
        EcoFriendlyVehicle.__init__(self, max_speed, fuel_type, emission_level)

    def status(self):
        # Статус в одну строку
        print(
            f"Гибридный фургон: скорость={self.max_speed}, топливо={self.fuel_type}, колеса={self.wheel_count}, "
            f"грузоподъемность={self.cargo_capacity}кг, макс. вес={self.max_weight}кг, "
            f"пассажиры={self.passenger_capacity}, выбросы={self.emission_level}."
        )


# Создание гибридного фургона
hybrid_van = HybridDeliveryVan(
    max_speed=120,
    fuel_type="Электро/Гибрид",
    wheel_count=4,
    cargo_capacity=1000,
    max_weight=2000,
    passenger_capacity=4,
    emission_level="Низкий"
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