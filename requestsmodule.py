import requests

#requests lets you download content off websites ; useful for where there is a direct/easy url to file available

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# a response object is returned

res.status_code

# res.status_code method  to check if download went okay ; if 404, then file not found ; 200 means all okay

len(res.text)

print(res.text[:500])


res.raise_for_status()

# method to raise exception if any issue with download ; fail early otherwise nothing happens


#badResexample = requests.get('https://automatetheboringstuff.com/files/jkfsasoifsafsao')
#badResexample.raise_for_status()

# exception raised for this resposne object which is looking for a file that doesnt exist

playFile = open('RomeoAndJuliet.txt' , 'wb')

# you have to enable write in binary mode because you need to maintain unicode encoding of the text
# basic understanding is computer fundamentally only works with bytes
# but we need more chars/combinations than what bytes can provide due to vast amount of languages and symbols that
# we need to be able to capture; unicode is what has been created as a universal store all chars needed in the world
# it has a capacity of ~ 1.1m and so far only 10% of that has been utilised in getting all the major languages on board
# at the time of this course, unicode 6.1 was published/upgraded

for chunk in res.iter_content(100000):
    #100000 specifies the number of bytes being written per chunk of iteration
    playFile.write(chunk)

playFile.close()
