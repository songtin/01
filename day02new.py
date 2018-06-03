# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:12:37 2018

@author: stt
"""
import urllib.request as r
city_pinyin=input("请输入城市拼音：")
print(city_pinyin)
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')

import json
data=json.loads(info)
days=[0,8,16,24,32]
def wea(data,day): 
     print('时间是：'+str(data['list'][day]['dt_txt']))
     print('天气情况是:'+str(data['list'][day]['weather'][0]['description']))
     print('当前风速是'+str(data['list'][day]['wind']['speed']))
     print('最高温度是：'+str(data['list'][day]['main']['temp_max']))
     print('最低气温是：'+str(data['list'][day]['main']['temp_min']))
     print('........................\n')
for day in days:
    wea(data,day)
    


