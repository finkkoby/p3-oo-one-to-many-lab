class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner) and owner is not None:
            raise Exception
        self._owner = owner

    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception
        self._pet_type = pet_type

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        names = [pet for pet in self.pets()]
        return sorted(names, key=lambda pet: pet.name)