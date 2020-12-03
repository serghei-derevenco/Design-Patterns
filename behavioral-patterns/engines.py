from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def add_engine(self):
        pass

class Diesel(Engine):
    def add_engine(self):
        print("- Diesel engine added")

class Petrol(Engine):
    def add_engine(self):
        print("- Petrol engine added")

# Prototype pattern implementation
# from copy import deepcopy
#
# class Engine(ABC):
#     def add_engine(self):
#         pass
#
# class StandartEngine(Engine):
#     def __init__(self, volume="3.0l", horse_power="300 HP", fuel_type="diesel"):
#         self.volume = volume
#         self.horse_power = horse_power
#         self.fuel_type = fuel_type
#
#     def clone(self):
#         return deepcopy(self)
#
#     def add_engine(self):
#         print("- Engine added: " + self.volume + ", " + self.horse_power + ", " + self.fuel_type)
#
# class PowerfulEngine(Engine):
#     def __init__(self, volume="4.4l", horse_power="600 HP", fuel_type="petrol"):
#         self.volume = volume
#         self.horse_power = horse_power
#         self.fuel_type = fuel_type
#
#     def clone(self):
#         return deepcopy(self)
#
#     def add_engine(self):
#         print("- Engine added: " + self.volume + ", " + self.horse_power + ", " + self.fuel_type)