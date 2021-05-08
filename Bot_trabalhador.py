from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller



def click(x,y):#single click
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_arrasta(x,y,a,b):#this simulate a click with shift or alt in game, basically the mouse teleport from (x,y) to (a,b)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.SetCursorPos((a,b))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.01)

def vai_trabalhador():# walk from the start of the island till the laborers
    
    for x in range(10):#
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence=0.8) != None:
               
                break
        else:
            time.sleep(0.5)
        
    for x in range(10):
        time.sleep(1)
        print('antes locate: \n')
        print(pyautogui.position())
        #if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Batata dia.png', confidence=0.45) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Batata.png', confidence=0.45) != None:
        time.sleep(1)
        print('antes click')
        print(pyautogui.position())
        click(1578, 0)
        print('depois click')
        print(pyautogui.position())
        break
        #else:
         #   time.sleep(1)

    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Runa.png', confidence=0.45) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Runa Dia.png', confidence=0.45) != None:
            time.sleep(2)
            click(1578, 0)
            break
        else:
            time.sleep(1)

    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Pedras.png', confidence=0.45) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Pedras Dia.png', confidence=0.45) != None:
            time.sleep(2)
            click(1294, 302)
            break
        else:
            time.sleep(1)

    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Porta.png', confidence=0.45) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Porta Dia.png', confidence=0.45) != None:
            time.sleep(2)
            click(1619, 0)
            break
        else:
            time.sleep(1)

def volta_trabalhador():
    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha.png', confidence=0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha Dia.png', confidence=0.45) != None:
            time.sleep(2)
            click(0, 1028)
            break
        else:
            time.sleep(1)

    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Lamparina.png', confidence=0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Lamparina Dia.png', confidence=0.5) != None:
            time.sleep(2)
            click(0, 1069)
            break
        else:
            time.sleep(1)

    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Runa_volta.png', confidence=0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Runa_volta Dia.png', confidence=0.5) != None:
            time.sleep(2)
            click(235,1049)
            break
        else:
            time.sleep(1)

    for x in range(10):
        time.sleep(1)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Lanterna.png', confidence=0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Lanterna Noite.png', confidence=0.5)  != None:
            time.sleep(2)
            click(358, 762)
            break
        else:
            time.sleep(1)

def coloca_diario():
    for x in range(4):
        time.sleep(0.2)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Take All.png', confidence=0.8) != None:
            click(216, 861)#colhe recursos
            break
        else:
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Deixar Diario.png', confidence=0.8) != None:
                break # caso nao tenha recurso
            else:
                if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Esta trabalho.png', confidence=0.8) != None:
                    return # caso ainda esteja trabalhando
                else:
                    if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence=0.8) != None: 
                        click(1858, 0)
                        time.sleep(3)
                        deu_merda()
                        return #caso nao ache o trabalhador
                    else:
                        time.sleep(0.3)

    for x in range(4):
        time.sleep(0.2)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Deixar Diario.png', confidence=0.8) != None:
            time.sleep(0.2)
            click_arrasta(1585, 548, 207, 659)#coloca o diário
            time.sleep(0.2)
            break
        else:
            time.sleep(0.5)

    for x in range(4):
        time.sleep(0.2)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Aceitar.png', confidence=0.8) != None:
            click(121, 866)#confirma o diário
            time.sleep(0.3)
            break
        else:
            time.sleep(0.5)

def viaja_prox(numero_ilha):
    for x in range(10):
        time.sleep(0.5)
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Comprar Viagem.png', confidence=0.8) != None:
            click(275,291)
            pyautogui.write('')
            time.sleep(0.2)
            break
        [0,1,2,3,4,5]
    if(numero_ilha == 1):
        pyautogui.write('biscoito1')
        confirma_viajem()
    if(numero_ilha == 2):
        pyautogui.write('biscoito 4')
        confirma_viajem()
    if(numero_ilha == 3):
        pyautogui.write('biscoito 7')
        confirma_viajem()
    if(numero_ilha == 4):
        pyautogui.write('biscoito 10')
        confirma_viajem()
    if(numero_ilha == 5):
        pyautogui.write('biscoito 13')
        confirma_viajem()
    if(numero_ilha == 6):
        pyautogui.write('biscoito 16')
        confirma_viajem()
    if(numero_ilha == 7):
        pyautogui.write('biscoito 19')
        confirma_viajem()
    if(numero_ilha == 8):
        pyautogui.write('bolacha 01')
        confirma_viajem()
    if(numero_ilha == 9):
        pyautogui.write('bolacha 04')
        confirma_viajem()
    if(numero_ilha == 10):
        pyautogui.write('bolacha 07')
        confirma_viajem()
    if(numero_ilha == 11):
        pyautogui.write('bolacha 10')
        confirma_viajem()
    if(numero_ilha == 12):
        pyautogui.write('bolacha 13')
        confirma_viajem()
    if(numero_ilha == 13):
        pyautogui.write('bolacha 16')
        confirma_viajem()
    if(numero_ilha == 14):
        pyautogui.write('bolacha 19')
        confirma_viajem()
    if(numero_ilha == 15):
        pyautogui.write('polvilho 01')
        confirma_viajem()
    if(numero_ilha == 16):
        pyautogui.write('polvilho 04')
        confirma_viajem()
    if(numero_ilha == 17):
        pyautogui.write('polvilho 07')
        confirma_viajem()
    if(numero_ilha == 18):
        pyautogui.write('polvilho 10')
        confirma_viajem()
    if(numero_ilha == 19):
        pyautogui.write('polvilho 13')
        confirma_viajem()
    if(numero_ilha == 20):
        pyautogui.write('polvilho 16')
        confirma_viajem()
    if(numero_ilha == 21):
        pyautogui.write('polvilho 19')
        confirma_viajem()
    if(numero_ilha == 22):
        pyautogui.write('cookie 01')
        confirma_viajem()
    if(numero_ilha == 23):
        pyautogui.write('cookie 04')
        confirma_viajem()
    if(numero_ilha == 24):
        pyautogui.write('cookie 07')
        confirma_viajem()
    if(numero_ilha == 25):
        pyautogui.write('cookie 10')
        confirma_viajem()
    if(numero_ilha == 26):
        pyautogui.write('cookie 13')
        confirma_viajem()
    if(numero_ilha == 27):
        pyautogui.write('cookie 16')
        confirma_viajem()
    if(numero_ilha == 28):
        pyautogui.write('cookie 19')
        confirma_viajem()
    if(numero_ilha == 29):
        pyautogui.write('rosca 01')
        confirma_viajem()
    if(numero_ilha == 30):
        pyautogui.write('rosca 04')
        confirma_viajem()
    if(numero_ilha == 31):
        pyautogui.write('rosca 07')
        confirma_viajem()
    if(numero_ilha == 32):
        pyautogui.write('rosca 10')
        confirma_viajem()
    if(numero_ilha == 33):
        pyautogui.write('rosca 13')
        confirma_viajem()
    if(numero_ilha == 34):
        pyautogui.write('rosca 16')
        confirma_viajem()
    if(numero_ilha == 35):
        pyautogui.write('rosca 19')
        confirma_viajem()
    if(numero_ilha == 36):
        pyautogui.write('bolo 01')
        confirma_viajem()
    if(numero_ilha==37):
        pyautogui.write('bolo 04')
        confirma_viajem()
    if(numero_ilha==38):
        pyautogui.write('bolo 07')
        confirma_viajem()
    if(numero_ilha==39):
        pyautogui.write('bolo 10')
        confirma_viajem()
    if(numero_ilha==40):
        pyautogui.write('bolo 13')
        confirma_viajem()
    if(numero_ilha==41):
        pyautogui.write('biscoito2')
        confirma_viajem()
    if(numero_ilha==42):
        pyautogui.write('biscoito 5')
        confirma_viajem()
    if(numero_ilha==43):
        pyautogui.write('biscoito 8')
        confirma_viajem()
    if(numero_ilha==44):
        pyautogui.write('biscoito 11')
        confirma_viajem()
    if(numero_ilha==45):
        pyautogui.write('biscoito 14')
        confirma_viajem()
    if(numero_ilha==46):
        pyautogui.write('biscoito 17')
        confirma_viajem()
    if(numero_ilha==47):
        pyautogui.write('biscoito 20')
        confirma_viajem()
    if(numero_ilha==48):
        pyautogui.write('bolacha 02')
        confirma_viajem()
    if(numero_ilha==49):
        pyautogui.write('bolacha 05')
        confirma_viajem()
    if(numero_ilha==50):
        pyautogui.write('bolacha 08')
        confirma_viajem()
    if(numero_ilha==51):
        pyautogui.write('bolacha 11')
        confirma_viajem()
    if(numero_ilha==52):
        pyautogui.write('bolacha 14')
        confirma_viajem()
    if(numero_ilha==53):
        pyautogui.write('bolacha 17')
        confirma_viajem()
    if(numero_ilha==54):
        pyautogui.write('bolacha 20')
        confirma_viajem()
    if(numero_ilha==55):
        pyautogui.write('polvilho 02')
        confirma_viajem()
    if(numero_ilha==56):
        pyautogui.write('polvilho 05')
        confirma_viajem()
    if(numero_ilha==57):
        pyautogui.write('polvilho 08')
        confirma_viajem()
    if(numero_ilha==58):
        pyautogui.write('polvilho 11')
        confirma_viajem()
    if(numero_ilha==59):
        pyautogui.write('polvilho 14')
        confirma_viajem()
    if(numero_ilha==60):
        pyautogui.write('polvilho 17')
        confirma_viajem()
    if(numero_ilha==61):
        pyautogui.write('polvilho 20')
        confirma_viajem()
    if(numero_ilha==62):
        pyautogui.write('cookie 02')
        confirma_viajem()
    if(numero_ilha==63):
        pyautogui.write('cookie 05')
        confirma_viajem()
    if(numero_ilha==64):
        pyautogui.write('cookie 08')
        confirma_viajem()
    if(numero_ilha==65):
        pyautogui.write('cookie 11')
        confirma_viajem()
    if(numero_ilha==66):
        pyautogui.write('cookie 14')
        confirma_viajem()
    if(numero_ilha==67):
        pyautogui.write('cookie 17')
        confirma_viajem()
    if(numero_ilha==68):
        pyautogui.write('cookie 20')
        confirma_viajem()
    if(numero_ilha==69):
        pyautogui.write('rosca 02')
        confirma_viajem()
    if(numero_ilha==70):
        pyautogui.write('rosca 05')
        confirma_viajem()
    if(numero_ilha==71):
        pyautogui.write('rosca 08')
        confirma_viajem()    
    if(numero_ilha==72):
        pyautogui.write('rosca 11')
        confirma_viajem()    
    if(numero_ilha==73):
        pyautogui.write('rosca 14')
        confirma_viajem()    
    if(numero_ilha==74):
        pyautogui.write('rosca 17')
        confirma_viajem()    
    if(numero_ilha==75):
        pyautogui.write('rosca 20')
        confirma_viajem()    
    if(numero_ilha==76):
        pyautogui.write('bolo 02')
        confirma_viajem()    
    if(numero_ilha==77):
        pyautogui.write('bolo 05')
        confirma_viajem()    
    if(numero_ilha==78):
        pyautogui.write('bolo 08')
        confirma_viajem()    
    if(numero_ilha==79):
        pyautogui.write('bolo 11')
        confirma_viajem()    
    if(numero_ilha==80):
        pyautogui.write('bolo 14')
        confirma_viajem()   
    if(numero_ilha==81):
        pyautogui.write('biscoito3')
        confirma_viajem()    
    if(numero_ilha==82):
        pyautogui.write('biscoito 6')
        confirma_viajem()
    if(numero_ilha==83):
        pyautogui.write('biscoito 9')
        confirma_viajem()
    if(numero_ilha==84):
        pyautogui.write('biscoito 12')
        confirma_viajem()
    if(numero_ilha==85):
        pyautogui.write('biscoito 15')
        confirma_viajem()
    if(numero_ilha==86):
        pyautogui.write('biscoito 18')
        confirma_viajem()
    if(numero_ilha==87):
        pyautogui.write('biscoito 21')
        confirma_viajem()
    if(numero_ilha==88):
        pyautogui.write('bolacha 03')
        confirma_viajem()
    if(numero_ilha==89):
        pyautogui.write('bolacha 06')
        confirma_viajem()
    if(numero_ilha==90):
        pyautogui.write('bolacha 09')
        confirma_viajem()
    if(numero_ilha==91):
        pyautogui.write('bolacha 12')
        confirma_viajem()
    if(numero_ilha==92):
        pyautogui.write('bolacha 15')
        confirma_viajem()
    if(numero_ilha==93):
        pyautogui.write('bolacha 18')
        confirma_viajem()
    if(numero_ilha==94):
        pyautogui.write('bolacha 21')
        confirma_viajem()
    if(numero_ilha==95):
        pyautogui.write('polvilho 03')
        confirma_viajem()
    if(numero_ilha==96):
        pyautogui.write('polvilho 06')
        confirma_viajem()
    if(numero_ilha==97):
        pyautogui.write('polvilho 09')
        confirma_viajem()
    if(numero_ilha==98):
        pyautogui.write('polvilho 12')
        confirma_viajem()
    if(numero_ilha==99):
        pyautogui.write('polvilho 15')
        confirma_viajem()
    if(numero_ilha==100):
        pyautogui.write('polvilho 18')
        confirma_viajem()
    if(numero_ilha==101):
        pyautogui.write('polvilho 21')
        confirma_viajem()
    if(numero_ilha==102):
        pyautogui.write('cookie 03')
        confirma_viajem()
    if(numero_ilha==103):
        pyautogui.write('cookie 06')
        confirma_viajem()
    if(numero_ilha==104):
        pyautogui.write('cookie 09')
        confirma_viajem()
    if(numero_ilha==105):
        pyautogui.write('cookie 12')
        confirma_viajem()
    if(numero_ilha==106):
        pyautogui.write('cookie 15')
        confirma_viajem()
    if(numero_ilha==107):
        pyautogui.write('cookie 18')
        confirma_viajem()
    if(numero_ilha==108):
        pyautogui.write('cookie 21')
        confirma_viajem()
    if(numero_ilha==109):
        pyautogui.write('rosca 03')
        confirma_viajem()
    if(numero_ilha==110):
        pyautogui.write('rosca 06')
        confirma_viajem()
    if(numero_ilha==111):
        pyautogui.write('rosca 09')
        confirma_viajem()
    if(numero_ilha==112):
        pyautogui.write('rosca 12')
        confirma_viajem()
    if(numero_ilha==113):
        pyautogui.write('rosca 15')
        confirma_viajem()
    if(numero_ilha==114):
        pyautogui.write('rosca 18')
        confirma_viajem()
    if(numero_ilha==115):
        pyautogui.write('rosca 21')
        confirma_viajem()
    if(numero_ilha==116):
        pyautogui.write('bolo 03')
        confirma_viajem()
    if(numero_ilha==117):
        pyautogui.write('bolo 06')
        confirma_viajem()
    if(numero_ilha==118):
        pyautogui.write('bolo 09')
        confirma_viajem()
    if(numero_ilha==119):
        pyautogui.write('bolo 12')
        confirma_viajem()
    if(numero_ilha==120):
        pyautogui.write('bolo 15')
        confirma_viajem()


def confirma_viajem():
    time.sleep(0.3)
    click(281,318)
    time.sleep(0.3)
    click(305,863)

def deu_merda():
   time.sleep(0.2)


def faz_trabalhador():

    for x in range(10):
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha.png', confidence=0.6) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha Dia.png', confidence=0.6) != None:
            time.sleep(0.5)
            click(1020, 402)#1 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(1026, 551)#2 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(898, 427)#3 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(925, 645)#4 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(817, 499)#5 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(833, 692)#6 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(779, 509)#7 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(787, 722)#8 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(772, 511)#9 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(793, 717)#10 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(784, 521)#11 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(789, 719)#12 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(772, 513)#13 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(783, 708)#14 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(764, 524)#15 trabalhador
            time.sleep(0.2)
            coloca_diario()

            click(1858, 0)
            time.sleep(2)
            break

        else:
            time.sleep(0.4)

def troca_imb_p_flec():
    click(1543,22)
    time.sleep(0.2)
    click_arrasta(1666,548,1588,548)
    time.sleep(0.2)
    
def troca_flec_p_ferr():
    click(1543,22)
    time.sleep(0.2)
    click_arrasta(1749,548,1588,548)
    time.sleep(0.2)

#numero_ilha = int(input('Número da ilha: '))

#for x in range(1, 121):    
   # viaja_prox(numero_ilha)
    #numero_ilha+=1
   # time.sleep(3)
vai_trabalhador()
   # time.sleep(1)
   # faz_trabalhador()
   # time.sleep(1)
   # volta_trabalhador()
   # time.sleep(1)
   # if (numero_ilha == 41):
   #     troca_imb_p_flec()
  #  else:
  #      continue
  #  if (numero_ilha == 81):
  #      troca_flec_p_ferr()
  #  else:
   #     continue'''


