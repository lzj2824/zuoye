import unittest
from post_youdao import *

class PostYoudaoText(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def text_get_ts(self):
        #import time
        #t=time.time()
        #ts=str(int(round(t*1000)))
        #print(ts)
        get_ts=mock.Mock(return_value='1585615460763')
        self.assertEqual('1585615460763',get_ts())

if __name__ == '__main__':
    unittest.main()
