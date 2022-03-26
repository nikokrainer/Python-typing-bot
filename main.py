# import time to implement delay in for loop
import time

# Using Keyboard module in Python
import keyboard

# PyAutoGui for screenshots
import pyautogui

# extracting text from images
import pytesseract.pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files x86\Tesseract-OCR\tesseract.exe'
from pytesseract import pytesseract

word = 'Hello, nice to meet you'

pyText = ''


def save_screenshot():
    global pyText
    screenshot = pyautogui.screenshot(region=(850, 500, 850, 300))
    screenshot.save('image.png')
    img = Image.open('image.png')
    pyText = pytesseract.image_to_string(img)
    print(pyText)


line = "|"


def writing_function(word):
    time.sleep(1)
    for char in word:
        if char == '\n':
            keyboard.write(' ')
            time.sleep(0.010)
        if char != line:
            keyboard.write(char)
            time.sleep(0.010)
        elif char == line:
            keyboard.write('I')
            time.sleep(0.010)


keyboard.add_hotkey('8', lambda: keyboard.write(pyText))

keyboard.add_hotkey('ctrl + shift', lambda: writing_function(pyText))

keyboard.add_hotkey('0', lambda: save_screenshot())

keyboard.add_hotkey('7', lambda: change_stop())

keyboard.wait('esc')
