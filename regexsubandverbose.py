import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))

#sub will do find and replace
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob'))

#what if you want to use part of the original regex pattern and return Agent A and Agent B

namesRegex = re.compile (r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
# this will return ['A', 'B']

print(namesRegex.sub(r'Agent \1****' , 'Agent Alice gave the secret documents to Agent Bob'))
#this will return Agent A**** gave secredt documents to Agent B****

#basically similar to group(1) , group(2) etc you can use \1 \2 to specify regex group 1 or 2
#and can use this in sub method to specify which regex group to substitute


re.compile (r'''
\d\d\d    # area code
-         # first dash
\d\d\d    # first 3 digits 
-         # second dash
\d\d\d\d  # last 4 digits''',re.VERBOSE)

#re.VERBOSE bascially lets you use multi-line raw string in which spaces are not treated
#as part of regex pattern ; you can also put in comments within the raw string as well
#useful to help understand more clearly complex regex patterns


re.compile (r'''
\d\d\d    # area code
-         # first dash
\d\d\d    # first 3 digits 
-         # second dash
\d\d\d\d  # last 4 digits''' , re.IGNORECASE | re.DOTALL | re.VERBOSE)


# you can use a bit-wise OR operator which is esoteric syntax
# and only really for the options for re.compile function ;
# add a pipe | to be able to use more than one option in the second argument to the re.compile function


