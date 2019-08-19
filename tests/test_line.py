import unittest
from drawingСommands.line import Line


class TestLine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.field = ['----------------------',
                     '|                    |',
                     '|                    |',
                     '|                    |',
                     '|                    |',
                     '----------------------']
        cls.file_path = 'example/output.txt'

    def test_valid_data(self):
        with open(self.file_path, 'a') as file:
            self.line = Line(file, self.field)
            with self.assertRaises(Exception):
                self.line.valid_data(1, 2, 3, 4)

            with self.assertRaises(Exception):
                self.line.valid_data(0, 2, 0, 4)

            with self.assertRaises(Exception):
                self.line.valid_data(1, 0, 4, 0)

            with self.assertRaises(Exception):
                self.line.valid_data('a', 0, 4, 0)
            with self.assertRaises(Exception):
                self.line.valid_data(1, 'n', 4, 0)
            with self.assertRaises(Exception):
                self.line.valid_data(1, 0, 'y', 0)
            with self.assertRaises(Exception):
                self.line.valid_data(1, 0, 4, 'p')

    def test_create(self):
        with open(self.file_path, 'w') as file_write:
            line_create = Line(file_write, self.field)
            line_create.create(1, 1, 6, 1)
            test_line = line_create.create(6, 1, 6, 4)
            output_file = ['----------------------',
                           '|xxxxxx              |',
                           '|     x              |',
                           '|     x              |',
                           '|     x              |',
                           '----------------------']
            self.assertEqual(test_line, output_file)
        with open(self.file_path) as file_read:
            file_data = file_read.read().splitlines()
            self.assertEqual(file_data[-6:], output_file)


if __name__ == '__main__':
    unittest.main()
