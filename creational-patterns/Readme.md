# Laboratory work nr. 1
-----
# Topic: *Creational Design Patterns*
### Author: *Serghei Derevenco*
-----
## Objectives:
1. Study and understand the Creational Design Patterns;
2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms;
3. Based on the previous point, implement atleast 3 creational design patterns in project;
>I've used 3 design patterns - [Factory Method](https://sourcemaking.com/design_patterns/factory_method), [Abstract Factory](https://sourcemaking.com/design_patterns/abstract_factory) and [Builder](https://sourcemaking.com/design_patterns/builder).  
>Below is the description of project.


## Description & Implementation
In this project I used the BMW 5-series building domain area. Where will be a factory named Factory which will have possibilities to build 3 types of cars: 
* BMW M5 
* BMW X5 
* BMW 5-series Grand Turismo   

I collect cars from the following auto parts: body, engine, drive type, salon. Those parts I collect separately using design patterns.  
For the engine, body and drive type I used the [Factory Method](https://sourcemaking.com/design_patterns/factory_method) that allows an interface or a class to create an object, but let subclasses decide which class or object to instantiate. All the parts have separate interface to inherit and to use its methods in their product classes. Here is one example:

```python
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
```
For the salon I used the [Builder pattern](https://sourcemaking.com/design_patterns/builder), which is especially useful when you need to create an object with lots of possible configuration options. It helps me to collect salon parts: front panel, seats into one. And has the option to add material for the salon (like alcantara).

```python
"""The Director, creating a customised product."""
class SalonBuilder(Builder):
    def add_front_panel(self):
        return FrontPanel()

    def add_seats(self):
        return Seats()

    def create_salon(self):
        front_panel = self.add_front_panel()
        seats = self.add_seats()
        return Salon(front_panel, seats)
```
Finally, all of this factories I collect using [Abstract Factory](https://sourcemaking.com/design_patterns/abstract_factory) that allows you to produce the families of related objects without specifying their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type of many objects. 

```python
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
```
## Results
So, every time I create a car, I will be asked to select model (m5/x5/grand turismo), after that I will get car with its parameters, collected with help of creational design patterns.

```
Please select the model of BMW (m5 / x5 / grand turismo): m5
BMW M5
- Petrol engine added
- Sedan body added
- Back wheel drive added
- Salon from alcantara added

Please select the model of BMW (m5 / x5 / grand turismo): x5
BMW X5
- Petrol engine added
- Suv body added
- All-wheel drive added
- Salon from alcantara added

Please select the model of BMW (m5 / x5 / grand turismo): grand turismo
BMW 5-series Grand Turismo
- Diesel engine added
- Wagon body added
- Front wheel drive added
- Salon added

```
-----
## To Use
* Firstly, clone this repository using [Git](https://git-scm.com) or download `.zip` archive with project.
* Secondly, if your OS is Windows, you will need to [install Python](https://realpython.com/installing-python/) language to be able to execute the project (In other types of OS [Python](https://www.python.org/) is installed by default).
* Finally, `cd` into the folder with project and run `python main.py` to start application.
