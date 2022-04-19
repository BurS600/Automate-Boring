import re

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line."

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

    # creating a regex object that stores what pattern you are looking for ; \d specifies a digit

mo = phoneNumRegex.search(message)

    # methods on a regex object return something called a matched object
    #the search method for a regex object looks for the 1st match only
    #the findall() method for a regex object looks for all occurences
    #print(phoneNumRegex.findall(message)) -- for some reason in Al's tutorial it seems you dont need to
    #first store it as a matched object to be able to print ALL occurences

#print(mo) -- just printing mo prints metadata along with matched string, hence group() used to just return matched string

print('output of mo group: ' + mo.group())

    #matched objects have a group() method which returns the actual matched string ----- mo stores ONE matched object,
    #hence when doing findall() you dont store it as ONE matched object, you just print return of PhoneNumRegex.findall(message)


print('output of findall() on regex object: ' + str(phoneNumRegex.findall(message)))

