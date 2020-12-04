from abc import ABC, abstractmethod


class Context:
    def __init__(self, brake_system):
        self._brake_system = brake_system

    def context_interface(self):
        self._brake_system.set()


class BrakeSystem(ABC):
    @abstractmethod
    def set(self):
        pass


class StandartBrake(BrakeSystem):
    def set(self):
        print("- Standart brake system setted")


class MBrake(BrakeSystem):
    def set(self):
        print("- BMW M Performance brake system setted")


class CarbonCeramicBrake(BrakeSystem):
    def set(self):
        print("- Carbon-ceramic sport brake system setted")