from dataclasses import dataclass, field, asdict


def get_default_age():
    #the mean age in a dataset, so this could load a data set in with a parameter from pandas and then set default for
    #any missing nepersons we want to add in
    ages = [12, 34, 22, 59, 2]
    return sum(ages) // len(ages)


@dataclass
class NewPerson:
    name: str
    city: str = field(init=False, default="Amarillo")
    age: int #have to have the field one at the bottom or have them all as field
    is_senior: bool = field(init=False)

    def __post_init__(self):
        #A postinitialization function for working out if the person is a senior citizen or not
        if self.age >= 65:
            self.is_senior = True
        else:
            self.is_senior = False

p1 = NewPerson("Calum", 22)
p2 = NewPerson("Calum", 22)
print(p1)
print(p2)
print("Are the two data clusters equal? {}".format(p1==p2))
print(p1.is_senior)


"I wonder if I could use this with pandas, sort of create some data and then use pandas to load it in"

###Classes inside classes and a way of writing it as json format

import json

@dataclass
class Address:
    lat: int = 0
    long: int = 51
    city: str = "London"
    country: str = "United Kingdom"

@dataclass
class Person:
    name: str
    age: int
    addr: Address

address = Address()

p = Person("Calum", 22, address)
print(asdict(p))

#This appears as the same on mine but then it may come in useful with larder amounts of data.
print(json.dumps(asdict(p)))