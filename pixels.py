import time

class Pixel():
    def __init__(self, n, display):
        self.__pixel_location = n
        self.__display = display
        self.order = "GRB"

    def set_colour(self, r, g, b):
        new_col_as_list = []
        for colours in self.order:
            if colours == "R":
                new_col_as_list.append(r)
            elif colours == "G":
                new_col_as_list.append(g)
            elif colours == "B":
                new_col_as_list.append(b)
        self.__display.pixels[self.__pixel_location] = (
            new_col_as_list[0],
            new_col_as_list[1],
            new_col_as_list[2]
        )

    def get_colour(self):
        new_col_as_list = []
        (r, g, b) = self.__display.pixels[self.__pixel_location]
        for colours in self.order:
            if colours == "R":
                new_col_as_list.append(r)
            elif colours == "G":
                new_col_as_list.append(g)
            elif colours == "B":
                new_col_as_list.append(b)
        return (new_col_as_list[0], new_col_as_list[1], new_col_as_list[2])

    def off(self):
        self.set_colour(0, 0, 0)
