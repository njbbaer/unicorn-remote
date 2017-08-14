import unittest
import time

from app.state import state, ProgramNotFound


class TestState(unittest.TestCase):

    def tearDown(self):
        if state._process is not None:
            state._process.terminate()

    def test_start_all(self):
        programs= ["ascii_text", "cheertree", "cross", "demo", "dna", 
            "game_of_life", "matrix", "psychedelia", "rain", "rainbow", 
            "random_blinky", "random_sparkles", "simple", "snow", "trig"]
        for program in programs:
            with self.subTest(program=program):
                r = state.start_program(program)
                self.assertTrue(state._process.is_alive())

    def test_start_not_found(self):
        with self.assertRaises(ProgramNotFound):
            state.start_program("does_not_exist")

    def test_start_with_good_params(self):
        state.start_program("demo", {"brightness": 0.5, "rotation": 0})
        self.assertTrue(state._process.is_alive())

    def test_start_with_bad_brightness(self):
        with self.assertRaises(ValueError):
            state.start_program("demo", {"brightness": 1.1})

    def test_start_with_bad_rotation(self):
        with self.assertRaises(ValueError):
            state.start_program("demo", {"rotation": 91})

    def test_stop_program(self):
        state.start_program("demo")
        state.stop_program()
        time.sleep(0.1)
        self.assertFalse(state._process.is_alive())