import unittest

from main import main, Main


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_path = 'example/output.txt'

    def test_main(self):
        with self.assertRaises(Exception):
            main([])

        self.assertIsNone(main(['main.py', 'example/input.txt', self.file_path]))

    def test_valid_data(self):
        with self.assertRaises(Exception):
            Main(self.file_path, ['']).valid_data()
        with self.assertRaises(Exception):
            Main(self.file_path, ['C 20 4', 'F 1 1 6 1']).valid_data()
        with self.assertRaises(Exception):
            Main(self.file_path, []).valid_data()
        with self.assertRaises(Exception):
            Main(self.file_path, ['R 16 1 20 3', 'L 1 1 6 1']).valid_data()

    def test_write_in_output_file(self):

        output_file = ['----------------------',
                       '|xxxxxxoooooooooxxxxx|',
                       '|     xooooooooox   x|',
                       '|     xoooooooooxxxxx|',
                       '|     xoooooooooooooo|',
                       '----------------------']
        return_file = Main(self.file_path, ['C 20 4', 'L 1 1 6 1',
                                            'L 6 2 6 4', 'R 16 1 20 3',
                                            'B 10 3 o']).write_in_output_file()
        self.assertEqual(output_file, return_file)

        with open(self.file_path) as file_read:
            file_data = file_read.read().splitlines()
            self.assertEqual(file_data[-6:], output_file)

        with self.assertRaises(Exception):
            Main(self.file_path, ['C 20 4 1', 'L 1 1 6 1']).write_in_output_file()
        with self.assertRaises(Exception):
            Main(self.file_path, ['C 20 4', 'L 1 1 6 1 5']).write_in_output_file()
        with self.assertRaises(Exception):
            Main(self.file_path, ['C 20 4', 'R 1 1 6 1 2']).write_in_output_file()
        with self.assertRaises(Exception):
            Main(self.file_path, ['C 20 4', 'B 1 1 6 1 2']).write_in_output_file()


if __name__ == '__main__':
    unittest.main()
