import unittest
import multiprocessing
import time

import app.programs

class TestPrograms(unittest.TestCase):

    def program_helper(self, func, params=dict()):
        self.process = multiprocessing.Process(target=func, args=(params,))
        self.process.start()
        time.sleep(0.2)
        self.process.terminate()

    def test_ascii_text(self):
        self.program_helper(app.programs.ascii_text.run, { "text": "Hello World" }) 

    def test_cheertree(self):
        self.program_helper(app.programs.cheertree.run)

    def test_cross(self):
        self.program_helper(app.programs.cross.run)

    def test_demo(self):
        self.program_helper(app.programs.demo.run)

    def test_dna(self):
        self.program_helper(app.programs.dna.run)

    def test_game_of_life(self):
        self.program_helper(app.programs.game_of_life.run)

    def test_matrix(self):
        self.program_helper(app.programs.matrix.run)

    def test_psychedelia(self):
        self.program_helper(app.programs.psychedelia.run)

    def test_rain(self):
        self.program_helper(app.programs.rain.run)

    def test_rainbow(self):
        self.program_helper(app.programs.rainbow.run)

    def test_random_blinky(self):
        self.program_helper(app.programs.random_blinky.run)

    def test_random_sparkles(self):
        self.program_helper(app.programs.random_sparkles.run)

    def test_simple(self):
        self.program_helper(app.programs.simple.run)

    def test_snow(self):
        self.program_helper(app.programs.snow.run)

    def test_trig(self):
        self.program_helper(app.programs.trig.run)


if __name__ == '__main__':
    unittest.main()