from dataclasses import dataclass


@dataclass
class NewPerson:
    name: str
    age: int
    city: str

p1 = NewPerson("Calum", 22, "Sheffield")
p2 = NewPerson("Calum", 22, "Sheffield")
print(p1)
print(p2)
print("Are the two data clusters equal? {}".format(p1==p2))


"I wonder if I could use this with pandas, sort of create some data and then use pandas to load it in"