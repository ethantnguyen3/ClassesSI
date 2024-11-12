class AnimalData:
    def __init__(self):
        self.full_name = ''
        self.age_years = 0

    def set_name(self, given_name):
        self.full_name = given_name

    def set_age(self, num_years):
        self.age_years = num_years

    

    def print_all(self):
        print(f'Name: {self.full_name}')
        print(f'Age: {self.age_years}')


class PetData(AnimalData):
    def __init__(self):
        AnimalData.__init__(self)
        self.id_num = 0

    def set_id(self, pet_id):
        self.id_num = pet_id

    # FIXME: Add print_all() member method
    def print_all(self):
        AnimalData.print_all(self)
        print(f'ID: {self.id_num}')

user_pet = PetData()
user_pet.set_name('Spot')
user_pet.set_age(5)
user_pet.set_id(8743)
user_pet.print_all() 

animal = AnimalData() 
animal.set_name('Raven')
animal.set_age(12)  
animal.set_id(1327)
