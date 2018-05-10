import unittest
import multiprocessing
import time
import importlib

import app.programs.hd
import app.programs.original


class TestPrograms(unittest.TestCase):

    def run_program(self, location, params=dict()):
        run_program = importlib.import_module(location).run
        self.process = multiprocessing.Process(target=run_program, args=(params,))
        self.process.start()
        time.sleep(0.2)
        self.process.terminate()

    def test_all_hd(self):
        for name, program in app.programs.hd.list.items():
            with self.subTest(program=name):
                self.run_program(program.location)

    def test_all_original(self):
        for name, program in app.programs.original.list.items():
            with self.subTest(program=name):
                self.run_program(program.location)
