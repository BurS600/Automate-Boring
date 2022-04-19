import re

batRegex = re.compile(r'Bat(wo)?man') # ? looks to match group 0 or 1 time
mo = batRegex.search('The Adventure of Batman')
print(mo.group()) # will match
mo = batRegex.search('The Adventure of Batwoman')
print(mo.group()) # will match
mo = batRegex.search('The Adventure of Batwowowoman')
# won't match
print(mo == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search('My Phone number is 415-555-4242')) # will match with area code in it
print(phoneRegex.search('My phone number is 555-4242')) # but will also match without area code in it as (\d\d\d-)? means match if area code appears 0 or 1 time


## Side note: If you want to actually match ? * or +, use escape character beforehand \? \* \+


batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # will match as * looks to match 0 or many times
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # will match as * looks to match 0 or many times
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group()) # will ALSO match compared to when ? was used as * looks to match the specified group 0 or many times


batRegex = re.compile(r'Bat(wo)+man')
batRegex.search('The Adventures of Batman')
print(batRegex.search('The Adventures of Batman') == None) ## won't match as 'wo' has to appear at least 1 time. + matches 1 or more times
# have to do a boolean test as mo.group() the group() method on a matched object cannot work with None type variable and will throw an error



haRegex = re.compile (r'(Ha){3}') # using {} curly bracks after a group you can specify how many repetitions of that group you want to match
print(haRegex.search('He said HaHaHa'))


phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d\-\d\d\d\d(,)?){3}')
# will look for 3 phone number matches (w/ or w/out area code) with an optional , delimiter in between
print(phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000'))

######
## when using {} curly brackets to specify number of repetitions you can use it like range {3,} {,3} {1,6}
## using a ? after curly brackets serves a special purpose to switch from greedy matching to non greedy matching
## greedy matching is where it looks for the maximum number of repetitions (which is the default)
## non greedy matching is where it looks for the least number of repetitions (using ? after curly brackets e.g: {3,5}?)



##'Ha'{3} means three repetitions (from current understanding) rather than three instances/occurences across entire string (which is what findall() does)
## i.e: HaHaHa matched rather than 'Ha','Ha,'Ha' from a string such as '''HaHaHa, is a 6 letter word that can be broken down into Ha and Ha and Ha'''








                
