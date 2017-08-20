import unittest
import multiprocessing
import time

import app.programs


class TestPrograms(unittest.TestCase):

    def run_program(self, func, params=dict()):
        self.process = multiprocessing.Process(target=func, args=(params,))
        self.process.start()
        time.sleep(0.2)
        self.process.terminate()

    def test_all_hd(self):
        for name, program in app.programs.hd.items():
            with self.subTest(program=name):
                self.run_program(program.run)

    def test_all_original(self):
        for name, program in app.programs.original.items():
            with self.subTest(program=name):
                self.run_program(program.run)