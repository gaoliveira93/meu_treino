import pyautogui
import time

#pythonautogui.write()
#pythonautogui.click()
#pythonautogui.LocateOnScreen()
#pythonautogui.hotkey()
##pythonautogui.press()

pyautogui.PAUSE = 1

pyautogui.hotkey('win')
pyautogui.write('brave')
x, y = pyautogui.locateCenterOnScreen('Brave.png', confidence=0.7)
pyautogui.click(x, y)
pyautogui.write('gmail.com')
pyautogui.press('Enter')

while True:
    try:
        barra_email =pyautogui.locateCenterOnScreen('Barra_Email.png', confidence=0.7)
        if barra_email:
            break
    except:
        time.sleep(0.5)

x, y = pyautogui.locateCenterOnScreen('Menu.png', confidence=0.7)
pyautogui.click(x, y)
x, y = pyautogui.locateCenterOnScreen('Contatos.png', confidence=0.7)
pyautogui.click(x, y)