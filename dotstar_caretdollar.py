import re

beginsWithHelloRegex = re.compile(r'^Hello!')
print(beginsWithHelloRegex.search('Hello! How are you?'))
print(beginsWithHelloRegex.search('He said Hello! How are you?')) # returns None


endsWithWorldRegex = re.compile(r'World!$')
print(endsWithWorldRegex.search('Hello World!'))
print(endsWithWorldRegex.search('Hello World! of Worlds')) # returns None


allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('00328947329472937429742'))
#if you miss out the + in the Regex it will only look for 1 char match
# the point of caret/dollar match is to say everything in my string matches said pattern i.e full string consists of digits only

print(allDigitsRegex.search('003289473294x72937429742'))
# will return None as begins with digits and ends with digits but pattern is broken in-between



# . -- wildcard means any char except newline (N.B: 1 char wildcard match only)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
# flat comes out as 'lat' because its 4 char long compared to all others which are 3 char long

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
# this still not what you are expecting as now it returns any 1 or 2
# chars before 'at' that are not newline

atRegex = re.compile(r'(\w+at)')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
# not in the tutorial but this how you can match all the words ending in 'at' - using \w (any letter, numeric digit or the underscore char) (i.e: matching "word" chars)




NameStr = 'First Name: Al Last Name: Sweigart'

NameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # remember when 2 or more groups in Regex you will return tuples / list of tuples
print(NameRegex.findall(NameStr))


serve = '<To serve humans> for dinner.>'

nonGreedydotStar = re.compile(r'<(.*?)>')
print(nonGreedydotStar.findall(serve))
# adding ? after .* does non-greedy match similar to adding ? after curly {}

GreedydotStar = re.compile(r'<(.*)>')
print(GreedydotStar.findall(serve))
      


#. matches any char except newline ; can use re.dotALL to also match newline


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
print(dotStar.findall(prime))

dotStar = re.compile(r'.*',re.DOTALL)
print(dotStar.search(prime))
#print(dotStar.findall(prime))
modotStar = dotStar.search(prime)
print(modotStar.group())

# you have to print matched object using mo.group() to view the entire matched object
# as there is cap to what is shown as return of simply .search()


vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE)# can just use re.I as shortform for re.IGNORECASE
print(vowelRegex.findall('Al SweigArt, why does your programming book talk about RoboCop so much?'))








