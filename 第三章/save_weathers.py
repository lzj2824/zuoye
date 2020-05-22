import weathers as weathers
from 第三章.city_weather import HeFeng


class HeFengDb(object):
    pass


def save_all_weather():
    hefeng = HeFeng()
    hefeng.get_all_weather(50)
    hefengDb = HeFengDb()
    hefengDb.save_all(weathers)
    hefengDb.show_all()

if __name__=='__main__':
    hefengDb=HeFengDb()
    for each in hefengDb.find({'HeWeather6.basic.city':'北京'}):
        print(each)
    for each in hefengDb.find({'HeWeather6.basic.now.cond_txt':'晴'}):
        print(each)