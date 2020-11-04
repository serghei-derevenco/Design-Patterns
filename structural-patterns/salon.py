from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def add_front_panel(self):
        raise NotImplementedError()

    @abstractmethod
    def add_seats(self):
        raise NotImplementedError()

    @abstractmethod
    def create_salon(self):
        raise NotImplementedError()

class Salon(ABC):
    def __init__(self, front_panel, seats):
        self.alcantara = False
        self.front_panel =front_panel
        self.seats = seats

    def add_alcantara(self):
        self.alcantara = True

    def standart_salon(self):
        self.alcantara = False

    def __str__(self):
        if self.alcantara == True:
            return "- Salon from alcantara added"
        else:
            return "- Salon added"

class FrontPanel(object):
    """Front Panel"""

class Seats(object):
    """Seats"""

class SalonBuilder(Builder):
    def add_front_panel(self):
        return FrontPanel()

    def add_seats(self):
        return Seats()

    def create_salon(self):
        front_panel = self.add_front_panel()
        seats = self.add_seats()
        return Salon(front_panel, seats)

builder = SalonBuilder().create_salon()
salon = builder.standart_salon()