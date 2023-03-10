# creating classes according to ex. 2.4
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


"""
_x - x coordinate
_y - y coordinate
_red - a value between 0 and 255
_green - a value between 0 and 255
_blue - a value between 0 and 255
"""


class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        mean_color = (self._red + self._green + self._blue)/3
        self._red = int(mean_color)
        self._green = int(mean_color)
        self._blue = int(mean_color)

    def print_pixel_info(self):
        add_color = "0"
        print(add_color)
        if self._red == 0 & self._blue == 0 & self._green > 49:
            add_color = "Green"
        if self._red == 0 & self._green == 0 & self._blue > 49:
            add_color = "Blue"
        if self._blue == 0 & self._green == 0 & self._red > 49:
            add_color = "Red"
        print(f"X:{self._x}, Y:{self._y} , Color:{self._red, self._green, self._blue}")


def main():
    print("\nPixel class:")
    pixel = Pixel(5, 6, 255)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()

    print("\nTiger class:")
    miron_tiger = Tiger("Miron")
    shoham_tiger = Tiger()
    print(miron_tiger.get_name())
    print(shoham_tiger.get_name())
    miron_tiger.set_name("Miron_2")
    shoham_tiger.set_name("Shoham")
    print(miron_tiger.get_name())
    print(shoham_tiger.get_name())
    miron_tiger.birthday_1()
    miron_tiger.birthday_1()
    print(miron_tiger.get_age())

    print("\nBigThing class:")
    my_thing = BigThing("balloon")
    my_thing.size()
    print("\nBigCat class:")
    cutie = BigCat("mitzy", 22)
    cutie.size()


class BigThing:

    def __init__(self, thing):
        self.thing = thing

    def size(self):
        if isinstance(self.thing, int):
            print(self.thing)
        else:
            print(len(self.thing))


class BigCat (BigThing):
    def __init__(self, thing, weight=0):
        self.weight = weight

    def size(self):
        if self.weight > 20:
            print("Very Fat")
        elif self.weight > 15:
            print(" Fat")
        else:
            print("OK")



main()



