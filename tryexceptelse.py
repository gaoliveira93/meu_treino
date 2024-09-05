import pyautogui
import time
import pandas as pd

#pythonautogui.write()
#pythonautogui.click()
#pythonautogui.LocateOnScreen()
#pythonautogui.hotkey()
##pythonautogui.press()

data = pd.read_excel('Teste_Email.xlsx')

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

x, y = pyautogui.locateCenterOnScreen('Escrever.png', confidence=0.7)
pyautogui.click(x, y)
for i, Email in data.iterrows():
    time.sleep(0.5)
    pyautogui.write(data['Email'][i])
    time.sleep(0.5)
    pyautogui.press('Tab')
    pyautogui.press('Tab')
    time.sleep(0.5)
    pyautogui.write(str(data['Assunto'][i]))
    time.sleep(0.5)
    pyautogui.press('Tab')
    time.sleep(0.5)
    pyautogui.write(data['Mensagem'][i])
    time.sleep(0.5)
    pyautogui.press('Tab')
    time.sleep(0.5)
    pyautogui.press('Enter')
    x, y = pyautogui.locateCenterOnScreen('Escrever.png', confidence=0.7)
    pyautogui.click(x, y)   

print('Emails enviados')


with open('keys.log')