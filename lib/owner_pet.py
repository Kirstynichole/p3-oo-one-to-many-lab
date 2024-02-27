class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_to_list()

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Invalid pet type!")
        self._pet_type = pet_type

    def add_to_list(self):
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.get_sorted_pets()
    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                owner_pets.append(pet)
        return owner_pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("Invalid pet type!")
        
    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets

owner = Owner("Ben")
owner2 = Owner("Kirstyn")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Cairo", "dog", owner2)

