import bs4, requests

# res = requests.get('https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?crid=27ZU3YLRV2G6O&keywords=automate+the+boring+stuff&qid=1645350209&sprefix=automate+the+boring+stuff%2Caps%2C76&sr=8-1')
# Apparently Amazon introduced some deterrent to prevent web scraping


res = requests.get('https://uk.finance.yahoo.com/')
print(res.raise_for_status())

# warning will show up just to say it has assumed it needs to parse html ; you can add 'html.parser' option after res.text to get rid of this warning

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# the contents of the response object can be called using res.text


elems = soup.select('#marketsummary-itm-0 > h3 > fin-streamer')

# above will list of all the elements from selector specified, currently we have only 1 element
# the HTML of the SOUP object will be returned produced using soup.select() method
# text just holds string value
# we can look at the first index within the soup object using [0] (remember this is a list return)
# similar to res.text, the soup object also has a text method that can help return its contents
# N.B: the res.text method doesnt need an input and is not .text() with parenthesis

print(elems)

print(elems[0].text)

# print(elem[0].text.strip()
# could use the above if returned element string contained lots of whitespaces etc


# putting it all into a function
def getYahooFTSE100(YahooUrl):
    res = requests.get(YahooUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#marketsummary-itm-0 > h3 > fin-streamer')
    return elems[0].text
    

FTSE100Price = getYahooFTSE100('https://uk.finance.yahoo.com/')
print('The price of FTSE 100, when this program was run is: ' + FTSE100Price)
