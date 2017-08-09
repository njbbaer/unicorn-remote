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
        from app.programs.ascii_text import run
        self.program_helper(run, { "text": "Hello World" }) 

    def test_cheertree(self):
        from app.programs.cheertree import run
        self.program_helper(run)

    def test_cross(self):
        from app.programs.cross import run
        self.program_helper(run)

    def test_demo(self):
        from app.programs.demo import run
        self.program_helper(run)

    def test_dna(self):
        from app.programs.dna import run
        self.program_helper(run)

    def test_game_of_life(self):
        from app.programs.game_of_life import run
        self.program_helper(run)

    def test_dna(self):
        from app.programs.dna import run
        self.program_helper(run)

    def test_program_matrix(self):
        from app.programs.matrix import run
        self.program_helper(run)

    def test_psychedelia(self):
        from app.programs.psychedelia import run
        self.program_helper(run)

    def test_rain(self):
        from app.programs.rain import run
        self.program_helper(run)

    def test_rainbow(self):
        from app.programs.rainbow import run
        self.program_helper(run)

    def test_random_blinky(self):
        from app.programs.random_blinky import run
        self.program_helper(run)

    def test_random_sparkles(self):
        from app.programs.random_sparkles import run
        self.program_helper(run)

    def test_simple(self):
        from app.programs.simple import run
        self.program_helper(run)

    def test_snow(self):
        from app.programs.snow import run
        self.program_helper(run)

    def test_trig(self):
        from app.programs.trig import run
        self.program_helper(run)


if __name__ == '__main__':
    unittest.main()