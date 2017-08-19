import unittest
import multiprocessing
import time

import app.programs.original

class TestPrograms(unittest.TestCase):

    def program_helper(self, func, params=dict()):
        self.process = multiprocessing.Process(target=func, args=(params,))
        self.process.start()
        time.sleep(0.2)
        self.process.terminate()

    def test_ascii_text(self):
        self.program_helper(app.programs.original.ascii_text.run, { "text": "Hello World" }) 

    def test_cheertree(self):
        self.program_helper(app.programs.original.cheertree.run)

    def test_cross(self):
        self.program_helper(app.programs.original.cross.run)

    def test_demo(self):
        self.program_helper(app.programs.original.demo.run)

    def test_dna(self):
        self.program_helper(app.programs.original.dna.run)

    def test_game_of_life(self):
        self.program_helper(app.programs.original.game_of_life.run)

    def test_matrix(self):
        self.program_helper(app.programs.original.matrix.run)

    def test_psychedelia(self):
        self.program_helper(app.programs.original.psychedelia.run)

    def test_rain(self):
        self.program_helper(app.programs.original.rain.run)

    def test_rainbow(self):
        self.program_helper(app.programs.original.rainbow.run)

    def test_random_blinky(self):
        self.program_helper(app.programs.original.random_blinky.run)

    def test_random_sparkles(self):
        self.program_helper(app.programs.original.random_sparkles.run)

    def test_simple(self):
        self.program_helper(app.programs.original.simple.run)

    def test_snow(self):
        self.program_helper(app.programs.original.snow.run)

    def test_trig(self):
        self.program_helper(app.programs.original.trig.run)


if __name__ == '__main__':
    unittest.main()