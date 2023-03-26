import win32api
import pyautogui
import keyboard
import time
from random import uniform, randint


def main():
    while True:
        if keyboard.read_key() == "1":
            for _ in range(0, 26):
                click_inventory()
                click_altar()
                time.sleep(round(uniform(0.2, 0.3), 2))
                main()


def click_inventory(x=randint(1569, 1596), y=randint(454, 477)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.08, 0.12), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))


def click_altar(x=randint(1006, 1152), y=randint(256, 341)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))


if __name__ == "__main__":
    time.sleep(5)
    main()
