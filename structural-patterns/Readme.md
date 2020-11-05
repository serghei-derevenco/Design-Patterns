# Laboratory work nr. 2
-----
# Topic: *Structural Design Patterns*
### Author: *Serghei Derevenco*
-----
## Objectives:
1. Study and understand the Structural Design Patterns;
2. Try to implement to the previous laboratory work some of those patterns;
3. Based on the previous point, implement atleast 3 structural design patterns in project;

## Description & Implementation
In this lab I've used the following structural design patterns to continue my 'bmw' application:  
* [Decorator](https://sourcemaking.com/design_patterns/decorator)
* [Bridge](https://sourcemaking.com/design_patterns/bridge)
* [Adapter](https://sourcemaking.com/design_patterns/adapter)  

Firstly, I used the [Decorator](https://sourcemaking.com/design_patterns/decorator) to attach new feautures to my body_types. Those features are spoiler and body_color. All the classes are stored in `body_types.py` file.  
Here is the exemple of implementation of the base Decorator class:  
```python
class BodyDecorator(BodyType):
    def __init__(self, decorate):
        self._decorate = decorate

    def add_body_type(self):
        self._decorate.add_body_type()
```
And the example of Concrete Decorator:
```python
class Spoiler(BodyDecorator):
    def __init__(self, decorate, spoiler):
        self._decorate = decorate
        self._spoiler = spoiler

    def add_body_type(self):
        BodyDecorator.add_body_type(self)
        self._add_spoiler()

    def _add_spoiler(self):
        print(f"\t-- {self._spoiler.title()} spoiler added")
```

Secondly, I've used the [Bridge](https://sourcemaking.com/design_patterns/bridge) to split my LoadCapacity class into two separate hierarchies - abstraction and implementation, to have posibility for independent developing them. So, this helped me to add some new features like getting the information about the tank volume and the trunk volume of the specified BMW model. All the code for this pattern is stored in `load_capacity.py` file, and the Abstraction interface - Factory, is located in `factories.py`.  
Below is the example of implementation of Abstraction interface:
```python
class Factory(ABC):
    def __init__(self, LoadCapacity):
        self.load_capacity = LoadCapacity
    @abstractmethod
    def add_parts(self):
        pass

    @abstractmethod
    def display_description(self):
        pass
```
And of course the Base and the Concrete implementation:  
```python
class LoadCapacity(ABC):
    @abstractmethod
    def load_items(self, items):
        pass


class TankCapacity(LoadCapacity):
    def load_items(self, tank_volume):
        print(f"- Car has a tank of volume - {tank_volume} liters")

```

Finnaly, I've used the [Adapter](https://sourcemaking.com/design_patterns/adapter) in the implementation of the foreign exhaust systems in my BMW models. My PowerfulAdapter allows classes work together that couldn't otherwise becuase of incompatible interfaces. All the code is stored in `exhaust_system.py` file.  
There is the implementation of Adapter:
```python3
class PowerfulAdapter(StandartExhaust):
    def __init__(self, name):
        super(PowerfulAdapter, self).__init__(name=name)
        self._powerful = PowerfulExhaust(name=name)

    def add_exhaust(self):
        return self._powerful.add_powerful_exhaust()
```
## Results  
Below you can see results, and the new feautures that was added:
```
Please select the model of BMW (m5 / x5 / grand turismo): m5
BMW M5
- Sedan body added
        -- Carbon spoiler added
        -- Black color added
- Petrol engine added
- Sedan body added
- Back wheel drive added
- Salon from alcantara added
- Akrapovic exhaust system added
- Car has a tank of volume - 68 liters
- Car has a trunk of volume - 530 liters

Please select the model of BMW (m5 / x5 / grand turismo): x5
BMW X5
- Suv body added
        -- Carbon spoiler added
        -- Red color added
- Petrol engine added
- Suv body added
- All-wheel drive added
- Salon from alcantara added
- Akrapovic exhaust system added
- Car has a tank of volume - 80 liters
- Car has a trunk of volume - 645 liters

Please select the model of BMW (m5 / x5 / grand turismo): grand turismo
BMW 5-series Grand Turismo
- Wagon body added
        -- Polimer spoiler added
        -- Blue color added
- Diesel engine added
- Wagon body added
- Front wheel drive added
- Salon added
- BMW exhaust system added
- Car has a tank of volume - 70 liters
- Car has a trunk of volume - 500 liters

```

-----
## To Use
* Firstly, clone this repository using [Git](https://git-scm.com) or download `.zip` archive with project.
* Secondly, if your OS is Windows, you will need to [install Python](https://realpython.com/installing-python/) language to be able to execute the project (In other types of OS [Python](https://www.python.org/) is installed by default).
* Finally, `cd` into the folder with project and run `python main.py` to start application.
