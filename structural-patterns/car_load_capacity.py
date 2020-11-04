from abc import ABC, abstractmethod

class LoadCapacity(ABC):
    @abstractmethod
    def load_items(self, items):
        pass


class TankCapacity(LoadCapacity):
    def load_items(self, tank_capacity):
        print(f"- Car has a tank of volume - {tank_capacity} liters")


class TrunkCapacity(LoadCapacity):
    def load_items(self, trunk_volume):
        print(f"- Car has a trunk of volume - {trunk_volume} liters")