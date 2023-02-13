# creating a class of our favorite animal
# updating the code:
# adding a class that creats a pixel
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
    pixel = Pixel(5, 6, 255)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()

    # count_animals = 0  # numer of animals from this class
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


main()



