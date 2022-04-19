import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', 'Vapiano', 'Bankside', 'SE1 0FD']

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # sysargv will be a list, you dont need first item of list at index 0
else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)



