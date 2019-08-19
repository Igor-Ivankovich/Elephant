import unittest
from drawingСommands.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.field = ['----------------------',
                     '|                    |',
                     '|                    |',
                     '|                    |',
                     '|                    |',
                     '----------------------']
        cls.file_path = 'example/output.txt'

    def test_create(self):
        with open(self.file_path, 'w') as file_write:
            self.rectangle = Rectangle(file_write, self.field)
            test_rectangle = self.rectangle.create(16, 1, 20, 3)
            output_file = ['----------------------',
                           '|               xxxxx|',
                           '|               x   x|',
                           '|               xxxxx|',
                           '|                    |',
                           '----------------------']
            self.assertEqual(output_file, test_rectangle)
        with open(self.file_path) as file_read:
            file_data = file_read.read().splitlines()
            self.assertEqual(file_data, output_file)


if __name__ == '__main__':
    unittest.main()
