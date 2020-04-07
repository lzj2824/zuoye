import unittest
from unittest import mock
from post_youdao import *

class PostYoudaoText(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value='15862200738969')
        self.assertEqual('15862200738969',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='158622007389693')
        self.assertEqual('158622007389693',get_salt())

    def test_get_sign(self):
        self.assertEqual('d330b7eeeef6a968524d0ea22f41a6f2',get_sign())
if __name__ == '__main__':
    unittest.main()
