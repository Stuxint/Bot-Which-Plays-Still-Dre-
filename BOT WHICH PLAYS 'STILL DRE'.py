#--------------------BOT WHICH PLAYS 'STILL DRE'------------------------------------------
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

#------------STEP 1: GOES TO PIANO WEBSITE----------------------------
web = uc.Chrome()
web.get("https://recursivearts.com/virtual-piano/")


play= WebDriverWait(web, 10).until(
                        EC.presence_of_element_located(('xpath', '//*[@id="pianoButtonImage"]'))
                    )
play.click()

time.sleep(10)
pyautogui.moveTo(500, 550)
pyautogui.click()

#------------STEP 2: PLAYS INTO----------------------------
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
pyautogui.press('f')
time.sleep(0.2)
pyautogui.press('j')

time.sleep(1.5)
for x in range(4):
    pyautogui.press('s')
    time.sleep(0.06)
    pyautogui.press('f')
    time.sleep(0.06)
    pyautogui.press('j')
    time.sleep(0.2) 

#------------STEP 3: PLAYS SECOND PART----------------------------
for x in range(11):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
for x in range(5):
    pyautogui.hotkey('a', 'd', 'h')
    time.sleep(0.2)

time.sleep(0.01)

for x in range(11):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
for x in range(5):
    pyautogui.hotkey('a', 'd', 'h')
    time.sleep(0.2)

#------------STEP 4: PLAYS THIRD PART----------------------------
pyautogui.hotkey('e', '6')
time.sleep(0.00001)
for x in range(6):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
pyautogui.hotkey('r', '7')
for x in range(2):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.000001)
pyautogui.hotkey('0', '3') 
for x in range(3):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
for x in range(5):
    pyautogui.hotkey('a', 'd', 'h')
    time.sleep(0.2)

pyautogui.hotkey('e', '6')
time.sleep(0.00001)
for x in range(6):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
pyautogui.hotkey('r', '7')
for x in range(2):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.000001)
pyautogui.hotkey('0', '3')
for x in range(3):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
for x in range(5):
    pyautogui.hotkey('a', 'd', 'h')
    time.sleep(0.2)

#------------STEP 5: PLAYS THE END----------------------------
pyautogui.hotkey('8', 't')
time.sleep(0.00001)
for x in range(6):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
pyautogui.hotkey('y', '9')
for x in range(2):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.000001)
pyautogui.hotkey('7', 'r')
for x in range(3):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
for x in range(5):
    pyautogui.hotkey('a', 'd', 'h')
    time.sleep(0.2)

pyautogui.hotkey('4', 'q')
time.sleep(0.00001)
for x in range(6):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
pyautogui.hotkey('5', 'w')
for x in range(2):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.000001)
pyautogui.hotkey('3', '0')
for x in range(3):
    pyautogui.hotkey('s', 'f', 'j')
    time.sleep(0.2)
time.sleep(0.00001)
for x in range(5):
    pyautogui.hotkey('a', 'd', 'h')
    time.sleep(0.2)

time.sleep(100)