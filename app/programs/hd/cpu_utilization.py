import unicornhathd
import psutil
import time
import threading
import math

COLOR = [255, 255, 255]
FADE_RATE = 0.2

class Indicator:
    def __init__(self, position, dimensions, color):
        self.color = color
        self.dimensions = dimensions
        self.position = position
        self.current_intensity = 0

    def update(self, target_intensity):
        self.current_intensity += (target_intensity - self.current_intensity) * FADE_RATE
        self.current_intensity = min(self.current_intensity, 1)

        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                r = self.current_intensity * self.color[0]
                g = self.current_intensity * self.color[1]
                b = self.current_intensity * self.color[2]
                pixel_x = x + self.position[0]
                pixel_y = y + self.position[1]
                unicornhathd.set_pixel(pixel_x, pixel_y, r, g, b)

        unicornhathd.show()

class CPUUtil:
    def __init__(self):
        self.indicators = [
            Indicator([0, 0], [8, 8], COLOR),
            Indicator([0, 8], [8, 8], COLOR),
            Indicator([8, 0], [8, 8], COLOR),
            Indicator([8, 8], [8, 8], COLOR)]

    def update_util(self):
        self.cpu_percents = psutil.cpu_percent(percpu=True)

    def update_indicators(self):
        for indicator, cpu_percent in zip(self.indicators, self.cpu_percents):
            indicator.update(cpu_percent / 100)

def run(params):
    cpu = CPUUtil()
    while True:
        cpu.update_util()
        for i in range(10):
            cpu.update_indicators()