from abc import ABC


class StandartExhaust(ABC):
    def __init__(self, name):
        self._name = name

    def add_exhaust(self):
        print(f"- {self._name} exhaust system added")


class PowerfulExhaust(ABC):
    def __init__(self, name):
        self._name = name

    def add_powerful_exhaust(self):
        print(f"- {self._name} exhaust system added")


class PowerfulAdapter(StandartExhaust):
    def __init__(self, name):
        super(PowerfulAdapter, self).__init__(name=name)
        self._powerful = PowerfulExhaust(name=name)

    def add_exhaust(self):
        return self._powerful.add_powerful_exhaust()
