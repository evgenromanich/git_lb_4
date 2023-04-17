from math import *


def f_opt(x):
	if (x > -1) and (x < 0):
		y = sin(x)
	elif (x >= 0) and (x < 1):
		y = cos(x)
	else:
		y = 0
	return round(y, 3)

num = float(input())
print(f_opt(num))
#--------------------------------


def f(x):
	if round(-pi, 3) < round (x , 3) < 0:
		y = sin(x)
	elif 0 <= round(x , 3) < round(pi, 3):
		y = cos(x)
	else:
		y = 0
	return round(y, 3)

def Y_tab():
	x = round(-2 * pi, 3)
	h = round(pi / 8, 3)
	while x <= round(2* pi, 3):
		y = f(x)
		print('x = ', round(x,3), '\t', 'y = ', round(y,3))
		x += h

Y_tab()