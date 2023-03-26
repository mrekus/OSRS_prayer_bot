import win32api
import pyautogui
import time
from random import uniform, randint


def main():
    x = 1
    while x < 25:
        click_inventory()
        click_altar()
        time.sleep(round(uniform(0.08, 0.12), 2))
        x += 1


def click_inventory(x=randint(1130, 1142), y=randint(347, 362)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.08, 0.12), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))


def click_altar(x=randint(1128, 1146), y=randint(387, 402)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))


if __name__ == "__main__":
    time.sleep(5)
    main()
