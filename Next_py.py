# creating a class of our favorite animal

class Tiger:

    def __init__(self):
        self.color = "brown"
        self.age = 0

    def birthday_1(self):
        self.age += 1

    def get_age(self):
        return self.age


def __main__():
    Mirons_Tiger = Tiger()
    Shoham_Tiger = Tiger()
    Mirons_Tiger.birthday_1()
    Mirons_Tiger.birthday_1()
    print(Mirons_Tiger.get_age())


__main__()


