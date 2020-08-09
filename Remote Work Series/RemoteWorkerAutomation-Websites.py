import requests
from bs4 import BeautifulSoup

from selenium import webdriver

url = 'https://www.derricksherrill.com'
response = requests.get(url)
print(response.status_code)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find_all('a')[1:5:1])

driver = webdriver.Chrome('./chromedriver')
url_to_search = 'https://www.gamestop.com/video-games/switch/consoles/products/nintendo-switch-with-gray-joy-con/11095821.html'

driver.get(url_to_search)

content = driver.find_element_by_xpath('//*[@id="primary-details"]/div[4]/div[12]/div[3]/div/div[1]/button')
print(content.text)
