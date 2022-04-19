import pyautogui, os

os.chdir(r"C:\Users\burha\MyPythonScripts\ImageRecog")
# pillow imaging module lets program 'see' whats on screen and what it's clicking

pyautogui.screenshot()

# will return pillow object ; look at chapter 17

pyautogui.screenshot(r'C:\Users\burha\MyPythonScripts\ImageRecog\screenshot_example.png')


# pyautogui.locateOnScreen('passimageyouwanttolocate')
# will return of tuple list of 4 items, first 2 will be x,y and last 2 will be width,height

# pyautogui.locateCenteronScreen('')
# above slightly better will return tuple of center

# pyautogui.click()
# can pass both tuples of 2 coordinates or coordinates directly

# above functions are taxing, and usually need exact matches; read documentation to optimise / and look for partial matches

