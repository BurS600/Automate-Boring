#character counting program

import pprint
message = "It was a bright cold day in April, and the clocks were striking thirteen"

count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count) # pretty prints for dicts and lists

#messageFormatPrint = pprint.format(count)
#pprint.pformat prints the same as pprint.pprint but in STRING type which you can store in a variable to do any manipulation with later


