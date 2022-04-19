from selenium import webdriver

path = (r"C:\Users\burha\AppData\Local\Programs\Python\Python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(path)
browser.get('https://investopedia.com/')

iAcceptSelector = browser.find_element_by_css_selector('#onetrust-accept-btn-handler')
iAcceptSelector.click()
# clicking "I Accept" for cookies ; it seems (assumption) you have to automate by following every step you would click/interact with otherwise


#hamburgerSelector = browser.find_element_by_css_selector('#header-nav_1-0 > div > svg.icon.icon-hamburger')
#hamburgerSelector.click()

# clicking categories menu ('hamburger')


# finding all the paragraph elements from the HTML page

paraElements = browser.find_elements_by_css_selector('p')
print(len(paraElements))



searchElem = browser.find_element_by_css_selector('#header__search_1-0')
searchElem.click()

# click on search icon


searchInputElem = browser.find_element_by_css_selector('#header__search_1-0 > div > input')
searchInputElem.send_keys('Credit Risk')
searchInputElem.submit()

# send_keys and submit() to find search box, input text, and submit form

browser.back()
browser.forward()
browser.refresh()
# browser.quit()

# controlling the browser to go back / forward etc








# opening another browser to read content of the page

browser = webdriver.Chrome(path)
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('body > div > main > div > p:nth-child(6)')
print(elem.text)

allElems = browser.find_element_by_css_selector('html')
print(allElems.text)




