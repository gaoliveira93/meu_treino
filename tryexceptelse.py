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
        location = pyautogui.locateOnScreen('Barra_Email.png')
        if location is not None:
            x, y = location
            pyautogui.click(x, y)
            break  # Exit loop once the image is found and clicked
        else:
            print('Image not found, trying again...')
            time.sleep(1)  # Wait before retrying to reduce resource usage
    except pyautogui.ImageNotFoundException:
        print('Image not found exception raised, trying again...')
        time.sleep(1)

x, y = pyautogui.locateCenterOnScreen('Menu.png', confidence=0.7)
pyautogui.click(x, y)
x, y = pyautogui.locateCenterOnScreen('Contatos.png', confidence=0.7)
pyautogui.click(x, y)