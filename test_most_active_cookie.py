import unittest
from most_active_cookie import process_log_file
import os

class TestMostActiveCookie(unittest.TestCase):
    def setUp(self):
        self.test_file_single = 'test_single_cookie.csv'
        with open(self.test_file_single, 'w') as file:
            file.write('cookie,timestamp\n')
            file.write('AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n')
            file.write('SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n')
            file.write('AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n')

        self.test_file_multiple = 'test_multiple_cookies.csv'
        with open(self.test_file_multiple, 'w') as file:
            file.write('cookie,timestamp\n')
            file.write('AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n')
            file.write('SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n')
            file.write('AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n')
            file.write('SAZuXPGUrfbcn5UA,2018-12-09T22:03:00+00:00\n')

        self.test_file_none = 'test_no_cookies.csv'
        with open(self.test_file_none, 'w') as file:
            file.write('cookie,timestamp\n')
            file.write('AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n')
            file.write('SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n')

    def tearDown(self):
        os.remove(self.test_file_single)
        os.remove(self.test_file_multiple)
        os.remove(self.test_file_none)

    def test_single_cookie(self):
        result = process_log_file(self.test_file_single, '2018-12-09')
        self.assertEqual(result, ['AtY0laUfhglK3lC7'])

    def test_multiple_cookies(self):
        result = process_log_file(self.test_file_multiple, '2018-12-09')
        self.assertEqual(sorted(result), sorted(['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA']))

    def test_no_cookies(self):
        result = process_log_file(self.test_file_none, '2018-12-10')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
