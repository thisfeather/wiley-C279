# Python codes on animal class and inheritance

# your code here

class Animal:
    animal_name = ""
    number_of_legs = None
    category = ""
    have_visible_ears = None
    
    def __init__(self, aname, numoflegs, category, havevisears):
        self.animal_name = aname
        self.number_of_legs = numoflegs
        self.category = category
        self.have_visible_ears = havevisears
        
    def display_info(self):
        print("\nThese are attributes of:", self.animal_name)
        print("Number of legs:", self.number_of_legs)
        print("Category:", self.category)
        print("Have visible ears or not:", self.have_visible_ears)     

        
# Try intantiate three animal object:
monkey = Animal("Monkey", 2, "mammal", True)
lizard = Animal("Lizard", 4, "reptile", False)
eagle = Animal("Eagle", 2, "bird", False)

monkey.display_info()
lizard.display_info()
eagle.display_info()

