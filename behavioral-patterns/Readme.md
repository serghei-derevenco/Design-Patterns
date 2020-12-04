# Laboratory work nr. 3
-----
# Topic: *Behavioral Design Patterns*
### Author: *Serghei Derevenco*
-----
## Objectives:
1. Study and understand the Behavioral Design Patterns;  
2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system;  
3. Implement some additional functionalities using behavioral design patterns;
## Description & Implementation
In this lab I've used the following design patterns for implementing some additional functionalities to my 'bmw' application:  
* [Strategy](https://sourcemaking.com/design_patterns/strategy)  

Firstly, I've implemented new feature - brake system, using Strategy pattern. So, now I have option to add to my cars the standart, the M Perfomance and the Carbon-Ceramic brake systems. [Strategy](https://sourcemaking.com/design_patterns/strategy) helped me to put each of them into separate classes and make their objects interchangeable. All the classes are stored in `brake_system.py` file.  
Here is the example of implementation of the Context class:  
```python
class Context:
    def __init__(self, brake_system):
        self._brake_system = brake_system

    def context_interface(self):
        self._brake_system.set()
```
And the code for Strategy class and its Concrete classes:  
```python
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
```
## Results  
Below you can see the output with new feature:
```
Please select the model of BMW (m5 / x5 / grand turismo): m5
BMW M5
- Sedan body added
        -- Carbon spoiler added
        -- Black color added
- Petrol engine added
*- Carbon-ceramic sport brake system setted
- Back wheel drive added
- Salon from alcantara added
- Akrapovic exhaust system added
- Car has a tank of volume - 68 liters
- Car has a trunk of volume - 530 liters

```
-----
## To Use
* Firstly, clone this repository using [Git](https://git-scm.com) or download `.zip` archive with project.
* Secondly, if your OS is Windows, you will need to [install Python](https://realpython.com/installing-python/) language to be able to execute the project (In other types of OS [Python](https://www.python.org/) is installed by default).
* Finally, `cd` into the folder with project and run `python main.py` to start application.
