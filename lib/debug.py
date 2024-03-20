#!usr/bin/env python3
from owner_pet import Owner
from owner_pet import Pet
import ipdb

owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
ipdb.set_trace()
