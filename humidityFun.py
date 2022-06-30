#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 获取湿度度数据
# 说明：
# 注意事项：
#####################################################

import adafruit_dht


humidity_pin = 19		# DHT11 温湿度传感器管脚定义

def setup():
	global se
	se=adafruit_dht.DHT11(humidity_pin)


def get_humidity():
	#获取湿度
	humidity,temperature=se.humidity,se.temperature
	if humidity is not None:
		print('湿度是：{1:0.1f}%'.format(humidity))
		return "humidity"
	else:
		print("温度出错了！")
