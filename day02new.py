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
print("=========6月3日====天气如下")
print('时间'+data['list'][0]['dt_txt'])
print('天气情况:'+data['list'][0]['weather'][0]['description'])
print('最高温度：'+str(data['list'][0]['main']['temp_max']))
print('最低温度:'+str(data['list'][0]['main']['temp_min']))

print("=========6月4日====天气如下")
print('时间'+data['list'][8]['dt_txt'])
print('天气情况:'+data['list'][8]['weather'][0]['description'])
print('最高温度：'+str(data['list'][8]['main']['temp_max']))
print('最低温度'+str(data['list'][8]['main']['temp_min']))

print("=========6月5日====天气如下")
print('时间'+data['list'][16]['dt_txt'])
print('天气情况:'+data['list'][16]['weather'][0]['description'])
print('最高温度：'+str(data['list'][16]['main']['temp_max']))
print('最低温度'+str(data['list'][16]['main']['temp_min']))

print("=========6月6日====天气如下")
print('时间'+data['list'][24]['dt_txt'])
print('天气情况:'+data['list'][24]['weather'][0]['description'])
print('最高温度：'+str(data['list'][24]['main']['temp_max']))
print('最低温度'+str(data['list'][24]['main']['temp_min']))

print("=========6月7日====天气如下")
print('时间'+data['list'][32]['dt_txt'])
print('天气情况:'+data['list'][32]['weather'][0]['description'])
print('最高温度：'+str(data['list'][32]['main']['temp_max']))
print('最低温度'+str(data['list'][32]['main']['temp_min']))