import unittest
from drawingСommands.bucketFill import BucketFill


class TestBucketFill(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.field = ['----------------------',
                     '|xxxxxx              |',
                     '|     x              |',
                     '|     x            x |',
                     '|     x              |',
                     '----------------------']
        cls.file_path = 'example/output.txt'

    def test_create(self):
        with open(self.file_path, 'w') as file_write:
            bucket_fill = BucketFill(file_write, self.field, 'o')
            with self.assertRaises(Exception):
                bucket_fill.create(0, 0)
            with self.assertRaises(Exception):
                bucket_fill.create('d', 1)
            with self.assertRaises(Exception):
                bucket_fill.create(10, 'v')

            self.assertTrue(bucket_fill.valid(self.field[3][10]))

            output_file = ['----------------------',
                           '|xxxxxxoooooooooooooo|',
                           '|     xoooooooooooooo|',
                           '|     xooooooooooooxo|',
                           '|     xoooooooooooooo|',
                           '----------------------']
            test_bucket_fill = bucket_fill.create(10, 1)
            self.assertEqual(test_bucket_fill, output_file)

        with open(self.file_path) as file_read:
            file_data = file_read.read().splitlines()
            self.assertEqual(file_data, output_file)


if __name__ == '__main__':
    unittest.main()
