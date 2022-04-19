#! python 3

import re, pyperclip, pprint

text = pyperclip.paste()

# Create Regex for phonenumbers
phoneRegex = re.compile (r'''

# options to cover: 555-555-0000, (555) 555-0000, 555-0000, ext.1234, ext1234, x.1234
(
((\d\d\d) | (\(\d\d\d\)))?        #area code (optional)
  (\s|-)      #separator
  (\d\d\d)      #middle number
   (-)         #separator
      (\d\d\d\d) #ending digits
   ((ext(\.)?(\d{2,5})) | (x(\.)?(\d{2,5})))?

) #extension code (optional)


''', re.VERBOSE)

# Create Regex for emails

emailRegex = re.compile (r'''

# options to cover somthing +. @ something +.

[a-zA-Z0-9+.]+ ##REMEMBER, you dont need escape slash in character classes!!
@
[a-zA-Z0-9+.]+


''', re.VERBOSE)


phonenumberExtract = phoneRegex.findall(text)

emailExtract = emailRegex.findall(text)

# iterating through list of tuples to pick up first group and append into list
phonenumberlist = []

for phoneNumber in phonenumberExtract:
    phonenumberlist.append(phoneNumber[0])



# Extract phonenumbers and emails neatly

results = '\n'.join(phonenumberlist) + '\n' + '\n'.join(emailExtract)
          
pyperclip.copy(results)
