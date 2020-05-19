import unittest

from 第三章.city_weather import Hefeng


class CityWeatherTest(unittest.TestCase):
    def test_get_city_code(self):
        hefeng=Hefeng()
        codes=hefeng.get_city_code()
        print(codes)
        count=0
        for each in codes:
            print(next(codes))
            count+=1
        print("count=",count)
        self.assertEqual(1620,count)

    def text_get_all_weather(self):
        hefeng=Hefeng()
        results=hefeng.get_all_weather(7)
        for each in results:
            print(each)
        self.assertEqual(7,len(results))

if __name__ == '__main__':
    unittest.main()
