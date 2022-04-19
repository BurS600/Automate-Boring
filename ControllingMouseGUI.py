import pyautogui

# resolution of screen

width, height = pyautogui.size()

pyautogui.position()

# current mouse position ; most of these calls return tuples in this script

pyautogui.moveTo(10,10, duration=1.5)

# moves mouse to position within specified duration; can also use dragTo() which will click and drag to position

pyautogui.moveRel(20,0)

# move relative to current position ; can also use dragRel() which clicks and drags to relative position

# remember 0,0 is top left corner; bottom bost and right most corner is resolution numbers minus 1 as it starts from 0

pyautogui.click(339,38)

# click mouse in this position ; can also use rightClick, doubleClick, middleClick



## this module has a fail safe for when you want to interrupt your automation; simply force your mouse to the top left near 0,0 position while automation is running
# equivalent of keyboard interrupt effectively



# you can use CMD prompt and run pyautogui.displayMousePosition() and note down all the coordinates of interest in one go
# by moving your mouse around; you will also be able to see the RGB of the pixel

