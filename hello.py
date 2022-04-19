#' this program says hello and asks for my name

print('Hello World!')
print( 'What is your name?') # ask their name
myName= input()
print('It is good to meet you, ' +myName)
print(len(myName))
print ('What is your age?') # ask for their age
myAge = input()
print( 'You will be' + str(int(myAge) + 1) + 'in a year') # input returns string which gets converted to int then mathematcally added then turned to str again before concatenating

       
