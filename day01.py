# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request as r
city_pinyin=input("请输入城市拼音：")
print(city_pinyin)
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')

import json
data=json.loads(info)
print("欢迎使用全球天气app")
print("1.查看当前城市天气，2.查看其它城市天气，3.保存当前城市天气")
menno=input("请输入菜单：")
if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
if menno=="3":
    print("3.保留当前城市天气")
print('城市最高温度'+str(data['main']['temp_max']))
print('城市湿度'+str(data['main']['humidity']))
print('天气情况'+str(data['weather'][0]['description']))
