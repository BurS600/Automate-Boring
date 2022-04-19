# try and except -- program can recover i.e move on to next iteration post capturing error
# raise and assert -- program cannot recover i.e stops and produces error


"""

*********
*       *
*       *
*       *
*       *
*       *
*********

"""


#def boxPrint(symbol, width, height):
 #   print(symbol * width)

 #   for i in range(height-2):
  #      print(symbol + (" " * (width -2)) + symbol)

  #  print(symbol * width)

#boxPrint("*", 15, 5)
#boxPrint("~", 15, 5)

# but what if we accidentally pass it more than one character? then it would
# not produce what we want
# we can include a raise statement so program fails fast and early

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception( "Symbol needs to be character length of 1")
    if (width < 2) or (height < 2):
        raise Exception( "width or height must be greater or equal to 2")
    print(symbol * width)

    for i in range(height-2):
        print(symbol + (" " * (width -2)) + symbol)

    print(symbol * width)

boxPrint("*", 15, 5)
#boxPrint("~~", 15, 5)
boxPrint("v", 15, 5)
#boxPrint("*", 1, 1)



# you can get the traceback error message in the form of text/string for your logging
# need to import traceback to use traceback.format_exc() function
# in below by using try and except and error logging, you allow the function to keep on running while
# creating a log to store the error / traceback messages


import traceback

try:
    raise Exception( ' This is the error message')
except:
    errorFile = open('error_log1.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')








# Assert statements are used to perform sanity checks on your code
# by stating a condition that needs to be true for code to run properly, you use the assert statement enabling the code to fail fast and early
# note assert statement allows for an error message to be specified after a comma


# assert False, 'This is the error message.'

market_2nd = { 'north-south': 'green', 'east-west': 'red' }

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), "Neither light is red! " + str(intersection)

print(market_2nd)           
switchLights(market_2nd)
print(market_2nd)










