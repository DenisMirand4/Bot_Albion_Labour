import tkinter
from tkinter.constants import S
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller
from tkinter import Event
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import B, Checkbox, Check
import os

class GUI:

    biscoito_imb = [
        [sg.Text('Biscoito1  '),sg.Checkbox('',default=True,key=1)],
        [sg.Text('Biscoito 4 '),sg.Checkbox('',default=True,key=2)],
        [sg.Text('Biscoito 7 '),sg.Checkbox('',default=True,key=3)],
        [sg.Text('Biscoito 10'),sg.Checkbox('',default=True,key=4)],
        [sg.Text('Biscoito 13'),sg.Checkbox('',default=True,key=5)],
        [sg.Text('Biscoito 16'),sg.Checkbox('',default=True,key=6)],
        [sg.Text('Biscoito 19'),sg.Checkbox('',default=True,key=7)],]

    bolacha_imb =[
        [sg.Text('Bolacha 01'),sg.Checkbox('',default=True,key=8)],
        [sg.Text('Bolacha 04'),sg.Checkbox('',default=True,key=9)],
        [sg.Text('Bolacha 07'),sg.Checkbox('',default=True,key=10)],
        [sg.Text('Bolacha 10'),sg.Checkbox('',default=True,key=11)],
        [sg.Text('Bolacha 13'),sg.Checkbox('',default=True,key=12)],
        [sg.Text('Bolacha 16'),sg.Checkbox('',default=True,key=13)],
        [sg.Text('Bolacha 19'),sg.Checkbox('',default=True,key=14)],]

    polvilho_imb = [
        [sg.Text('Polvilho 01'),sg.Checkbox('',default=True,key=15)],
        [sg.Text('Polvilho 04'),sg.Checkbox('',default=True,key=16)],
        [sg.Text('Polvilho 07'),sg.Checkbox('',default=True,key=17)],
        [sg.Text('Polvilho 10'),sg.Checkbox('',default=True,key=18)],
        [sg.Text('Polvilho 13'),sg.Checkbox('',default=True,key=19)],
        [sg.Text('Polvilho 16'),sg.Checkbox('',default=True,key=20)],
        [sg.Text('Polvilho 19'),sg.Checkbox('',default=True,key=21)],]

    cookie_imb = [
        [sg.Text('Cookie 01'),sg.Checkbox('',default=True,key=22)],
        [sg.Text('Cookie 04'),sg.Checkbox('',default=True,key=23)],
        [sg.Text('Cookie 07'),sg.Checkbox('',default=True,key=24)],
        [sg.Text('Cookie 10'),sg.Checkbox('',default=True,key=25)],
        [sg.Text('Cookie 13'),sg.Checkbox('',default=True,key=26)],
        [sg.Text('Cookie 16'),sg.Checkbox('',default=True,key=27)],
        [sg.Text('Cookie 19'),sg.Checkbox('',default=True,key=28)],]

    rosca_imb = [
        [sg.Text('Rosca 01'),sg.Checkbox('',default=True,key=29)],
        [sg.Text('Rosca 04'),sg.Checkbox('',default=True,key=30)],
        [sg.Text('Rosca 07'),sg.Checkbox('',default=True,key=31)],
        [sg.Text('Rosca 10'),sg.Checkbox('',default=True,key=32)],
        [sg.Text('Rosca 13'),sg.Checkbox('',default=True,key=33)],
        [sg.Text('Rosca 16'),sg.Checkbox('',default=True,key=34)],
        [sg.Text('Rosca 19'),sg.Checkbox('',default=True,key=35)],]

    bolo_imb = [
        [sg.Text('Bolo 01'),sg.Checkbox('',default=True,key=36)],
        [sg.Text('Bolo 04'),sg.Checkbox('',default=True,key=37)],
        [sg.Text('Bolo 07'),sg.Checkbox('',default=True,key=38)],
        [sg.Text('Bolo 10'),sg.Checkbox('',default=True,key=39)],
        [sg.Text('Bolo 13'),sg.Checkbox('',default=True,key=40)],]

    biscoito_fle = [
        [sg.Text('Biscoito2  '),sg.Checkbox('',default=True,key=41)],
        [sg.Text('Biscoito 5 '),sg.Checkbox('',default=True,key=42)],
        [sg.Text('Biscoito 8 '),sg.Checkbox('',default=True,key=43)],
        [sg.Text('Biscoito 11'),sg.Checkbox('',default=True,key=44)],
        [sg.Text('Biscoito 14'),sg.Checkbox('',default=True,key=45)],
        [sg.Text('Biscoito 17'),sg.Checkbox('',default=True,key=46)],
        [sg.Text('Biscoito 20'),sg.Checkbox('',default=True,key=47)],]

    bolacha_fle = [
        [sg.Text('Bolacha 02'),sg.Checkbox('',default=True,key=48)],
        [sg.Text('Bolacha 05'),sg.Checkbox('',default=True,key=49)],
        [sg.Text('Bolacha 08'),sg.Checkbox('',default=True,key=50)],
        [sg.Text('Bolacha 11'),sg.Checkbox('',default=True,key=51)],
        [sg.Text('Bolacha 14'),sg.Checkbox('',default=True,key=52)],
        [sg.Text('Bolacha 17'),sg.Checkbox('',default=True,key=53)],
        [sg.Text('Bolacha 20'),sg.Checkbox('',default=True,key=54)],]

    polvilho_fle = [
        [sg.Text('Polvilho 02'),sg.Checkbox('',default=True,key=55)],
        [sg.Text('Polvilho 05'),sg.Checkbox('',default=True,key=56)],
        [sg.Text('Polvilho 08'),sg.Checkbox('',default=True,key=57)],
        [sg.Text('Polvilho 11'),sg.Checkbox('',default=True,key=58)],
        [sg.Text('Polvilho 14'),sg.Checkbox('',default=True,key=59)],
        [sg.Text('Polvilho 17'),sg.Checkbox('',default=True,key=60)],
        [sg.Text('Polvilho 20'),sg.Checkbox('',default=True,key=61)],]

    cookie_fle = [
        [sg.Text('Cookie 02'),sg.Checkbox('',default=True,key=62)],
        [sg.Text('Cookie 05'),sg.Checkbox('',default=True,key=63)],
        [sg.Text('Cookie 08'),sg.Checkbox('',default=True,key=64)],
        [sg.Text('Cookie 11'),sg.Checkbox('',default=True,key=65)],
        [sg.Text('Cookie 14'),sg.Checkbox('',default=True,key=66)],
        [sg.Text('Cookie 17'),sg.Checkbox('',default=True,key=67)],
        [sg.Text('Cookie 20'),sg.Checkbox('',default=True,key=68)],]

    rosca_fle = [
        [sg.Text('Rosca 02'),sg.Checkbox('',default=True,key=69)],
        [sg.Text('Rosca 05'),sg.Checkbox('',default=True,key=70)],
        [sg.Text('Rosca 08'),sg.Checkbox('',default=True,key=71)],
        [sg.Text('Rosca 11'),sg.Checkbox('',default=True,key=72)],
        [sg.Text('Rosca 14'),sg.Checkbox('',default=True,key=73)],
        [sg.Text('Rosca 17'),sg.Checkbox('',default=True,key=74)],
        [sg.Text('Rosca 20'),sg.Checkbox('',default=True,key=75)],]

    bolo_fle = [
        [sg.Text('Bolo 02'),sg.Checkbox('',default=True,key=76)],
        [sg.Text('Bolo 05'),sg.Checkbox('',default=True,key=77)],
        [sg.Text('Bolo 08'),sg.Checkbox('',default=True,key=78)],
        [sg.Text('Bolo 11'),sg.Checkbox('',default=True,key=79)],
        [sg.Text('Bolo 14'),sg.Checkbox('',default=True,key=80)],]

    biscoito_fer = [
        [sg.Text('Biscoito3  '),sg.Checkbox('',default=True,key=81)],
        [sg.Text('Biscoito 6 '),sg.Checkbox('',default=True,key=82)],
        [sg.Text('Biscoito 9 '),sg.Checkbox('',default=True,key=83)],
        [sg.Text('Biscoito 12'),sg.Checkbox('',default=True,key=84)],
        [sg.Text('Biscoito 15'),sg.Checkbox('',default=True,key=85)],
        [sg.Text('Biscoito 18'),sg.Checkbox('',default=True,key=86)],
        [sg.Text('Biscoito 21'),sg.Checkbox('',default=True,key=87)],]

    bolacha_fer = [
        [sg.Text('Bolacha 03'),sg.Checkbox('',default=True,key=88)],
        [sg.Text('Bolacha 06'),sg.Checkbox('',default=True,key=89)],
        [sg.Text('Bolacha 09'),sg.Checkbox('',default=True,key=90)],
        [sg.Text('Bolacha 12'),sg.Checkbox('',default=True,key=91)],
        [sg.Text('Bolacha 15'),sg.Checkbox('',default=True,key=92)],
        [sg.Text('Bolacha 18'),sg.Checkbox('',default=True,key=93)],
        [sg.Text('Bolacha 21'),sg.Checkbox('',default=True,key=94)],]

    polvilho_fer = [
        [sg.Text('Polvilho 03'),sg.Checkbox('',default=True,key=95)],
        [sg.Text('Polvilho 06'),sg.Checkbox('',default=True,key=96)],
        [sg.Text('Polvilho 09'),sg.Checkbox('',default=True,key=97)],
        [sg.Text('Polvilho 12'),sg.Checkbox('',default=True,key=98)],
        [sg.Text('Polvilho 15'),sg.Checkbox('',default=True,key=99)],
        [sg.Text('Polvilho 18'),sg.Checkbox('',default=True,key=100)],
        [sg.Text('Polvilho 21'),sg.Checkbox('',default=True,key=101)],]

    cookie_fer = [
        [sg.Text('Cookie 03'),sg.Checkbox('',default=True,key=102)],
        [sg.Text('Cookie 06'),sg.Checkbox('',default=True,key=103)],
        [sg.Text('Cookie 09'),sg.Checkbox('',default=True,key=104)],
        [sg.Text('Cookie 12'),sg.Checkbox('',default=True,key=105)],
        [sg.Text('Cookie 15'),sg.Checkbox('',default=True,key=106)],
        [sg.Text('Cookie 18'),sg.Checkbox('',default=True,key=107)],
        [sg.Text('Cookie 21'),sg.Checkbox('',default=True,key=108)],]

    rosca_fer = [
        [sg.Text('Rosca 03'),sg.Checkbox('',default=True,key=109)],
        [sg.Text('Rosca 06'),sg.Checkbox('',default=True,key=110)],
        [sg.Text('Rosca 09'),sg.Checkbox('',default=True,key=111)],
        [sg.Text('Rosca 12'),sg.Checkbox('',default=True,key=112)],
        [sg.Text('Rosca 15'),sg.Checkbox('',default=True,key=113)],
        [sg.Text('Rosca 18'),sg.Checkbox('',default=True,key=114)],
        [sg.Text('Rosca 21'),sg.Checkbox('',default=True,key=115)],]

    bolo_fer = [
        [sg.Text('Bolo 03'),sg.Checkbox('',default=True,key=116)],
        [sg.Text('Bolo 06'),sg.Checkbox('',default=True,key=117)],
        [sg.Text('Bolo 09'),sg.Checkbox('',default=True,key=118)],
        [sg.Text('Bolo 12'),sg.Checkbox('',default=True,key=119)],
        [sg.Text('Bolo 15'),sg.Checkbox('',default=True,key=120)],]

    layout= [
        #here i use column to separate the 3 tipes of labour
        [sg.Button('Start',) ,sg.Button('Toggle IMBUIDOR'), sg.Button('Toggle FLECHEIRO'), sg.Button('Toggle FERREIRO')],
        [sg.Text('========================================IMBUIDOR========================================')],
        [sg.Text(' '),sg.Button('Toggle',key='biscoito_imb'),sg.Text('            '),sg.Button('Toggle',key = 'bolacha_imb'),sg.Text('             '), sg.Button('Toggle',key = 'polvilho_imb'),sg.Text('           '),sg.Button('Toggle',key = 'cookie_imb'),sg.Text('        '),sg.Button('Toggle',key = 'rosca_imb'),sg.Text('          '),sg.Button('Toggle',key = 'bolo_imb')],
        [sg.Column(biscoito_imb),sg.Column(bolacha_imb),sg.Column(polvilho_imb),sg.Column(cookie_imb),sg.Column(rosca_imb),sg.Column(bolo_imb)],
        [sg.Text('========================================FLECHEIRO=======================================')],
        [sg.Text(' '),sg.Button('Toggle',key='biscoito_fle'),sg.Text('            '),sg.Button('Toggle',key = 'bolacha_fle'),sg.Text('             '), sg.Button('Toggle',key = 'polvilho_fle'),sg.Text('           '),sg.Button('Toggle',key = 'cookie_fle'),sg.Text('        '),sg.Button('Toggle',key = 'rosca_fle'),sg.Text('          '),sg.Button('Toggle',key = 'bolo_fle')],
        [sg.Column(biscoito_fle, key=('imbuidor')),sg.Column(bolacha_fle),sg.Column(polvilho_fle),sg.Column(cookie_fle),sg.Column(rosca_fle),sg.Column(bolo_fle)],
        [sg.Text('========================================FERREIRO========================================')],
        [sg.Text(' '),sg.Button('Toggle',key='biscoito_fer'),sg.Text('            '),sg.Button('Toggle',key = 'bolacha_fer'),sg.Text('             '), sg.Button('Toggle',key = 'polvilho_fer'),sg.Text('           '),sg.Button('Toggle',key = 'cookie_fer'),sg.Text('        '),sg.Button('Toggle',key = 'rosca_fer'),sg.Text('          '),sg.Button('Toggle',key = 'bolo_fer')],
        [sg.Column(biscoito_fer),sg.Column(bolacha_fer),sg.Column(polvilho_fer),sg.Column(cookie_fer),sg.Column(rosca_fer),sg.Column(bolo_fer)]]

    window = sg.Window("Labour Manager", layout)

    while (True):#The loop that update your window
   
        event, numero_ilha = window.read()

        if event in ('Start', sg.WIN_CLOSED):
            break
        if event in ('Toggle IMBUIDOR'):
            for t in range(1,41):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('Toggle FLECHEIRO'):
            for t in range(41,81):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('Toggle FERREIRO'):
            for t in range(81,121):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('biscoito_imb'):
            for t in range(1,8):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('bolacha_imb'):
            for t in range(8,15):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('polvilho_imb'):
            for t in range(15,22):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('cookie_imb'):
            for t in range(22,29):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('rosca_imb'):
            for t in range(29,36):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('bolo_imb'):
            for t in range(36,41):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('biscoito_fle'):
            for t in range(41,48):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('bolacha_fle'):
            for t in range(48,55):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('polvilho_fle'):
            for t in range(55,62):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('cookie_fle'):
            for t in range(62,69):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('rosca_fle'):
            for t in range(69,76):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('bolo_fle'):
            for t in range(76,81):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('biscoito_fer'):
            for t in range(81,88):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('bolacha_fer'):
            for t in range(88,95):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('polvilho_fer'):
            for t in range(95,102):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('cookie_fer'):
            for t in range(102,109):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('rosca_fer'):
            for t in range(109,116):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        if event in ('bolo_fer'):
            for t in range(116,121):
                if numero_ilha[t] == True:
                    window[t].Update(value = False)
                else:
                    window[t].Update(value = True)
        
                
    window.close()#Close the window

def click(x,y,andar):#single click, u can swich andar to do a right or left click 
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

def click_arrasta(x,y,a,b):#this simulate a click with shift or alt in game, basically the mouse teleport from (x,y) to (a,b)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.SetCursorPos((a,b))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.01)

def vai_trabalhador():# walk from the start of the island till the laborers
    timed_out=0
    while(True):
        click(1622, 0, True)
        time.sleep(3)
        timed_out+=1

        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha.png', confidence = 0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha Dia.png', confidence = 0.5) != None :
            time.sleep(0.2)
            click(1622, 0, True)
            time.sleep(0.5)
            return False
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            deu_merda()
            return True
        if (timed_out==8):
            deu_merda()
            return True

def volta_trabalhador():#walk from the end of the island till the Travel Planer
    timed_out=0
    while(True): 
        
        click(60, 1079, True)
        time.sleep(2)
        timed_out+=1
        if(timed_out==10):
            deu_merda()
            return True
            
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.6) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador_noite.png', confidence = 0.6) != None :
            click(60, 1079, True)
            time.sleep(1)
            a = pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.6)
            b = pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador_noite.png', confidence = 0.6)
            if (a==None):
                if (b==None):
                    click(60, 1079, True)
                    time.sleep(1.5)
                    click(1082, 264, False)
                    break
                else:
                    pyautogui.click(b)
                    break
            else:
                pyautogui.click(a)
                break      

        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            deu_merda()
            return True

def faz_trabalhador():#click in each labour and put the journals into it    
    
    for x in range(8):
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            deu_merda()
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha.png', confidence=0.6) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha Dia.png', confidence=0.6) != None:
            click(1020, 402, False)#1 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(1026, 551, False)#2 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(898, 427, False)#3 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(925, 645, False)#4 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(817, 499, False)#5 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(833, 692, False)#6 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(779, 509, False)#7 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(787, 722, False)#8 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(772, 511, False)#9 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(793, 717, False)#10 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(784, 521, False)#11 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(789, 719, False)#12 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(772, 513, False)#13 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(783, 708, False)#14 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(764, 524, False)#15 labour
            time.sleep(0.2)
            error = coloca_diario()
            if(error == True):
                return True

            click(1858, 0, True)#go back to where he started
            time.sleep(2)
            return False

        else:
            time.sleep(0.5)

def coloca_diario():#make the task of colect and give the journal to the labour
    timed_out = 0
    while(True):
        if (timed_out==40):
            deu_merda()
            return True
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Take All.png', confidence=0.8) != None:
            click(216, 861, False)#colect the resources from labours
            break
        else:
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Deixar Diario.png', confidence=0.8) != None:
                break #if there is no resorce to colect but the labour is ready to work
            else:
                if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Esta trabalho.png', confidence=0.8) != None:
                    return False #labor is still working
                else:
                    if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence=0.8) != None: 
                        click(1858, 0, True)
                        time.sleep(3)
                        deu_merda()
                        return True #didn't click in the labour(security scape)
                    else:
                        time.sleep(0.1)
                        timed_out+=1
        
    timed_out = 0
    while(True):
        if (timed_out==30):
            deu_merda()
            return True
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Deixar Diario.png', confidence=0.8) != None:
            click_arrasta(1585, 548, 207, 659)#put the journal in the labour
            time.sleep(0.3)
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Aceitar.png', confidence=0.8) != None:
                break
            else:
                click_arrasta(1585, 548, 207, 659)
        else:
            time.sleep(0.1)
            timed_out+=1
            
    timed_out = 0
    while(True):
        if (timed_out==30):
            deu_merda()
            return True   
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Aceitar.png', confidence=0.8) != None:
            click(121, 866, False)#after the journal is put in the labour this funcion click to confirm the journal and start the work
            time.sleep(0.3)
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence=0.8) != None:
                return False
            else:
                click(121, 866, False)

        else:
            time.sleep(0.1)
            timed_out+=1

def viaja_prox(numero_ilha):#type the name of the island u want to travel
    timed_out=0             ##If u want to use u need to change the name of the islands to match with your own islands
    while(True):            ###Notice the number of 'numero_ilha' plus one in each island
        timed_out+=1
        time.sleep(2)
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Comprar Viagem.png', confidence=0.8) != None:
            click_arrasta(176, 289,228, 291)
            time.sleep(1)
            pyautogui.press('backspace')
            time.sleep(1)
            break
        if((timed_out==30)  and (pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viagem_indisponivel.png', confidence=0.8) != None)):
            pyautogui.press('esc')
            time.sleep(2)
            click(995, 256,False)
        if(timed_out==5):
            click(1009, 500, True)
            time.sleep(1)
            volta_trabalhador()
        if(timed_out==50):
            deu_merda()
        else:
            time.sleep(0.1)

    if(numero_ilha == -1):
        pyautogui.write('Fort Stearling Craft')#onde pega os livros
        confirma_viagem()
    if(numero_ilha == 0):
        pyautogui.write('Pedra Refino')#Your backup point
        confirma_viagem()
    if(numero_ilha == 1):
        pyautogui.write('biscoito1')#U change here and repet if u have more then one island, and so on
        confirma_viagem()           ##In case u have a different number u just need to add more if's or remove then
    if(numero_ilha == 2):
        pyautogui.write('biscoito 4')
        confirma_viagem()
    if(numero_ilha == 3):
        pyautogui.write('biscoito 7')
        confirma_viagem()
    if(numero_ilha == 4):
        pyautogui.write('biscoito 10')
        confirma_viagem()
    if(numero_ilha == 5):
        pyautogui.write('biscoito 13')
        confirma_viagem()
    if(numero_ilha == 6):
        pyautogui.write('biscoito 16')
        confirma_viagem()
    if(numero_ilha == 7):
        pyautogui.write('biscoito 19')
        confirma_viagem()
    if(numero_ilha == 8):
        pyautogui.write('bolacha 01')
        confirma_viagem()
    if(numero_ilha == 9):
        pyautogui.write('bolacha 04')
        confirma_viagem()
    if(numero_ilha == 10):
        pyautogui.write('bolacha 07')
        confirma_viagem()
    if(numero_ilha == 11):
        pyautogui.write('bolacha 10')
        confirma_viagem()
    if(numero_ilha == 12):
        pyautogui.write('bolacha 13')
        confirma_viagem()
    if(numero_ilha == 13):
        pyautogui.write('bolacha 16')
        confirma_viagem()
    if(numero_ilha == 14):
        pyautogui.write('bolacha 19')
        confirma_viagem()
    if(numero_ilha == 15):
        pyautogui.write('polvilho 01')
        confirma_viagem()
    if(numero_ilha == 16):
        pyautogui.write('polvilho 04')
        confirma_viagem()
    if(numero_ilha == 17):
        pyautogui.write('polvilho 07')
        confirma_viagem()
    if(numero_ilha == 18):
        pyautogui.write('polvilho 10')
        confirma_viagem()
    if(numero_ilha == 19):
        pyautogui.write('polvilho 13')
        confirma_viagem()
    if(numero_ilha == 20):
        pyautogui.write('polvilho 16')
        confirma_viagem()
    if(numero_ilha == 21):
        pyautogui.write('polvilho 19')
        confirma_viagem()
    if(numero_ilha == 22):
        pyautogui.write('cookie 01')
        confirma_viagem()
    if(numero_ilha == 23):
        pyautogui.write('cookie 04')
        confirma_viagem()
    if(numero_ilha == 24):
        pyautogui.write('cookie 07')
        confirma_viagem()
    if(numero_ilha == 25):
        pyautogui.write('cookie 10')
        confirma_viagem()
    if(numero_ilha == 26):
        pyautogui.write('cookie 13')
        confirma_viagem()
    if(numero_ilha == 27):
        pyautogui.write('cookie 16')
        confirma_viagem()
    if(numero_ilha == 28):
        pyautogui.write('cookie 19')
        confirma_viagem()
    if(numero_ilha == 29):
        pyautogui.write('rosca 01')
        confirma_viagem()
    if(numero_ilha == 30):
        pyautogui.write('rosca 04')
        confirma_viagem()
    if(numero_ilha == 31):
        pyautogui.write('rosca 07')
        confirma_viagem()
    if(numero_ilha == 32):
        pyautogui.write('rosca 10')
        confirma_viagem()
    if(numero_ilha == 33):
        pyautogui.write('rosca 13')
        confirma_viagem()
    if(numero_ilha == 34):
        pyautogui.write('rosca 16')
        confirma_viagem()
    if(numero_ilha == 35):
        pyautogui.write('rosca 19')
        confirma_viagem()
    if(numero_ilha == 36):
        pyautogui.write('bolo 01')
        confirma_viagem()
    if(numero_ilha==37):
        pyautogui.write('bolo 04')
        confirma_viagem()
    if(numero_ilha==38):
        pyautogui.write('bolo 07')
        confirma_viagem()
    if(numero_ilha==39):
        pyautogui.write('bolo 10')
        confirma_viagem()
    if(numero_ilha==40):
        pyautogui.write('bolo 13')
        confirma_viagem()
    if(numero_ilha==41):
        pyautogui.write('biscoito2')
        confirma_viagem()
    if(numero_ilha==42):
        pyautogui.write('biscoito 5')
        confirma_viagem()
    if(numero_ilha==43):
        pyautogui.write('biscoito 8')
        confirma_viagem()
    if(numero_ilha==44):
        pyautogui.write('biscoito 11')
        confirma_viagem()
    if(numero_ilha==45):
        pyautogui.write('biscoito 14')
        confirma_viagem()
    if(numero_ilha==46):
        pyautogui.write('biscoito 17')
        confirma_viagem()
    if(numero_ilha==47):
        pyautogui.write('biscoito 20')
        confirma_viagem()
    if(numero_ilha==48):
        pyautogui.write('bolacha 02')
        confirma_viagem()
    if(numero_ilha==49):
        pyautogui.write('bolacha 05')
        confirma_viagem()
    if(numero_ilha==50):
        pyautogui.write('bolacha 08')
        confirma_viagem()
    if(numero_ilha==51):
        pyautogui.write('bolacha 11')
        confirma_viagem()
    if(numero_ilha==52):
        pyautogui.write('bolacha 14')
        confirma_viagem()
    if(numero_ilha==53):
        pyautogui.write('bolacha 17')
        confirma_viagem()
    if(numero_ilha==54):
        pyautogui.write('bolacha 20')
        confirma_viagem()
    if(numero_ilha==55):
        pyautogui.write('polvilho 02')
        confirma_viagem()
    if(numero_ilha==56):
        pyautogui.write('polvilho 05')
        confirma_viagem()
    if(numero_ilha==57):
        pyautogui.write('polvilho 08')
        confirma_viagem()
    if(numero_ilha==58):
        pyautogui.write('polvilho 11')
        confirma_viagem()
    if(numero_ilha==59):
        pyautogui.write('polvilho 14')
        confirma_viagem()
    if(numero_ilha==60):
        pyautogui.write('polvilho 17')
        confirma_viagem()
    if(numero_ilha==61):
        pyautogui.write('polvilho 20')
        confirma_viagem()
    if(numero_ilha==62):
        pyautogui.write('cookie 02')
        confirma_viagem()
    if(numero_ilha==63):
        pyautogui.write('cookie 05')
        confirma_viagem()
    if(numero_ilha==64):
        pyautogui.write('cookie 08')
        confirma_viagem()
    if(numero_ilha==65):
        pyautogui.write('cookie 11')
        confirma_viagem()
    if(numero_ilha==66):
        pyautogui.write('cookie 14')
        confirma_viagem()
    if(numero_ilha==67):
        pyautogui.write('cookie 17')
        confirma_viagem()
    if(numero_ilha==68):
        pyautogui.write('cookie 20')
        confirma_viagem()
    if(numero_ilha==69):
        pyautogui.write('rosca 02')
        confirma_viagem()
    if(numero_ilha==70):
        pyautogui.write('rosca 05')
        confirma_viagem()
    if(numero_ilha==71):
        pyautogui.write('rosca 08')
        confirma_viagem()    
    if(numero_ilha==72):
        pyautogui.write('rosca 11')
        confirma_viagem()    
    if(numero_ilha==73):
        pyautogui.write('rosca 14')
        confirma_viagem()    
    if(numero_ilha==74):
        pyautogui.write('rosca 17')
        confirma_viagem()    
    if(numero_ilha==75):
        pyautogui.write('rosca 20')
        confirma_viagem()    
    if(numero_ilha==76):
        pyautogui.write('bolo 02')
        confirma_viagem()    
    if(numero_ilha==77):
        pyautogui.write('bolo 05')
        confirma_viagem()    
    if(numero_ilha==78):
        pyautogui.write('bolo 08')
        confirma_viagem()    
    if(numero_ilha==79):
        pyautogui.write('bolo 11')
        confirma_viagem()    
    if(numero_ilha==80):
        pyautogui.write('bolo 14')
        confirma_viagem()   
    if(numero_ilha==81):
        pyautogui.write('biscoito3')
        confirma_viagem()    
    if(numero_ilha==82):
        pyautogui.write('biscoito 6')
        confirma_viagem()
    if(numero_ilha==83):
        pyautogui.write('biscoito 9')
        confirma_viagem()
    if(numero_ilha==84):
        pyautogui.write('biscoito 12')
        confirma_viagem()
    if(numero_ilha==85):
        pyautogui.write('biscoito 15')
        confirma_viagem()
    if(numero_ilha==86):
        pyautogui.write('biscoito 18')
        confirma_viagem()
    if(numero_ilha==87):
        pyautogui.write('biscoito 21')
        confirma_viagem()
    if(numero_ilha==88):
        pyautogui.write('bolacha 03')
        confirma_viagem()
    if(numero_ilha==89):
        pyautogui.write('bolacha 06')
        confirma_viagem()
    if(numero_ilha==90):
        pyautogui.write('bolacha 09')
        confirma_viagem()
    if(numero_ilha==91):
        pyautogui.write('bolacha 12')
        confirma_viagem()
    if(numero_ilha==92):
        pyautogui.write('bolacha 15')
        confirma_viagem()
    if(numero_ilha==93):
        pyautogui.write('bolacha 18')
        confirma_viagem()
    if(numero_ilha==94):
        pyautogui.write('bolacha 21')
        confirma_viagem()
    if(numero_ilha==95):
        pyautogui.write('polvilho 03')
        confirma_viagem()
    if(numero_ilha==96):
        pyautogui.write('polvilho 06')
        confirma_viagem()
    if(numero_ilha==97):
        pyautogui.write('polvilho 09')
        confirma_viagem()
    if(numero_ilha==98):
        pyautogui.write('polvilho 12')
        confirma_viagem()
    if(numero_ilha==99):
        pyautogui.write('polvilho 15')
        confirma_viagem()
    if(numero_ilha==100):
        pyautogui.write('polvilho 18')
        confirma_viagem()
    if(numero_ilha==101):
        pyautogui.write('polvilho 21')
        confirma_viagem()
    if(numero_ilha==102):
        pyautogui.write('cookie 03')
        confirma_viagem()
    if(numero_ilha==103):
        pyautogui.write('cookie 06')
        confirma_viagem()
    if(numero_ilha==104):
        pyautogui.write('cookie 09')
        confirma_viagem()
    if(numero_ilha==105):
        pyautogui.write('cookie 12')
        confirma_viagem()
    if(numero_ilha==106):
        pyautogui.write('cookie 15')
        confirma_viagem()
    if(numero_ilha==107):
        pyautogui.write('cookie 18')
        confirma_viagem()
    if(numero_ilha==108):
        pyautogui.write('cookie 21')
        confirma_viagem()
    if(numero_ilha==109):
        pyautogui.write('rosca 03')
        confirma_viagem()
    if(numero_ilha==110):
        pyautogui.write('rosca 06')
        confirma_viagem()
    if(numero_ilha==111):
        pyautogui.write('rosca 09')
        confirma_viagem()
    if(numero_ilha==112):
        pyautogui.write('rosca 12')
        confirma_viagem()
    if(numero_ilha==113):
        pyautogui.write('rosca 15')
        confirma_viagem()
    if(numero_ilha==114):
        pyautogui.write('rosca 18')
        confirma_viagem()
    if(numero_ilha==115):
        pyautogui.write('rosca 21')
        confirma_viagem()
    if(numero_ilha==116):
        pyautogui.write('bolo 03')
        confirma_viagem()
    if(numero_ilha==117):
        pyautogui.write('bolo 06')
        confirma_viagem()
    if(numero_ilha==118):
        pyautogui.write('bolo 09')
        confirma_viagem()
    if(numero_ilha==119):
        pyautogui.write('bolo 12')
        confirma_viagem()
    if(numero_ilha==120):
        pyautogui.write('bolo 15')
        confirma_viagem()
    
    time.sleep(3)
    timed_out=0
    while(True):
        
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence=0.8) != None:
            return
        if (timed_out==40):
            pyautogui.press('esc')
            time.sleep(0.3)
            click(995, 256,False)
            time.sleep(1)
            viaja_prox(numero_ilha)
            return
        if (timed_out==60):
            deu_merda()
        else:
            time.sleep(0.1)
            
def confirma_viagem():#after the viaja_prox island tipe the name of your island this funcion click to travel
    
    time.sleep(1)
    click(281,318, False)
    time.sleep(1)
    click(305,863, False)
 
def logout():#try to log back in game

    while(True):
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png' , confidence = 0.8) != None:
            click(956, 644, True )#if u are in the login screen
            time.sleep(2)
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\No_wifi.png' , confidence = 0.8) != None:
            location = locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\No_wifi.png' , confidence = 0.8)
            pyautogui.click(location)#if u are stil ofline, the bot will keep tring to conect
            time.sleep(2)

        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\C_S.png', confidence = 0.8) != None:
            click(948, 864, True)#if the bot have sucess and pass the login screen, he will log in your charater
            time.sleep(2)
            break

def deu_merda():#if anything go out of the normal this funcion is the responsible to help
    
    timed_out=0
    timed_out_2=0
    while(True):
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.9) != None:
            logout() 

        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Desmontado.png', confidence = 0.9) != None:
            pyautogui.press('s')
            time.sleep(0.3)
            pyautogui.press('a')
            time.sleep(5)

        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.6) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador_noite.png', confidence = 0.6) != None :
            a=pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.6)
            b=pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador_noite.png', confidence = 0.6)
            if (a == None): 
                if (b == None):
                    click(1049, 253, False)
                else:
                    pyautogui.click(b)
            else:
                pyautogui.click(a)
                
            time.sleep(1)
            viaja_prox(0)#pass the backup island 
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Ilha_pedra.png', confidence = 0.7)  != None :
                time.sleep(0.2)
                click(1014, 246, False)
                return
            else:
                timed_out_2+=1
                time.sleep(1)
                if(timed_out_2==3):
                    deu_merda()

        else:          
            click(32, 1079, True)
            time.sleep(1)
            timed_out+=1
            if timed_out==10:
                click(1009, 500, True) 

def inv_bau():
    time.sleep(0.2)
    click_arrasta(1590,550,93,373)#1slot
    time.sleep(0.2)
    click_arrasta(1672,550,175,373)#2slot
    time.sleep(0.2)
    click_arrasta(1748,550,252,373)#3slot
    time.sleep(0.2)
    click_arrasta(1830,550,337,373)#4slot
    time.sleep(0.2)
    click_arrasta(1590,632,413,373)#5slot
    time.sleep(0.2)
    click_arrasta(1672,632,93,452)#6slot
    time.sleep(0.2)
    click_arrasta(1748,632,175,452)#7slot
    time.sleep(0.2)
    click_arrasta(1830,632,252,452)#8slot
    time.sleep(0.2)
    click_arrasta(1590,711,337,452)#9slot
    time.sleep(0.2)
    click_arrasta(1672,711,413,452)#10slot
    time.sleep(0.2)
    click_arrasta(1748,711,93,531)#11slot
    time.sleep(0.2)
    click_arrasta(1830,711,175,531)#12slot
    time.sleep(0.2)
    click_arrasta(1590,789,252,531)#13slot
    time.sleep(0.2)
    click_arrasta(1672,789,337,531)#14slot
    time.sleep(0.2)
    click_arrasta(1748,789,413,531)#15slot
    time.sleep(0.2)
    click_arrasta(1830,789,93,612)#16slot
    time.sleep(0.2)
    click_arrasta(1590,873,175,612)#17slot
    time.sleep(0.2)
    click_arrasta(1672,873,252,612)#18slot
    time.sleep(0.2)
    click_arrasta(1748,873,337,612)#19slot
    time.sleep(0.2)
    click_arrasta(1830,873,413,612)#20slot
    time.sleep(0.2)
    click_arrasta(1590,930,93,675)#21slot
    time.sleep(0.2)
    click_arrasta(1672,930,175,675)#22slot
    time.sleep(0.2)
    click_arrasta(1748,930,252,675)#23slot
    time.sleep(0.2)
    click_arrasta(1830,930,337,675)#24slot
    time.sleep(0.2)

def guardar_itens(x):
    timed_out=0
    while(True):
        if (timed_out==80):
            deu_merda()
            return
        if (pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Ilha_fort.png')) != None:
            time.sleep(0.2)
            click(1622, 0, False)
            break
        else:
            timed_out+=1
            time.sleep(0.1)
    timed_out=0
    while(True): 
        if (pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\inventario.png', confidence = 0.8) != None):
            if (x != 1):
                time.sleep(0.3)
                qual_bau(2)
                time.sleep(0.3)
                click(471,897, False)#rola fim do bau
                inv_bau()#passa os itens 
                click(319,272,False)#acumular no bau
                time.sleep(0.3)
                click(431,273,False)#classificar no bau
                time.sleep(0.3)
                click(1811,453,False)#classificar no inventario
                time.sleep(0.3)
                inv_bau()#passa os itens dnv
                time.sleep(0.5)
                break
            else:
                break
        elif (pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\banco.png') != None):
            pyautogui.press('esc')
            time.sleep(1)
            click(1098, 370, False)
            time.sleep(1)
        else:
            timed_out+=1
            time.sleep(0.1)
        if(timed_out==50):
            deu_merda()

def qual_bau(bau):#go to 2 slot of the chest
    click(141,272,False)
    time.sleep(0.5)
    if (bau==1):
        click(112, 330, False )
    if (bau==2):
        click(133,349, False)

def pegar_diario(diario):
    pegou = False
    qual_bau(1)
    time.sleep(0.3)
    if(diario==1):
        time.sleep(1)
        click_arrasta(89,345,1590,551)
        time.sleep(0.5)
        pegou = True
    if(diario==21):
        time.sleep(1)
        click_arrasta(91,434,1590,551)
        time.sleep(0.5)
        pegou = True
    if(diario==41):
        time.sleep(1)
        click_arrasta(173,351,1590,551)
        time.sleep(0.5)
        pegou = True
    if(diario==61):
        time.sleep(1)
        click_arrasta(173,431,1590,551)
        time.sleep(0.5)
        pegou = True
    if(diario==81):
        time.sleep(1)
        click_arrasta(254,351,1590,551)
        time.sleep(0.5)
        pegou = True
    if(diario==101):
        time.sleep(1)
        click_arrasta(257,428,1590,551)
        time.sleep(0.5)
        pegou = True
    if (pegou==True):
        volta_trabalhador()
        time.sleep(0.4)
        pyautogui.press('i')
        time.sleep(0.3)
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\imbuidor.png', confidence = 0.7) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\flecheiro.png', confidence = 0.7) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\ferreiro.png', confidence = 0.7) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\ferreiro_t7.png', confidence = 0.7) !=None:
            return pegou
        else:
            pyautogui.press('i')
            click(60, 1079, True)
            time.sleep(1)
            click(1778, 1, False)
            time.sleep(5)
            pegar_diario(diario)

    if (pegou==False):
        deu_merda()
        return pegou

def tempo_ilhas(t_comeco,t_fim,x):
    gasto = t_fim - t_comeco
    hora_atual=time.localtime()
    with open("tempo_ilha.txt", "a") as text_file:
        text_file.write("ilha: %d tempo: %.2f hora: %d:%d:%d \n" %(x-1, gasto, hora_atual.tm_hour, hora_atual.tm_min, hora_atual.tm_sec))
ft=True
for x,y in GUI.numero_ilha.items():# here is where the magic happens
    if(y):
        if (x==1):
            open("tempo_ilha.txt", "a")
            os.remove("tempo_ilha.txt")
            viaja_prox(-1)
            guardar_itens(x) 
            pegar_diario(x)
        if (x == 21 and ft==False):
            t_fim = time.time()
            tempo_ilhas(t_comeco,t_fim,x)
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 41 and ft==False):
            t_fim = time.time()
            tempo_ilhas(t_comeco,t_fim,x)
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 61 and ft==False):
            t_fim = time.time()
            tempo_ilhas(t_comeco,t_fim,x)
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 81 and ft==False):
            t_fim = time.time()
            tempo_ilhas(t_comeco,t_fim,x)
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 101 and ft==False):
            t_fim = time.time()
            tempo_ilhas(t_comeco,t_fim,x)
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)

    if(y==False):
        continue
    if(x != 1 and 21 and 41 and 61 and 81 and 101 and ft==False):
        t_fim = time.time()
        tempo_ilhas(t_comeco,t_fim,x)
    viaja_prox(x)
    t_comeco = time.time()
    ft=False
    error_vai = vai_trabalhador()
    error_faz = faz_trabalhador()

    while(error_vai or error_faz):#in case of any error, like low internet conection
        viaja_prox(x)
        time.sleep(2)
        error_vai = vai_trabalhador()
        error_faz = faz_trabalhador()
    
    time.sleep(1)
    volta_trabalhador()
    time.sleep(1)

    if (x == 120):
        tempo_ilhas(t_comeco,t_fim,x)
        viaja_prox(-1)
        guardar_itens(x)
        print('Ilhas Finalizadas')
        os.system('shutdown -s')
        break
    