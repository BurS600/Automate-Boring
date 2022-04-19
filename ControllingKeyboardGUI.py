import pyautogui

pyautogui.typewrite('Hello World')
# sends virtual keystrokes to computer (in the application that is in focus)

# pyautogui.click(40,-1522); pyautogui.typewrite('Hi, Hello World !', interval=0.05)
# interval in this case is the pause between each char being typed out; you can use semicolon to join 2 instructions for shell line


# pyautogui.click(40,-1522); pyautogui.typewrite(['Hi, Hello World !', 'left', 'left', 'Hello'], interval=0.05)
# you can also pass a list of keystrokes to be able to type keys like left arrow etc

pyautogui.KEYBOARD_KEYS

# will give you list of all the keys you can pass such as f11, volumemute, num3, shift, shiftleft, shiftright

pyautogui.press('F1')

# you can use to press a single key

pyautogui.hotkey('ctrl','o')

# can use hotkey to press shortcuts


