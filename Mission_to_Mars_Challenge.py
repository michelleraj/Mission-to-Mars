from splinter import Browser
from bs4 import BeautifulSoup as bsoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import requests

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemis_url)

html = browser.html
soup = bsoup(html, 'html.parser')

base_url = "https://astrogeology.usgs.gov"
hemis_img_urls = []

results = soup.find_all("div", class_='item')
for result in results:
    
    title = result.find('h3').text
    img_page_url = base_url + result.find('a')['href']
    
    response = requests.get(img_page_url)
    img_soup = bsoup(response.text, 'html.parser')
    
    img_url = img_soup.find('ul').li.a['href']
    
    img_dict = {'title': title, 
                'img_url': img_url}
    
    hemis_img_urls.append(img_dict)

