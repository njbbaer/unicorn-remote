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

    def start_all(self, list):
        for name, program in list.items():
            with self.subTest(program=name):
                self.run_program(program.location)

    def test_start_all_hd(self):
        self.start_all(app.programs.hd.list)

    def test_start_all_original(self):
        self.start_all(app.programs.original.list)
