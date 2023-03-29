import pyautogui
import keyboard
import time
from random import uniform


def main():
    while True:
        if keyboard.read_key() == "1":
            pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
            for _ in range(0, 25):
                click_altar()
                click_inventory()
            click_altar()
            main()


def click_inventory():
    pyautogui.move(-60, 0)
    time.sleep(round(uniform(0.06, 0.08), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))


def click_altar():
    pyautogui.move(60, 0)
    time.sleep(round(uniform(0.06, 0.08), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))


if __name__ == "__main__":
    main()
