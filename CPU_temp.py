import time


def get_temp():
	f=open('/sys/class/thermal/thermal_zone0/temp','r')
	s=f.read()
	temp=int(s)
	last_temp=temp/1000
	print("CPU当前温度：",last_temp)

if __name__ == '__main__':
	while True:
		time.sleep(2)
		get_temp()
