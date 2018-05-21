import unittest
import time

from app import create_app
from app.state import state

import app.programs.hd
import app.programs.original


class TestAPI(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def tearDown(self):
        state.stop_program()

    def start_all(self, list):
        for name, _ in list.items():
            with self.subTest(program=name):
                r = self.app.put("/api/program/" + name)
                self.assertEqual(r.status_code, 200)

    def test_start_all_hd(self):
        state.set_model(is_hd=True)
        self.start_all(app.programs.hd.list)

    def test_start_all_original(self):
        state.set_model(is_hd=False)
        self.start_all(app.programs.original.list)

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
        r = self.app.put("/api/stop")
        self.assertEqual(r.status_code, 200)
