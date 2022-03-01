import pyautogui 
import time
        
pyautogui.PAUSE = 0.8

começo = time.time() 
# primeiro laço de repetição.
for i in range(1):
    # lembrando que a posição da minha tela pode ser diferente da sua.  
    # por isso deixei em uma outra pasta uma forma de você encontrar cada posição da tela de acordo com o seu monitor. 

    # abrir a aba do Instagram.        
    pyautogui.click(x=128, y=14)
    # clicar em 'seguidores'. 
    pyautogui.click(x=756, y=304)

    # segundo laço de repetição. 
    pyautogui.PAUSE = 0.8
    for i in range (4):
        pyautogui.hotkey('tab')
    pyautogui.press('enter')
    # seguindo as 7 primeiras pessoas. 
    pyautogui.click(x=828, y=330)
    pyautogui.click(x=838, y=374)
    pyautogui.click(x=835, y=415)
    pyautogui.click(x=837, y=474)
    pyautogui.click(x=833, y=519)
    pyautogui.click(x=835, y=574)
    pyautogui.click(x=841, y=622)

    # recarregar a página.
    pyautogui.hotkey('f5')
    time.sleep(5)

final = time.time()
# mostrar na tela quanto tempo o código demorou para ser executado. 
print(f"Este código demorou {int(final - começo)} segundos para ser executado.")

# abrir uma nova janela personalizada quando o código rodar por completo.  
from tkinter import *
master = Tk()
Label(master, text="Concluído com sucesso!").grid(row=1)
mainloop()
