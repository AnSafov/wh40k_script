from bestconfig import Config
import pyautogui
import keyboard

#Переменные и оптимизация
config = Config('setting.json')  #считывание конфига
pyautogui.PAUSE = config['pause']  #интервал между командами библиотеки (для оптимизации)
funkey = False  #ключ запуска кода

print('Version: ', config['version'])  #инфа для крутых
print('Writen by AnSafov07')  #имя автора

def func(x):
    if x == 1:
        pyautogui.hotkey('ctrl', 'shift', '`')
        pyautogui.write('taskbar_hide', 0.1)
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'shift', '`')
    if x == 0:
        pyautogui.hotkey('ctrl', 'shift', '`')
        pyautogui.write('taskbar_show', 0.1)
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'shift', '`')

while True:
    if keyboard.is_pressed(config['start_but']):
        func(1)
    if keyboard.is_pressed(config['end_but']):
        func(0)
    if keyboard.is_pressed(config['shotdown']):
        break
