from abc import ABC, abstractmethod

class BodyType(ABC):
    @abstractmethod
    def add_body_type(self):
        pass

class Sedan(BodyType):
    def add_body_type(self):
        print("- Sedan body added")

class Suv(BodyType):
    def add_body_type(self):
        print("- Suv body added")

class Wagon(BodyType):
    def add_body_type(self):
        print("- Wagon body added")