import unittest
from unittest.mock import patch
from drawingСommands.file import File


class TestFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = 'example/output.txt'
        cls.file_bad_path = 'example/outt.txt'

    def test_file_path(self):
        with self.assertRaises(Exception):
            File(self.file_bad_path).file_path()
        output_file_return_path = File(self.file_path).file_path()
        self.assertEqual(self.file_path, output_file_return_path)

    @patch('file.File.read_file', return_value=['C 20 4', 'L 1 1 6 1'])
    def test_read_file(self, read_file):
        output_file = ['C 20 4', 'L 1 1 6 1']
        self.assertEqual(read_file(), output_file)


if __name__ == '__main__':
    unittest.main()
