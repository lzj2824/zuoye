import unittest

from pymongo import results

from 第三章.city_weather_db import HefengDb


class Hefeng(object):
    pass


class TestCityWeatherDbCase(unittest.TestCase):

    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "lzj", "class": "net19049"})
        hefengDb.show_all()
        hefengDb.find({"name": "lzj"})
        for each in results:
            self.assertEqual("lzj", each['name'])
            self.assertEqual("net19049", each['class'])
        hefengDb.delete()
            #print(each)
        #self.assertEqual(4,hefengDb.find_all())

    def test_save_all(self):
        hefeng=Hefeng()
        weathers=hefeng.get_all_weather(7)
        hefengDb=HefengDb()
        hefengDb.save_all(weathers)
        print("show_all")
        hefengDb.show_all()
        self.assertEqual(7,hefengDb.count())
        hefengDb.delete()

if __name__ == '__main__':
    unittest.main()
