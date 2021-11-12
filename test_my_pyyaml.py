#!/usr/bin/env python3

import unittest
import my_pyyaml

class TestMyPyYaml(unittest.TestCase):
    def setUp(self):
        self.yaml = my_pyyaml.MyPyYaml()

    def test_load_return_dict(self):
        line = self.yaml.load("")
        self.assertEqual(type(line), type(dict()))

    def test_load_simple_line(self):
        line = self.yaml.load("name: Flavien")
        self.assertEqual(list(line)[0], "name")
        self.assertEqual(list(line.values())[0], "Flavien")

    def test_load_simple_line_with_number(self):
        line = self.yaml.load("year: 2021")
        self.assertEqual(list(line)[0], "year")
        self.assertEqual(list(line.values())[0], 2021)

    def test_load_multi_lines(self):
        lines = self.yaml.load("""
name: Order
type: SALES
price: 350
        """)
        self.assertEqual(lines["name"], "Order")
        self.assertEqual(lines["type"], "SALES")
        self.assertEqual(lines["price"], 350)

    def test_load_object(self):
        obj = self.yaml.load("""
customer:
  firstName: Jon
  lastName: Snow
        """)
        self.assertEqual(type(obj["customer"]), type(dict()))
        self.assertEqual(obj["customer"]["firstName"], "Jon")
        self.assertEqual(obj["customer"]["lastName"], "Snow")

    def test_combine_object_simple_line(self):
        obj = self.yaml.load("""
country: FR
address:
  street: rue Ada Lovelace
  number: 117
city: Paris
        """)
        self.assertEqual(obj["country"], "FR")
        self.assertEqual(obj["address"]["street"], "rue Ada Lovelace")
        self.assertEqual(obj["address"]["number"], 117)
        self.assertEqual(obj["city"], "Paris")

if __name__ == '__main__':
    unittest.main()
