from displays import Display
import time
import logging
import threading
import requests
import datetime
# If you have problems importing board,
# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/issues/55

now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"), "- started")

class LightSystem():
    def __init__(self):
        self.display = Display(500)
        self.interval = 0.5
        self.cycle()
        self.current_act = ""
        self.prev_act = "nowt"
        self.config = self.render_text()
        self.main()

    def cycle(self):
        # test all colours
        interval = 1
        self.display.set_colour_of_all(255, 0, 0)
        time.sleep(interval)
        self.display.set_colour_of_all(0, 255, 0)
        time.sleep(interval)
        self.display.set_colour_of_all(0, 0, 255)
        time.sleep(interval)
        self.display.set_colour_of_all(0, 0, 0)

    def render_text(self):
        config = []
        file_nm = "config.txt"
        with open(file_nm) as file:
            lines = file.readlines()
            for x, line in enumerate(lines):
                line = line.replace("\n", "")
                if line.endswith(":"):
                    opt = {
                        "start_hh" : int(line[0:2]),
                        "end_hh" : int(line[3:5]),
                        "action" : lines[x+1].replace(" ", "").replace("\n", "")
                    }
                    config.append(opt)
        now = datetime.datetime.now()
        print(now.strftime("%d/%m/%Y %H:%M:%S"), "- config loaded:", config)
        return config

    def main(self):
        while True:
            self.check_all()
            time.sleep(self.interval)

    def check_all(self):
        something_valid = False
        for time_set in self.config:
            valid = (
                datetime.datetime.now().hour >= time_set["start_hh"]
                and datetime.datetime.now().hour <= time_set["end_hh"]
            )
            if valid:
                self.current_act = time_set["action"]
                something_valid = True
        if not something_valid:
            self.current_act = ""
        self.display.current_act = self.current_act

        now = datetime.datetime.now()

        # if lights should be on and weren't previously
        if self.current_act != "" and self.prev_act == "":
            print(now.strftime("%d/%m/%Y %H:%M:%S"), "- turning on fire")
            threading.Thread(target=self.display.fire).start()

        # if lights should be off and weren't previously
        if self.current_act == "" and self.prev_act != "":
            print(now.strftime("%d/%m/%Y %H:%M:%S"), "- turning off")
            self.display.set_colour_of_all(0, 0, 0)
            self.display.current_act = ""

        self.prev_act = self.current_act


light_system = LightSystem()





