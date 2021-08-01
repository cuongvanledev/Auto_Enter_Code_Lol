import pyautogui
import time
import keyboard


lmht = open("BongBayLMHT.txt", "r", encoding='utf-8').readlines()

width = 1920
Height = 1200

# get size of desktop
screenWidth, screenHeight = pyautogui.size()
print(screenWidth)
print(screenHeight)

for i in lmht:
    if keyboard.is_pressed('s') == True:
        break
    if i == "\n":
        continue
    val = i.replace("\n", "")
    print(val)

    #click mouse to enter code
    pyautogui.click(1066/width * screenWidth, 878/Height * screenHeight)
    #time.sleep(100)

    # Ctrl -a 
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')

    # Write Code 
    pyautogui.typewrite(val)

    # Click Nhap
    pyautogui.click(1300/width * screenWidth, 880/Height * screenHeight)
    time.sleep(0.5)

    # Click select OK
    pyautogui.click(1023/width * screenWidth, 757/Height * screenHeight)
    time.sleep(0.5)

    # Click select OK
    pyautogui.click(861/width * screenWidth, 758/Height * screenHeight)
    time.sleep(0.5)
