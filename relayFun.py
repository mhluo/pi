#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 获取湿度度数据
# 说明：
# 注意事项：
#####################################################

import RPi.GPIO as GPIO
import time

pins={
	'temperature_add_pin':11, #温度-加热 管脚
	'temperature_less_pin':12, #温度-降温 管脚
	'humidity_add_pin':13, #湿度-加湿 管脚
	'humidity_less_pin':14, #湿度-祛湿 管脚
	'water_add_pin':15, #水位-加水 管脚
	'water_less_pin':16, #水位-排水 管脚
}

isSetup=False

#初始化
def setup():
	#GPIO.setmode(GPIO.BOARD) #采用实际的物理管脚
	for item in pins:
		GPIO.setup(pins[item],GPIO.OUT) #设置管脚模式为：输出模式
		GPIO.output(pins[item],GPIO.LOW) #输出低电平，先关闭继电器

#关闭所有继电器
def close_all():
	for item in pins:
		GPIO.output(pins[item],GPIO.LOW) #输出低电平，关闭继电器

	GPIO.cleanup()

#打开继电器
def openR(name):
	print('打开继电器',pins[name])
	GPIO.output(pins[name],GPIO.HIGH) #输出高电平，开启继电器
	print(GPIO.input(pins[name]))
	time.sleep(3)
	closeR(name)
	print(GPIO.input(pins[name]))

#关闭继电器
def closeR(name):
	GPIO.output(pins[name],GPIO.LOW) #输出低电平，关闭继电器

def do_action(name,code):
	print('do_action:',name,code)
	global isSetup
	if(not isSetup):
		setup()
		isSetup=True
	
	if(code==1):
		pin_name=name+'_add_pin'
		openR(pin_name)
		return 'added'
	elif(code==-1):
		pin_name=name+'_less_pin'
		openR(pin_name)
		return 'lessed'
	else:
		close_all() # 关闭所有继电器
		return '请求的控制类型或状态码出错'
