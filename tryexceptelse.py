import pyautogui

#pythonautogui.write()
#pythonautogui.click()
#pythonautogui.LocateOnScreen()
#pythonautogui.hotkey()
##pythonautogui.press()

pyautogui.PAUSE = 1

pyautogui.hotkey('win')
pyautogui.write('brave')
x, y, largura, altura = pyautogui.locateCenterOnScreen('Brave.png')
pyautogui.click(x + largura/2, y + altura/2)