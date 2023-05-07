from pixels import Pixel
import time
import threading
import neopixel
import board
import random


class Display():
    def __init__(self, n):
        self.pixels = neopixel.NeoPixel(board.D18, n, auto_write=False)
        self.__smart_pixels = []
        self.current_act = ""
        self.action_happening = False
        for n, pixel in enumerate(self.pixels):
            self.__smart_pixels.append(Pixel(n, self))

    def update_screen(self):
        self.pixels.show()

    def fire(self, factor = 2, rate_of_decay = 400):
        self.action_happening = True
        copy_of_smart_pixels = list(self.__smart_pixels)
        to_decrement = []
        while self.current_act != "":
            for i in range(0, rate_of_decay):
                chosen_pixel = random.choice(copy_of_smart_pixels)
                chosen_pixel.set_colour(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
                if chosen_pixel in to_decrement:
                    to_decrement.remove(chosen_pixel)
                to_decrement.append(chosen_pixel)
            for smart_pixel in to_decrement:
                smart_pixel.set_colour(
                    self.__minimum(smart_pixel.get_colour()[0]-factor, 0),
                    self.__minimum(smart_pixel.get_colour()[1]-factor, 0),
                    self.__minimum(smart_pixel.get_colour()[2]-factor, 0)
                )
            time.sleep(0.02)
            self.update_screen()
        self.should_continue = True
        self.action_happening = False

    def __minimum(self, val, minimum_value):
        if val < minimum_value:
            return minimum_value
        else:
            return val

    def __maximum(self, val, maximum_value):
        if val > maximum_value:
            return maximum_value
        else:
            return val

    def set_colour_of_all(self, r, g, b):
        for smart_pixel in self.__smart_pixels:
            smart_pixel.set_colour(r, g, b)
        self.update_screen()

    def all_on(self):
        for smart_pixel in self.__smart_pixels:
            smart_pixel.set_colour(255, 255, 255)
        self.update_screen()

    def all_off(self):
        for smart_pixel in self.__smart_pixels:
            smart_pixel.off()
        self.update_screen()
