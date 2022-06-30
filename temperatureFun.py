#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 获取温度数据
# 说明： DS18B20数字温度传感器实验
# 注意事项：DS18B20有唯一的地址，一般为28-XXXXXX
#####################################################


import os

makerobo_ds18b20 = ''  # ds18b20 设备

def setup():
	global makerobo_ds18b20  # 全局变量
	# 获取 ds18b20 地址
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			makerobo_ds18b20 = i       # ds18b20存放在ds18b20地址

# 读取ds18b20地址数据
def temp_read():
	makerobo_location = '/sys/bus/w1/devices/' + makerobo_ds18b20 + '/w1_slave' # 保存ds18b20地址信息
	makerobo_tfile = open(makerobo_location)  # 打开ds18b20 
	makerobo_text = makerobo_tfile.read()     # 读取到温度值
	makerobo_tfile.close()                    # 关闭读取
	secondline = makerobo_text.split("\n")[1] # 格式化处理
	temperaturedata = secondline.split(" ")[9]# 获取温度数据
	temperature = float(temperaturedata[2:])  # 去掉前两位
	temperature = temperature / 1000          # 去掉小数点
	return temperature                        # 返回温度值


# 释放资源
def destroy():
	pass

# 程序调用入口
def get_temperature():
	setup() #初始化
	if temp_read() != None:  # 调用读取温度值，如果读到到温度值不为空
		temp=("当前温度 : %0.3f C" % makerobo_read())# 打印温度值
		return temp
	else:
		return 'temperature_err'

