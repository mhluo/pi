#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

from temperatureFun import get_temperature
from humidityFun import get_humidity
import relayFun as relayFun


@app.route('/')

# 获取温度数据
@app.route('/temperature/')
def get_tempData():
    wd=get_temperature()
    return '当前温度：{}'.format(wd)

# 获取湿度数据
@app.route('/humidity/')
def humidity():
    print('湿度')
    shidu=get_humidity()
    return '当前湿度：{}'.format(shidu)

# 控制继电器
@app.route('/control/<ctr_path>/<code>') # dynamic route
def control_relay(ctr_path,code):
	print("控制类型：%s, 状态码：%s"%(ctr_path,code))
	if ctr_path=='temperature' or ctr_path=='humidity' or ctr_path=='water' or ctr_path=='ph':
		# 控制温度/湿度度/水位/ph
		res=relayFun.do_action(ctr_path,int(code))
		return res
	else:
		print("请求的控制类型或路径出错，请检查")
		return("请求的控制类型或路径出错，请检查")


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # open for everyone