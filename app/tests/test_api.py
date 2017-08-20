import unittest

from app import create_app
from app.state import state

import app.programs


class TestAPI(unittest.TestCase):
    
    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def tearDown(self):
        state.stop_program()

    def test_start_all_hd(self):
        state.set_model(is_hd=True)
        for name, _ in app.programs.hd.items():
            with self.subTest(program=name):
                r = self.app.put("/api/program/" + name)
                self.assertEqual(r.status_code, 200)

    def test_start_all_original(self):
        state.set_model(is_hd=False)
        for name, _ in app.programs.original.items():
            with self.subTest(program=name):
                r = self.app.put("/api/program/" + name)
                self.assertEqual(r.status_code, 200)

    def test_start_not_found(self):
        r = self.app.put("/api/program/does_not_exist")
        self.assertEqual(r.status_code, 404)

    def test_start_with_good_params(self):
        r = self.app.put("/api/program/demo?brightness=0.5&rotation=0")
        self.assertEqual(r.status_code, 200)

    def test_start_with_bad_brightness(self):
        r = self.app.put("/api/program/demo?brightness=1.1")
        self.assertEqual(r.status_code, 400)

    def test_start_with_bad_rotation(self):
        r = self.app.put("/api/program/demo?rotation=91")
        self.assertEqual(r.status_code, 400)

    def test_stop_program(self):
        r = self.app.delete("/api/program")
        self.assertEqual(r.status_code, 200)