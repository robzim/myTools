from Tkinter import Tk, Label, Button


import pendulum
def myDateTime():
	theDateTime = pendulum.now().in_tz("UTC")
	theDateTime.format('YYYY-MM-DD HH:mm:ss', formatter='alternative')
	theDateTime.set_formatter('alternative')
	theDateTime.format('YYYY-MM-DD HH:mm:ss')
	print theDateTime.format('YYYY-MM-DD HH:mm:ss.SSSSSS z')


myDateTime()

