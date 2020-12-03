from abc import ABC, abstractmethod

from engines import *
from drive_types import *
from body_types import *
from salon import *
from car_load_capacity import *
from exhaust_system import *

class Factory(ABC):
    def __init__(self, LoadCapacity):
        self.load_capacity = LoadCapacity
    @abstractmethod
    def add_parts(self):
        pass

    @abstractmethod
    def display_description(self):
        pass

class Model(ABC):
    def __init__(self, car_model):
        self.car_model = car_model

    def show_model(self):
        print(self.car_model)

class M5(Factory):
    def __init__(self, Load_Capacity, items):
        super().__init__(Load_Capacity)
        self.items = items

    def add_parts(self):
        model = Model("BMW M5")
        model.show_model()
        engine = Petrol()
        body_type = Sedan()
        spoiler = Spoiler(body_type, "carbon")
        black_color = BodyColor(spoiler, "black")
        black_color.add_body_type()
        drive_type = BackWheelDrive()
        builder = SalonBuilder()
        salon = builder.create_salon()
        salon.add_alcantara()
        exhaust_system = PowerfulAdapter('Akrapovic')
        return engine.add_engine(), body_type.add_body_type(), drive_type.add_drive_type(), print(salon), exhaust_system.add_exhaust()

    def display_description(self):
        self.load_capacity.load_items(self.items)

class X5(Factory):
    def __init__(self, Load_Capacity, items):
        super().__init__(Load_Capacity)
        self.items = items

    def add_parts(self):
        model = Model("BMW X5")
        model.show_model()
        engine = Petrol()
        body_type = Suv()
        spoiler = Spoiler(body_type, "carbon")
        red_color = BodyColor(spoiler, "red")
        red_color.add_body_type()
        drive_type = AllWheelDrive()
        builder = SalonBuilder()
        salon = builder.create_salon()
        salon.add_alcantara()
        exhaust_system = PowerfulAdapter('Akrapovic')
        return engine.add_engine(), body_type.add_body_type(), drive_type.add_drive_type(), print(salon), exhaust_system.add_exhaust()

    def display_description(self):
        self.load_capacity.load_items(self.items)

class GrandTurismo(Factory):
    def __init__(self, Load_Capacity, items):
        super().__init__(Load_Capacity)
        self.items = items

    def add_parts(self):
        model = Model("BMW 5-series Grand Turismo")
        model.show_model()
        engine = Diesel()
        body_type = Wagon()
        spoiler = Spoiler(body_type, "polimer")
        blue_color = BodyColor(spoiler, "blue")
        blue_color.add_body_type()
        drive_type = FrontWheelDrive()
        builder = SalonBuilder()
        salon = builder.create_salon()
        salon.standart_salon()
        exhaust_system = StandartExhaust('BMW')
        return engine.add_engine(), body_type.add_body_type(), drive_type.add_drive_type(), print(salon), exhaust_system.add_exhaust()

    def display_description(self):
        self.load_capacity.load_items(self.items)

class BMWProducer:
    def create_bmw(self):
        tank_capacity = TankCapacity()
        trunk_capacity = TrunkCapacity()
        model = input("\nPlease select the model of BMW (m5 / x5 / grand turismo): ")
        while True:
            if model == "m5":
                return M5(tank_capacity, 0).add_parts(), M5(tank_capacity, 68).display_description(), M5(trunk_capacity, 530).display_description()
            elif model == "x5":
                return X5(tank_capacity, 0).add_parts(), X5(tank_capacity, 80).display_description(), X5(trunk_capacity, 645).display_description()
            elif model == "grand turismo":
                return GrandTurismo(tank_capacity, 0).add_parts(), GrandTurismo(tank_capacity, 70).display_description(), GrandTurismo(trunk_capacity, 500).display_description()
            elif model == 'quit':
                break
