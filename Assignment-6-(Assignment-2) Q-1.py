#Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"The name of the dog is {self.name}")
        print(f"The dog's age is {self.age}")

    def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}")

class Lebra(Dog):

    def weight(self, weight=16):
        self.weight = weight
        print(f"The weight of {self.name} is {self.weight} pounds")

    def life_span(self, lifespan = 15):
        self.lifespan = lifespan
        print(f"The lifespan of {self.name} is {self.lifespan} years")

class Pitbull(Dog):

    def __init__(self, name, age, coat_color="White",gender="Female"):
        super().__init__(name, age, coat_color)
        self.gender = gender

    def height(self, height=16):
        self.height = height
        print(f"The height of {self.name} is {self.height} inches")

    def bark(self, bark):
        self.bark = bark
        print(f"{self.name} is a {self.gender} and says {self.bark}")


scooby = Lebra("Scooby", 4, "White")
scooby.description()
scooby.get_info()
scooby.weight(9)
scooby.life_span()

print("-------------------------")

tiger = Lebra("Tiger", 9, "Brown")
tiger.description()
tiger.get_info()
tiger.weight()
tiger.life_span(18)

print("-------------------------")

don = Pitbull("Don", 18)
don.description()
don.get_info()
don.height(14)
don.bark("Woooofffyyyy!")

print("-------------------------")

rocky =Pitbull("Rocky", 7, "Yellow", "Male")
rocky.description()
rocky.get_info()
rocky.height(17)
rocky.bark("Woooofffyyyy !")