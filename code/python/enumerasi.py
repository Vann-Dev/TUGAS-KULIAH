from enum import Enum

class Gender(Enum):
    Helicopter  = 1
    Male        = 2
    Female      = 3
    Car         = 4
    Terserah    = 5

print(Gender.Terserah.name)