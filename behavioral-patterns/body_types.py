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

class BodyDecorator(BodyType):
    def __init__(self, decorate):
        self._decorate = decorate

    def add_body_type(self):
        self._decorate.add_body_type()

class Spoiler(BodyDecorator):
    def __init__(self, decorate, spoiler):
        self._decorate = decorate
        self._spoiler = spoiler

    def add_body_type(self):
        BodyDecorator.add_body_type(self)
        self._add_spoiler()

    def _add_spoiler(self):
        print(f"\t-- {self._spoiler.title()} spoiler added")

class BodyColor(BodyDecorator):
    def __init__(self, decorate, color):
        self._decorate = decorate
        self._color = color

    def add_body_type(self):
        BodyDecorator.add_body_type(self)
        self._add_body_color()

    def _add_body_color(self):
        print(f"\t-- {self._color.title()} color added")
