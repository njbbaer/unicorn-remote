import unittest
import multiprocessing
import time


class TestPrograms(unittest.TestCase):

    def program_helper(self, func, params=dict()):
        self.process = multiprocessing.Process(target=func, args=(params,))
        self.process.start()
        time.sleep(1)
        self.process.terminate()

    def test_program_ascii_text(self):
        from programs.ascii_text import run
        self.program_helper(run, { "text": "Hello World" }) 

    def test_cheertree(self):
        from programs.cheertree import run
        self.program_helper(run)

    def test_crss(self):
        from programs.cross import run
        self.program_helper(run)

    def test_demo(self):
        from programs.demo import run
        self.program_helper(run)

    def test_dna(self):
        from programs.dna import run
        self.program_helper(run)

    def test_game_of_life(self):
        from programs.game_of_life import run
        self.program_helper(run)

    def test_dna(self):
        from programs.dna import run
        self.program_helper(run)

    def test_program_matrix(self):
        from programs.matrix import run
        self.program_helper(run)

    def test_psychedelia(self):
        from programs.psychedelia import run
        self.program_helper(run)

    def test_rain(self):
        from programs.rain import run
        self.program_helper(run)

    def test_rainbow(self):
        from programs.rainbow import run
        self.program_helper(run)

    def test_random_blinky(self):
        from programs.random_blinky import run
        self.program_helper(run)

    def test_random_sparkles(self):
        from programs.random_sparkles import run
        self.program_helper(run)

    def test_simple(self):
        from programs.simple import run
        self.program_helper(run)

    def test_snow(self):
        from programs.snow import run
        self.program_helper(run)

    def test_trig(self):
        from programs.trig import run
        self.program_helper(run)


if __name__ == '__main__':
    unittest.main()