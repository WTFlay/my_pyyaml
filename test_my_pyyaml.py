#!/usr/bin/env python3

import unittest
import my_pyyaml

class TestMyPyYaml(unittest.TestCase):
    def setUp(self):
        self.parser = my_pyyaml.MyPyYaml()

    def test_parse_return_dict(self):
        line = self.parser.parse("")
        self.assertEqual(type(line), type(dict()))

    def test_parse_simple_line(self):
        line = self.parser.parse("name: Flavien")
        self.assertEqual(list(line)[0], "name")
        self.assertEqual(list(line.values())[0], "Flavien")

    def test_parse_simple_line_with_number(self):
        line = self.parser.parse("year: 2021")
        self.assertEqual(list(line)[0], "year")
        self.assertEqual(list(line.values())[0], 2021)

    def test_parse_multi_lines(self):
        lines = self.parser.parse("""
        name: Order
        type: SALES
        price: 350
        """)
        self.assertEqual(lines["name"], "Order")
        self.assertEqual(lines["type"], "SALES")
        self.assertEqual(lines["price"], 350)

if __name__ == '__main__':
    unittest.main()
