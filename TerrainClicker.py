import pyautogui
import os

#the position of the add terrain button
pyautogui.moveTo(1557, 281)
pyautogui.click()

def clicker():
	
	#position of the right side of the terrain I want to add to
	x = 674
	y = 661

	#takes the x and y coordinates and moves mouse to it.
	pyautogui.moveTo(x, y)
	pyautogui.click()

	#the amount of times I want this func to be repeated
	for i in range(47):
		while True:
			#the amount of times the func will add terrain upwards
			for i in range(75):
				pyautogui.move(0, 0 - 7.5, 1)
				pyautogui.click()
			#moves over right one, and adds a tile
			pyautogui.move(0 + 7.5, 0, 1)
			pyautogui.click()
			#the amount of times it adds a tile downwards
			for i in range(75):
				pyautogui.move(0, 0 + 7.5, 1)
				pyautogui.click()
			#moves over right again
			pyautogui.move(0 + 7.5, 0, 1)
			pyautogui.click()

#calls the definition to run it
clicker()
