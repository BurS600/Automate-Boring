import re

message = 'My number is 415-555-4242 or (415) 555 4200'
message2 = 'Batmobile is used by Batman to save Gotham'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #parenthesis in regex serve special purpose to specify groups
mo = phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2))


phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d \d\d\d\d') #if you want to look for actual parentheses, use escape character
mo = phoneNumRegex.search(message)
print(mo.group())


BatRegex = re.compile(r'Bat(mobile|man|monkey|woman)')
mo = BatRegex.search(message2)
print(mo.group())
print(mo.group(1)) # which group delimited by | was actually found


BatRegex = re.compile(r'Bat(mobile|man|monkey|woman)')
print(BatRegex.findall(message2))
print('Bat'+BatRegex.findall(message2)[0]+'\nBat'+BatRegex.findall(message2)[1])










