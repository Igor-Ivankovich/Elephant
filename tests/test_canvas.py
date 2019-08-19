import unittest

from drawingСommands.canvas import Canvas


class TestCanvas(unittest.TestCase):
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
            self.canvas = Canvas(file_write)
            with self.assertRaises(Exception):
                self.canvas.create('a', 4)
            with self.assertRaises(Exception):
                self.canvas.create(3, 'a')
            with self.assertRaises(Exception):
                self.canvas.create(-1, 4)
            with self.assertRaises(Exception):
                self.canvas.create(2, -3)

            test_canvas = self.canvas.create(20, 4)
            self.assertEqual(self.field, test_canvas)

        with open(self.file_path) as file_read:
            file_data = file_read.read().splitlines()
            self.assertEqual(file_data[-6:], self.field)


if __name__ == '__main__':
    unittest.main()
