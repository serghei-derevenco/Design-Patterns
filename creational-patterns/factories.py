from abc import ABC, abstractmethod
from engines import *
from drive_types import *
from body_types import *
from salon import *

class Factory(ABC):
    @abstractmethod
    def add_parts(self):
        pass

class Model(ABC):
    def __init__(self, car_model):
        self.car_model = car_model

    def __str__(self):
        return self.car_model

class M5(Factory):
    def add_parts(self):
        model = Model("BMW M5")
        engine = Petrol()
        body_type = Sedan()
        drive_type = BackWheelDrive()
        builder = SalonBuilder()
        salon = builder.create_salon()
        salon.add_alcantara()
        return print(model), engine.add_engine(), body_type.add_body_type(), drive_type.add_drive_type(), print(salon)

class X5(Factory):
    def add_parts(self):
        model = Model("BMW X5")
        engine = Petrol()
        body_type = Suv()
        drive_type = AllWheelDrive()
        builder = SalonBuilder()
        salon = builder.create_salon()
        salon.add_alcantara()
        return print(model), engine.add_engine(), body_type.add_body_type(), drive_type.add_drive_type(), print(salon)

class GrandTurismo(Factory):
    def add_parts(self):
        model = Model("BMW 5-series Grand Turismo")
        engine = Diesel()
        body_type = Wagon()
        drive_type = FrontWheelDrive()
        builder = SalonBuilder()
        salon = builder.create_salon()
        salon.standart_salon()
        return print(model), engine.add_engine(), body_type.add_body_type(), drive_type.add_drive_type(), print(salon)

class BMWProducer:
    def create_bmw(self):
        model = input("\nPlease select the model of BMW (m5 / x5 / grand turismo): ")
        while True:
            if model == "m5":
                return M5().add_parts()
            elif model == "x5":
                return X5().add_parts()
            elif model == "grand turismo":
                return GrandTurismo().add_parts()