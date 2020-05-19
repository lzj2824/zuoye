import weathers as weathers
from 第三章.city_weather import HeFeng


class HeFengDb(object):
    pass


if __name__=='__main__':
    hefeng=HeFeng()
    hefeng.get_all_weather(50)
    hefengDb=HeFengDb()
    hefengDb.save_all(weathers)