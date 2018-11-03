import unittest

from pyobsim.participant import Participant
from pyobsim.order import Order

class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.blank_participant = Participant(0, "", 0, 0)

    def test___init___normal(self):
        actual_order = Order(0, self.blank_participant, "", "", 0.01, 1)
        expected_order = Order(0, self.blank_participant, "", "", 0.01, 1)
        
        self.assertEqual(actual_order, expected_order)

    def test___init___negative_id(self):
        with self.assertRaises(ValueError):
            actual_order = Order(-1, self.blank_participant, "", "", 0.01, 1)

    def test___init___zero_price(self):
        with self.assertRaises(ValueError):
            actual_order = Order(0, self.blank_participant, "", "", 0.00, 1)

    def test___init___negative_price(self):
        with self.assertRaises(ValueError):
            actual_order = Order(0, self.blank_participant, "", "", -1.00, 1)

    def test___init___zero_quantity(self):
        with self.assertRaises(ValueError):
            actual_order = Order(0, self.blank_participant, "", "", 0.01, 0)

    def test___init___negative_quantity(self):
        with self.assertRaises(ValueError):
            actual_order = Order(0, self.blank_participant, "", "", 0.01, -1)

