import webbrowser
import time
import pyautogui
from typing import List
from random import randint

def open_browser_and_enter(urls: List[str]):
    browser = webbrowser.get()
    for url in urls:
        browser.open(url)
        pyautogui.press('enter')
        time.sleep(randint(3, 10))
        pyautogui.moveTo(1359, 174)
        pyautogui.drag(0, 500, 1, button='left')
        pyautogui.click()
    
    time.sleep(3)
    # Press Enter key
    time.sleep(60 + randint(3, 60))

    x = 1310
    y = 90
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(1)
    pyautogui.click()

# x, y = pyautogui.position()
# print("Mouse position:", x, y)

url = ["https://vocal.media/poets/layla-s-eyes", "https://vocal.media/poets/children-of-the-sand"]
open_browser_and_enter(url)

