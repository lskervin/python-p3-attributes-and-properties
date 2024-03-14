#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, breed="Beagle", name="Fido"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
        

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 25:
            self._name = new_name
        else:
            self._name = None 
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
        

    @breed.setter
    def breed(self, new_breed):
        if new_breed in APPROVED_BREEDS:
            self._breed = new_breed
        else:
            self._breed = None 
            print("Breed must be in list of approved breeds.")
            
        

fido = Dog('Beagle')
print(fido.name)

# print(fido.breed)