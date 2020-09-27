# Creational Design Patterns

>I've used 3 design patterns - [Factory Method](https://sourcemaking.com/design_patterns/factory_method), [Abstract Factory](https://sourcemaking.com/design_patterns/abstract_factory) and [Builder](https://sourcemaking.com/design_patterns/builder).  
>Below is the description of project.

## Descriprion
In this project I used the BMW 5-series building domain area. Where will be a factory named Factory which will have possibilities to build 3 types of cars: 
* BMW M5 
* BMW X5 
* BMW 5-series Grand Turismo   

I collect cars from the following auto parts: body, engine, drive type, salon.   
Those parts I collect separately using design patterns. For the engine, body and drive type I used the [Factory Method](https://sourcemaking.com/design_patterns/factory_method). They all have separate interface to inherit and to use its methods in their product classes.   
For the salon I used the [Builder](https://sourcemaking.com/design_patterns/builder), which helps me to collect salon parts: front panel, seats into one. And has the option to add material for the salon (like alcantara).  
Finally, all of this factories I collect using [Abstract Factory](https://sourcemaking.com/design_patterns/abstract_factory). And every time I create a car, I will be asked to select model (m5/x5/grand turismo), after that I will get car with its parameters.

## To Use
* Firstly, clone this repository using [Git](https://git-scm.com) or download `.zip` archive with project.
* Secondly, if your OS is Windows, you will need to [install Python](https://realpython.com/installing-python/) language to be able to execute the project (In other types of OS [Python](https://www.python.org/) is installed by default).
* Finally, `cd` into the folder with project and run `python main.py` to start application.
