class Animal():
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def __str__(self):
        return self.get_str()


class Zebra(Animal):
    type = "common zebra"

    def __init__(self, name, age, type):
        self.type = type
        super().__init__(name, age)

    def get_type(self):
        return self.type

    def get_str(self):
        return " ".join([" Name is", self.get_name(), "\n",
                         "Age is", str(self.get_age()), "\n",
                         "Type is", self.get_type(), "\n",
                         "------------------------------------------------\n"])


class Dolphin(Animal):
    type = "common Dolfin"

    def __init__(self, name, age, type):
        self.type = type
        super().__init__(name, age)

    def get_type(self):
        return self.type

    def get_str(self):
        return " ".join([" Name is", self.get_name(), "\n",
                         "Age is", str(self.get_age()), "\n",
                         "Type is", self.get_type(), "\n",
                         "------------------------------------------------\n"])


if __name__ == "__main__":
    zebra = Zebra("Mona", 3, "African")
    print(zebra)
    dolphin = Dolphin("Dolphin", 5, "South")
    print(dolphin)

    
    
 Name is Mona 
 Age is 3 
 Type is African 
 ------------------------------------------------

 Name is Dolphin 
 Age is 5 
 Type is South 
 ------------------------------------------------
