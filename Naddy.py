import pyautogui
import keyboard

version = 1.1
x, y = pyautogui.size()
all_modifiers = 'alt, alt gr, ctrl, left alt, left ctrl, left shift, left windows, right alt, right ctrl, right shift, right windows, shift, windows'
print('Naddy', version, '\nEnter your averange ping(F8 hotkey in-game):')
ping = int(input())
print('Set ping to', ping, 'ms.\nEnter hotkey(only lowercase characters, Ex. "space" or "ctrl"). Enter "allmods" to see all unique modifers:')
hotkey = input()
if hotkey == 'allmods':
    print('list of unique modifers:', all_modifiers, '\n\nEnter hotkey:')
    del hotkey
    hotkey = input()
print('Script triggers when WASD and/or', hotkey.upper(), 'is pressed.\n\n\nRelaunch the program if you want to set another values.')
cd = (ping)/1000
pyautogui.PAUSE = cd
r = 1/36*y
p = (r**2/2)**(1/2)

def naddy():
    pyautogui.moveTo(x/2, y/2)
def naddyw():
    pyautogui.moveTo(x/2, y/2-r)
    if keyboard.is_pressed('d+w+' + hotkey):
        naddydw()
    elif keyboard.is_pressed('w+a+' + hotkey):
        naddywa()
    elif keyboard.is_pressed('w+' + hotkey):
        naddyw()
    else:
        naddy()
def naddya():
    pyautogui.moveTo(x/2-r, y/2)
    if keyboard.is_pressed('w+a+' + hotkey):
        naddywa()
    elif keyboard.is_pressed('a+s+' + hotkey):
        naddyas()
    elif keyboard.is_pressed('a+' + hotkey):
        naddya()
    else:
        naddy()
def naddys():
    pyautogui.moveTo(x/2, y/2+r)
    if keyboard.is_pressed('a+s+' + hotkey):
        naddyas()
    elif keyboard.is_pressed('s+d+' + hotkey):
        naddysd()
    elif keyboard.is_pressed('s+' + hotkey):
        naddys()
    else:
        naddy()
def naddyd():
    pyautogui.moveTo(x/2+r, y/2)
    if keyboard.is_pressed('s+d+' + hotkey):
        naddysd()
    elif keyboard.is_pressed('d+w+' + hotkey):
        naddydw()
    elif keyboard.is_pressed('d+' + hotkey):
        naddyd()
    else:
        naddy()
def naddywa():
    pyautogui.moveTo(x/2-p, y/2-p)
    if keyboard.is_pressed('w+a+' + hotkey):
        naddywa()
    else:
        if keyboard.is_pressed('w+' + hotkey):
            naddyw()
        elif keyboard.is_pressed('a+' + hotkey):
            naddya()
        else:
            naddy()
def naddyas():
    pyautogui.moveTo(x/2-p, y/2+p)
    if keyboard.is_pressed('a+s+' + hotkey):
        naddyas()
    else:
        if keyboard.is_pressed('a+' + hotkey):
            naddya()
        elif keyboard.is_pressed('s+' + hotkey):
            naddys()
        else:
            naddy()
def naddysd():
    pyautogui.moveTo(x/2+p, y/2+p)
    if keyboard.is_pressed('s+d+' + hotkey):
        naddysd()
    else:
        if keyboard.is_pressed('s+' + hotkey):
            naddys()
        elif keyboard.is_pressed('d+' + hotkey):
            naddyd()
        else:
            naddy()
def naddydw():
    pyautogui.moveTo(x/2+p, y/2-p)
    if keyboard.is_pressed('d+w+' + hotkey):
        naddydw()
    else:
        if keyboard.is_pressed('d+' + hotkey):
            naddyd()
        elif keyboard.is_pressed('w+' + hotkey):
            naddyw()
        else:
            naddy()
keyboard.add_hotkey(hotkey, naddy)
keyboard.add_hotkey('w+' + hotkey, naddyw)
keyboard.add_hotkey('a+' + hotkey, naddya)
keyboard.add_hotkey('s+' + hotkey, naddys)
keyboard.add_hotkey('d+' + hotkey, naddyd)
keyboard.add_hotkey('w+a+' + hotkey, naddywa)
keyboard.add_hotkey('a+s+' + hotkey, naddyas)
keyboard.add_hotkey('s+d+' + hotkey, naddysd)
keyboard.add_hotkey('d+w+' + hotkey, naddydw)
keyboard.wait()
