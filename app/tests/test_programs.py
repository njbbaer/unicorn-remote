import unittest
import multiprocessing
import time

import app.programs.hd
import app.programs.original


HD_PROGRAMS_LIST = ["candle", "demo", "forest_fire", "game_of_life", "rainbow", 
    "stars", "trig"]
ORIGINAL_PROGRAMS_LIST = ["ascii_text", "cheertree", "cross", "demo", "dna", 
    "game_of_life", "matrix", "psychedelia", "rain", "rainbow", 
    "random_blinky", "random_sparkles", "simple", "snow", "trig"]


class TestPrograms(unittest.TestCase):

    def run_program(self, func, params=dict()):
        self.process = multiprocessing.Process(target=func, args=(params,))
        self.process.start()
        time.sleep(0.2)
        self.process.terminate()

    def test_all_hd(self):
        for program in HD_PROGRAMS_LIST:
            with self.subTest(program=program):
                run = getattr(app.programs.hd, program).run
                self.run_program(run)

    def test_all_original(self):
        for program in ORIGINAL_PROGRAMS_LIST:
            with self.subTest(program=program):
                run = getattr(app.programs.original, program).run
                self.run_program(run)