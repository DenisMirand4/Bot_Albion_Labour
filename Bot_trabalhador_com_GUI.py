from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller
from tkinter import Event
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import B, CBox, Check



class GUI:
    def toggle_imb(window,x):#funcion that toggle all the IMBUIDORES
        if (x==0):
            window[1].update(False)
            window[2].update(False)
            window[3].update(False)
            window[4].update(False)
            window[5].update(False)
            window[6].update(False)
            window[7].update(False)
            window[8].update(False)
            window[9].update(False)
            window[10].update(False)
            window[11].update(False)
            window[12].update(False)
            window[13].update(False)
            window[14].update(False)
            window[15].update(False)
            window[16].update(False)
            window[17].update(False)
            window[18].update(False)
            window[19].update(False)
            window[20].update(False)
            window[21].update(False)
            window[22].update(False)
            window[23].update(False)
            window[24].update(False)
            window[25].update(False)
            window[26].update(False)
            window[27].update(False)
            window[28].update(False)
            window[29].update(False)
            window[30].update(False)
            window[31].update(False)
            window[32].update(False)
            window[33].update(False)
            window[34].update(False)
            window[35].update(False)
            window[36].update(False)
            window[37].update(False)
            window[38].update(False)
            window[39].update(False)
            window[40].update(False)
        if(x==1):
            window[1].update(True)
            window[2].update(True)
            window[3].update(True)
            window[4].update(True)
            window[5].update(True)
            window[6].update(True)
            window[7].update(True)
            window[8].update(True)
            window[9].update(True)
            window[10].update(True)
            window[11].update(True)
            window[12].update(True)
            window[13].update(True)
            window[14].update(True)
            window[15].update(True)
            window[16].update(True)
            window[17].update(True)
            window[18].update(True)
            window[19].update(True)
            window[20].update(True)
            window[21].update(True)
            window[22].update(True)
            window[23].update(True)
            window[24].update(True)
            window[25].update(True)
            window[26].update(True)
            window[27].update(True)
            window[28].update(True)
            window[29].update(True)
            window[30].update(True)
            window[31].update(True)
            window[32].update(True)
            window[33].update(True)
            window[34].update(True)
            window[35].update(True)
            window[36].update(True)
            window[37].update(True)
            window[38].update(True)
            window[39].update(True)
            window[40].update(True)

    def toggle_fle(window,a):#funcion that toggle all the FLECHEIRO

        if(a==0):
            window[41].update(False)
            window[42].update(False)
            window[43].update(False)
            window[44].update(False)
            window[45].update(False)
            window[46].update(False)
            window[47].update(False)
            window[48].update(False)
            window[49].update(False)
            window[50].update(False)
            window[51].update(False)
            window[52].update(False)
            window[53].update(False)
            window[54].update(False)
            window[55].update(False)
            window[56].update(False)
            window[57].update(False)
            window[58].update(False)
            window[59].update(False)
            window[60].update(False)
            window[61].update(False)
            window[62].update(False)
            window[63].update(False)
            window[64].update(False)
            window[65].update(False)
            window[66].update(False)
            window[67].update(False)
            window[68].update(False)
            window[69].update(False)
            window[70].update(False)
            window[71].update(False)
            window[72].update(False)
            window[73].update(False)
            window[74].update(False)
            window[75].update(False)
            window[76].update(False)
            window[77].update(False)
            window[78].update(False)
            window[79].update(False)
            window[80].update(False)
        if(a==1):
            window[41].update(True)
            window[42].update(True)
            window[43].update(True)
            window[44].update(True)
            window[45].update(True)
            window[46].update(True)
            window[47].update(True)
            window[48].update(True)
            window[49].update(True)
            window[50].update(True)
            window[51].update(True)
            window[52].update(True)
            window[53].update(True)
            window[54].update(True)
            window[55].update(True)
            window[56].update(True)
            window[57].update(True)
            window[58].update(True)
            window[59].update(True)
            window[60].update(True)
            window[61].update(True)
            window[62].update(True)
            window[63].update(True)
            window[64].update(True)
            window[65].update(True)
            window[66].update(True)
            window[67].update(True)
            window[68].update(True)
            window[69].update(True)
            window[70].update(True)
            window[71].update(True)
            window[72].update(True)
            window[73].update(True)
            window[74].update(True)
            window[75].update(True)
            window[76].update(True)
            window[77].update(True)
            window[78].update(True)
            window[79].update(True)
            window[80].update(True)

    def toggle_fer(window,k):#funcion that toggle all the FERREIRO

        if(k==0):
            window[81].update(False)
            window[82].update(False)
            window[83].update(False)
            window[84].update(False)
            window[85].update(False)
            window[86].update(False)
            window[87].update(False)
            window[88].update(False)
            window[89].update(False)
            window[90].update(False)
            window[91].update(False)
            window[92].update(False)
            window[93].update(False)
            window[94].update(False)
            window[95].update(False)
            window[96].update(False)
            window[97].update(False)
            window[98].update(False)
            window[99].update(False)
            window[100].update(False)
            window[101].update(False)
            window[102].update(False)
            window[103].update(False)
            window[104].update(False)
            window[105].update(False)
            window[106].update(False)
            window[107].update(False)
            window[108].update(False)
            window[109].update(False)
            window[110].update(False)
            window[111].update(False)
            window[112].update(False)
            window[113].update(False)
            window[114].update(False)
            window[115].update(False)
            window[116].update(False)
            window[117].update(False)
            window[118].update(False)
            window[119].update(False)
            window[120].update(False)
        if(k==1):
            window[81].update(True)
            window[82].update(True)
            window[83].update(True)
            window[84].update(True)
            window[85].update(True)
            window[86].update(True)
            window[87].update(True)
            window[88].update(True)
            window[89].update(True)
            window[90].update(True)
            window[91].update(True)
            window[92].update(True)
            window[93].update(True)
            window[94].update(True)
            window[95].update(True)
            window[96].update(True)
            window[97].update(True)
            window[98].update(True)
            window[99].update(True)
            window[100].update(True)
            window[101].update(True)
            window[102].update(True)
            window[103].update(True)
            window[104].update(True)
            window[105].update(True)
            window[106].update(True)
            window[107].update(True)
            window[108].update(True)
            window[109].update(True)
            window[110].update(True)
            window[111].update(True)
            window[112].update(True)
            window[113].update(True)
            window[114].update(True)
            window[115].update(True)
            window[116].update(True)
            window[117].update(True)
            window[118].update(True)
            window[119].update(True)
            window[120].update(True)

    biscoito_imb = [
        [sg.Text('Biscoito1  '),sg.CBox('',default=True,key=1)],
        [sg.Text('Biscoito 4 '),sg.CBox('',default=True,key=2)],
        [sg.Text('Biscoito 7 '),sg.CBox('',default=True,key=3)],
        [sg.Text('Biscoito 10'),sg.CBox('',default=True,key=4)],
        [sg.Text('Biscoito 13'),sg.CBox('',default=True,key=5)],
        [sg.Text('Biscoito 16'),sg.CBox('',default=True,key=6)],
        [sg.Text('Biscoito 19'),sg.CBox('',default=True,key=7)],]

    bolacha_imb =[
        [sg.Text('Bolacha 01'),sg.CBox('',default=True,key=8)],
        [sg.Text('Bolacha 04'),sg.CBox('',default=True,key=9)],
        [sg.Text('Bolacha 07'),sg.CBox('',default=True,key=10)],
        [sg.Text('Bolacha 10'),sg.CBox('',default=True,key=11)],
        [sg.Text('Bolacha 13'),sg.CBox('',default=True,key=12)],
        [sg.Text('Bolacha 16'),sg.CBox('',default=True,key=13)],
        [sg.Text('Bolacha 19'),sg.CBox('',default=True,key=14)],]

    polvilho_imb = [
        [sg.Text('Polvilho 01'),sg.CBox('',default=True,key=15)],
        [sg.Text('Polvilho 04'),sg.CBox('',default=True,key=16)],
        [sg.Text('Polvilho 07'),sg.CBox('',default=True,key=17)],
        [sg.Text('Polvilho 10'),sg.CBox('',default=True,key=18)],
        [sg.Text('Polvilho 13'),sg.CBox('',default=True,key=19)],
        [sg.Text('Polvilho 16'),sg.CBox('',default=True,key=20)],
        [sg.Text('Polvilho 19'),sg.CBox('',default=True,key=21)],]

    cookie_imb = [
        [sg.Text('Cookie 01'),sg.CBox('',default=True,key=22)],
        [sg.Text('Cookie 04'),sg.CBox('',default=True,key=23)],
        [sg.Text('Cookie 07'),sg.CBox('',default=True,key=24)],
        [sg.Text('Cookie 10'),sg.CBox('',default=True,key=25)],
        [sg.Text('Cookie 13'),sg.CBox('',default=True,key=26)],
        [sg.Text('Cookie 16'),sg.CBox('',default=True,key=27)],
        [sg.Text('Cookie 19'),sg.CBox('',default=True,key=28)],]

    rosca_imb = [
        [sg.Text('Rosca 01'),sg.CBox('',default=True,key=29)],
        [sg.Text('Rosca 04'),sg.CBox('',default=True,key=30)],
        [sg.Text('Rosca 07'),sg.CBox('',default=True,key=31)],
        [sg.Text('Rosca 10'),sg.CBox('',default=True,key=32)],
        [sg.Text('Rosca 13'),sg.CBox('',default=True,key=33)],
        [sg.Text('Rosca 16'),sg.CBox('',default=True,key=34)],
        [sg.Text('Rosca 19'),sg.CBox('',default=True,key=35)],]

    bolo_imb = [
        [sg.Text('Bolo 01'),sg.CBox('',default=True,key=36)],
        [sg.Text('Bolo 04'),sg.CBox('',default=True,key=37)],
        [sg.Text('Bolo 07'),sg.CBox('',default=True,key=38)],
        [sg.Text('Bolo 10'),sg.CBox('',default=True,key=39)],
        [sg.Text('Bolo 13'),sg.CBox('',default=True,key=40)],]

    biscoito_fle = [
        [sg.Text('Biscoito2  '),sg.CBox('',default=True,key=41)],
        [sg.Text('Biscoito 5 '),sg.CBox('',default=True,key=42)],
        [sg.Text('Biscoito 8 '),sg.CBox('',default=True,key=43)],
        [sg.Text('Biscoito 11'),sg.CBox('',default=True,key=44)],
        [sg.Text('Biscoito 14'),sg.CBox('',default=True,key=45)],
        [sg.Text('Biscoito 17'),sg.CBox('',default=True,key=46)],
        [sg.Text('Biscoito 20'),sg.CBox('',default=True,key=47)],]

    bolacha_fle = [
        [sg.Text('Bolacha 02'),sg.CBox('',default=True,key=48)],
        [sg.Text('Bolacha 05'),sg.CBox('',default=True,key=49)],
        [sg.Text('Bolacha 08'),sg.CBox('',default=True,key=50)],
        [sg.Text('Bolacha 11'),sg.CBox('',default=True,key=51)],
        [sg.Text('Bolacha 14'),sg.CBox('',default=True,key=52)],
        [sg.Text('Bolacha 17'),sg.CBox('',default=True,key=53)],
        [sg.Text('Bolacha 20'),sg.CBox('',default=True,key=54)],]

    polvilho_fle = [
        [sg.Text('Polvilho 02'),sg.CBox('',default=True,key=55)],
        [sg.Text('Polvilho 05'),sg.CBox('',default=True,key=56)],
        [sg.Text('Polvilho 08'),sg.CBox('',default=True,key=57)],
        [sg.Text('Polvilho 11'),sg.CBox('',default=True,key=58)],
        [sg.Text('Polvilho 14'),sg.CBox('',default=True,key=59)],
        [sg.Text('Polvilho 17'),sg.CBox('',default=True,key=60)],
        [sg.Text('Polvilho 20'),sg.CBox('',default=True,key=61)],]

    cookie_fle = [
        [sg.Text('Cookie 02'),sg.CBox('',default=True,key=62)],
        [sg.Text('Cookie 05'),sg.CBox('',default=True,key=63)],
        [sg.Text('Cookie 08'),sg.CBox('',default=True,key=64)],
        [sg.Text('Cookie 11'),sg.CBox('',default=True,key=65)],
        [sg.Text('Cookie 14'),sg.CBox('',default=True,key=66)],
        [sg.Text('Cookie 17'),sg.CBox('',default=True,key=67)],
        [sg.Text('Cookie 20'),sg.CBox('',default=True,key=68)],]

    rosca_fle = [
        [sg.Text('Rosca 02'),sg.CBox('',default=True,key=69)],
        [sg.Text('Rosca 05'),sg.CBox('',default=True,key=70)],
        [sg.Text('Rosca 08'),sg.CBox('',default=True,key=71)],
        [sg.Text('Rosca 11'),sg.CBox('',default=True,key=72)],
        [sg.Text('Rosca 14'),sg.CBox('',default=True,key=73)],
        [sg.Text('Rosca 17'),sg.CBox('',default=True,key=74)],
        [sg.Text('Rosca 20'),sg.CBox('',default=True,key=75)],]

    bolo_fle = [
        [sg.Text('Bolo 02'),sg.CBox('',default=True,key=76)],
        [sg.Text('Bolo 05'),sg.CBox('',default=True,key=77)],
        [sg.Text('Bolo 08'),sg.CBox('',default=True,key=78)],
        [sg.Text('Bolo 11'),sg.CBox('',default=True,key=79)],
        [sg.Text('Bolo 14'),sg.CBox('',default=True,key=80)],]

    biscoito_fer = [
        [sg.Text('Biscoito3  '),sg.CBox('',default=True,key=81)],
        [sg.Text('Biscoito 6 '),sg.CBox('',default=True,key=82)],
        [sg.Text('Biscoito 9 '),sg.CBox('',default=True,key=83)],
        [sg.Text('Biscoito 12'),sg.CBox('',default=True,key=84)],
        [sg.Text('Biscoito 15'),sg.CBox('',default=True,key=85)],
        [sg.Text('Biscoito 18'),sg.CBox('',default=True,key=86)],
        [sg.Text('Biscoito 21'),sg.CBox('',default=True,key=87)],]

    bolacha_fer = [
        [sg.Text('Bolacha 03'),sg.CBox('',default=True,key=88)],
        [sg.Text('Bolacha 06'),sg.CBox('',default=True,key=89)],
        [sg.Text('Bolacha 09'),sg.CBox('',default=True,key=90)],
        [sg.Text('Bolacha 12'),sg.CBox('',default=True,key=91)],
        [sg.Text('Bolacha 15'),sg.CBox('',default=True,key=92)],
        [sg.Text('Bolacha 18'),sg.CBox('',default=True,key=93)],
        [sg.Text('Bolacha 21'),sg.CBox('',default=True,key=94)],]

    polvilho_fer = [
        [sg.Text('Polvilho 03'),sg.CBox('',default=True,key=95)],
        [sg.Text('Polvilho 06'),sg.CBox('',default=True,key=96)],
        [sg.Text('Polvilho 09'),sg.CBox('',default=True,key=97)],
        [sg.Text('Polvilho 12'),sg.CBox('',default=True,key=98)],
        [sg.Text('Polvilho 15'),sg.CBox('',default=True,key=99)],
        [sg.Text('Polvilho 18'),sg.CBox('',default=True,key=100)],
        [sg.Text('Polvilho 21'),sg.CBox('',default=True,key=101)],]

    cookie_fer = [
        [sg.Text('Cookie 03'),sg.CBox('',default=True,key=102)],
        [sg.Text('Cookie 06'),sg.CBox('',default=True,key=103)],
        [sg.Text('Cookie 09'),sg.CBox('',default=True,key=104)],
        [sg.Text('Cookie 12'),sg.CBox('',default=True,key=105)],
        [sg.Text('Cookie 15'),sg.CBox('',default=True,key=106)],
        [sg.Text('Cookie 18'),sg.CBox('',default=True,key=107)],
        [sg.Text('Cookie 21'),sg.CBox('',default=True,key=108)],]

    rosca_fer = [
        [sg.Text('Rosca 03'),sg.CBox('',default=True,key=109)],
        [sg.Text('Rosca 06'),sg.CBox('',default=True,key=110)],
        [sg.Text('Rosca 09'),sg.CBox('',default=True,key=111)],
        [sg.Text('Rosca 12'),sg.CBox('',default=True,key=112)],
        [sg.Text('Rosca 15'),sg.CBox('',default=True,key=113)],
        [sg.Text('Rosca 18'),sg.CBox('',default=True,key=114)],
        [sg.Text('Rosca 21'),sg.CBox('',default=True,key=115)],]

    bolo_fer = [
        [sg.Text('Bolo 03'),sg.CBox('',default=True,key=116)],
        [sg.Text('Bolo 06'),sg.CBox('',default=True,key=117)],
        [sg.Text('Bolo 09'),sg.CBox('',default=True,key=118)],
        [sg.Text('Bolo 12'),sg.CBox('',default=True,key=119)],
        [sg.Text('Bolo 15'),sg.CBox('',default=True,key=120)],]

    layout= [
        #here i use column to separate the 3 tipes of labour
        [sg.Button('Start') ,sg.Button('Toggle IMBUIDOR'), sg.Button('Toggle FLECHEIRO'), sg.Button('Toggle FERREIRO')],
        [sg.Text('========================================IMBUIDOR========================================')],
        [sg.Column(biscoito_imb),sg.Column(bolacha_imb),sg.Column(polvilho_imb),sg.Column(cookie_imb),sg.Column(rosca_imb),sg.Column(bolo_imb)],
        [sg.Text('========================================FLECHEIRO=======================================')],
        [sg.Column(biscoito_fle, key=('imbuidor')),sg.Column(bolacha_fle),sg.Column(polvilho_fle),sg.Column(cookie_fle),sg.Column(rosca_fle),sg.Column(bolo_fle)],
        [sg.Text('========================================FERREIRO========================================')],
        [sg.Column(biscoito_fer),sg.Column(bolacha_fer),sg.Column(polvilho_fer),sg.Column(cookie_fer),sg.Column(rosca_fer),sg.Column(bolo_fer)]]

    window = sg.Window("Labour Manager", layout)
    x=0
    y=1
    a=0
    b=1
    k=0
    q=1
    while (True):#The loop that update your window
   
        event, numero_ilha = window.read()

        if event in ('Start', sg.WIN_CLOSED):
            break
        if event in ('Toggle IMBUIDOR'):
            toggle_imb(window,x)
            x = x + y#this is a way to change 2 variables without use a trird one
            y = x - y
            x = x - y
        if event in ('Toggle FLECHEIRO'):
            toggle_fle(window,a)
            a = a + b
            b = a - b
            a = a - b
        if event in ('Toggle FERREIRO'):
            toggle_fer(window,k)
            k = k + q
            q = k - q
            k = k - q
                
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
            
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Topo_viajador.png', confidence = 0.5) != None :
            click(60, 1079, True)
            time.sleep(1.5)
            click(1082, 264, False)
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
            break
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
            time.sleep(0.1)
            return False
        else:
            time.sleep(0.1)
            timed_out+=1

def viaja_prox(numero_ilha):#type the name of the island u want to travel
    timed_out=0             ##If u want to use u need to change the name of the islands to match with your own islands
    while(True):            ###Notice the number of 'numero_ilha' plus one in each island
        timed_out+=1
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Comprar Viagem.png', confidence=0.8) != None:
            click(275,291, False)
            pyautogui.write('')
            time.sleep(0.2)
            break
        if(timed_out==10):
            deu_merda()
        time.sleep(0.5)
    if(numero_ilha == -1):
        pyautogui.write('Fort Stearling Craft')
        confirma_viagem()
    if(numero_ilha == 0):
        pyautogui.write('Pedra refino')#Your backup point
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
    while(True):
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence=0.8) != None:
            return

def confirma_viagem():#after the viaja_prox island tipe the name of your island this funcion click to travel
    
    time.sleep(0.1)
    click(281,318, False)
    time.sleep(0.1)
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
    while(True):
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.9) != None:
            logout() 

        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Topo_viajador.png', confidence = 0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Topo_viajador_noite.png', confidence = 0.5) != None :
            a=pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.6)
            b=pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Topo_viajador.png', confidence = 0.6)
            c=pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Topo_viajador_noite.png', confidence = 0.6)
            if (a == None): 
                if (b == None):
                    if (c == None):
                        click(1049, 253, False)
                    else:
                        pyautogui.click(c)
                else:
                    pyautogui.click(b)
            else:
                pyautogui.click(a)
                

            time.sleep(1)
            #click(1049, 253, False)
            viaja_prox(0)#pass the backup island 
            time.sleep(3)
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Ilha_pedra.png', confidence = 0.7)  != None :
                time.sleep(0.2)
                click(1014, 246, False)
                return
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
        click_arrasta(89,345,1590,551)
        pegou = True
    if(diario==21):
        click_arrasta(91,434,1590,551)
        pegou = True
    if(diario==41):
        click_arrasta(173,351,1590,551)
        pegou = True
    if(diario==61):
        click_arrasta(173,431,1590,551)
        pegou = True
    if(diario==81):
        click_arrasta(254,351,1590,551)
        pegou = True
    if(diario==101):
        click_arrasta(257,428,1590,551)
        pegou = True
    if (pegou==True):
        volta_trabalhador()
        return pegou
    if (pegou==False):
        deu_merda()
        return pegou

for x,y in GUI.numero_ilha.items():# here is where the magic happens
    if(y):
        if (x==1):
            viaja_prox(-1)
            guardar_itens(x) 
            pegar_diario(x)
        if (x == 21):
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 41):
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 61):
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 81):
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)
        if (x == 101):
            viaja_prox(-1)
            guardar_itens(x)
            pegar_diario(x)

    if(y==False):
        continue
    viaja_prox(x)
    error_vai = vai_trabalhador()
    error_faz = faz_trabalhador()

    while(error_vai or error_faz):#in case of any error, like low internet conection
        viaja_prox(x)
        time.sleep(3)
        error_vai = vai_trabalhador()
        error_faz = faz_trabalhador()
    
    time.sleep(1)
    volta_trabalhador()
    time.sleep(1)

    if (x == 120):
        viaja_prox(-1)
        guardar_itens(x)
        print('Ilhas Finalizadas')
        break