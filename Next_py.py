# creating a class of our favorite animal
# updating the code:
class Tiger:

    def __init__(self, name="no_name"):
        self.color = "brown"
        self._age = 0
        self._name = name
       # count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday_1(self):
        self._age += 1

    def get_age(self):
        return self._age


def __main__():
    # count_animals = 0  # numer of animals from this class
    Mirons_Tiger = Tiger("Miron")
    Shoham_Tiger = Tiger()
    print(Mirons_Tiger.get_name())
    print(Shoham_Tiger.get_name())
    Mirons_Tiger.set_name("Miron_2")
    Shoham_Tiger.set_name("Shoham")
    print(Mirons_Tiger.get_name())
    print(Shoham_Tiger.get_name())

    Mirons_Tiger.birthday_1()
    Mirons_Tiger.birthday_1()
    print(Mirons_Tiger.get_age())
    #print(count_animals)


__main__()


