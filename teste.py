from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller

def click(x,y,andar):#single click
    if(andar):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    else:
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

i=0
while(True):
    i+=1  
    time.sleep(5)
    click(32, 1079, True)
    if(i==10):
        click(1020, 402,False)
        break
    
    
'''
time.sleep(2)
print(pyautogui.position())

click(1622, 0, True)
time.sleep(5)
print(pyautogui.position())

click(1622, 0, True)
time.sleep(5)
print(pyautogui.position())

click(1622, 0, True)
time.sleep(5)
print(pyautogui.position())

click(1622, 0, True)
print(pyautogui.position())

time.sleep(2)
click(1622, 0, True)
time.sleep(2)
click(1619, 0)'''