from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller



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

    while(True):
        time.sleep(1)
        click(1622, 0, True)

        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha.png', confidence = 0.5) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha Dia.png', confidence = 0.5) != None :
            time.sleep(0.3)
            click(1020, 402, False)
            break
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            deu_merda()
            return True

def volta_trabalhador():#walk from the end of the island till the Travel Planer

    while(True): 
        time.sleep(1)
        click(32, 1079, True)

        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.5) != None :
            time.sleep(1)
            click(1082, 264, False)
            break
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            deu_merda()

def faz_trabalhador():#click in each labour and put the journals into it
    
    for x in range(8):
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            deu_merda()
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha.png', confidence=0.6) or pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Tocha Dia.png', confidence=0.6) != None:
            time.sleep(0.5)
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
    for x in range(4):
        time.sleep(0.2)
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
                        time.sleep(0.3)

    for x in range(4):
        time.sleep(0.2)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Deixar Diario.png', confidence=0.8) != None:
            time.sleep(0.2)
            click_arrasta(1585, 548, 207, 659)#put the journal in the labour
            time.sleep(0.2)
            break
        else:
            time.sleep(0.5)

    for x in range(4):
        time.sleep(0.2)
        if  pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Aceitar.png', confidence=0.8) != None:
            click(121, 866, False)#after the journal is put in the labour this funcion click to confirm the journal and start the work
            time.sleep(0.3)
            return False
        else:
            time.sleep(0.5)

def viaja_prox(numero_ilha):#type the name of the island u want to travel
                            ##If u want to use u need to change the name of the islands to match with your own islands
    for x in range(10):     ###Notice the number of 'numero_ilha' plus one in each island
        time.sleep(0.5)
        if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Comprar Viagem.png', confidence=0.8) != None:
            click(275,291, False)
            pyautogui.write('')
            time.sleep(0.2)
            break
    if(numero_ilha == 0):
        pyautogui.write('Fort Stearling Craft')#Your backup point
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

def confirma_viagem():#after the viaja_prox island tipe the name of your island this funcion click to travel
    
    time.sleep(0.3)
    click(281,318, False)
    time.sleep(0.3)
    click(305,863, False)
 
def logout():#try to log back in game

    while(True):
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png' , confidence = 0.8) != None:
            click(956, 644, True )#if u are in the login screen
            time.sleep(2)
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\No_wifi.png' , confidence = 0.8) != None:
            click(960, 547, True)#if u are stil ofline, the bot will keep tring to conect
            time.sleep(2)

        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\C_S.png', confidence = 0.8) != None:
            click(948, 864, True)#if the bot have sucess and pass the login screen, he will log in your charater
            time.sleep(2)
            break

def deu_merda():#if anything go out of the normal this funcion is the responsible to help
    
    while(True):
        if locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\logout.png', confidence = 0.8) != None:
            logout()
        else:        
            click(32, 1079, True)
            if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Viajador.png', confidence = 0.5)  != None :
                time.sleep(1)
                click(1049, 253, False)
                time.sleep(1)
                viaja_prox(0)#pass the backup island
                if pyautogui.locateOnScreen('C:\\Users\\denis\\Desktop\\Bot albion\\Imagens\\Roda_dos_ventos.png', confidence = 0.7)  != None :
                    time.sleep(0.2)
                    click(1014, 246, False)
                    return
                    

def troca_imb_p_flec():#personal personalization, just change the item in the second slot of inventory to the first
    
    click(1543, 22, False)
    time.sleep(0.2)
    click_arrasta(1666,548,1588,548)
    time.sleep(0.2)
    
def troca_flec_p_ferr():#personal personalization, just change the item in the third slot of inventory to the first
    
    click(1543, 22, False)
    time.sleep(0.2)
    click_arrasta(1749, 548, 1588, 548)
    time.sleep(0.2)

numero_ilha = int(input('Número da ilha: '))
error = False
for x in range(1, 121):    
    viaja_prox(numero_ilha)
    time.sleep(3)
    error = vai_trabalhador()
    error = faz_trabalhador()

    while(error == True):
        viaja_prox(numero_ilha)
        time.sleep(3)
        vai_trabalhador()
        error = faz_trabalhador()

    time.sleep(1)
    volta_trabalhador()
    time.sleep(1)

    if(error == False):
        numero_ilha+=1

    if (numero_ilha == 41):
        troca_imb_p_flec()

    if (numero_ilha == 81):
        troca_flec_p_ferr()