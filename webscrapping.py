import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import re


# class1 = "display--inline__09f24__EhyFv border-color--default__09f24__1eOdn"

# class2 = "display--inline__09f24__EhyFv border-color--default__09f24__1eOdn"

# assert class1 == class2

# Business urls
# https://www.yelp.co.uk/search?cflt=homeservices&find_loc=Berlin%2C%20Germany
# https://www.yelp.co.uk/search?cflt=restaurants&find_loc=Berlin%2C%20Germany

businesses = ["restaurants", "homeservices"]

main_url = f"https://www.yelp.co.uk/search?cflt={businesses[0]}&find_loc=Berlin%2C%20Germany"

# other pages url (for restaurants case)
# https://www.yelp.co.uk/search?cflt=restaurants&find_loc=Berlin%2C%20Germany&start=10
# pages --> main_url + (start = range(10,231,10)), can automate finding ending
# index

responses = [requests.get(main_url)]
for index in range(10,231,10):
    responses.append(requests.get(f"{main_url}&start={index}"))
    delay = np.random.randint(1,6)
    time.sleep(delay)

webpages = []
for response in responses:
    webpages.append(BeautifulSoup(response.content, 'html.parser'))

print(len(soups), "Should be 24 for restaurants")

# Class to get hrefs
span_class = "css-1pxmz4g"

# Needed regex here as strip was leaving some characters Strangely those
# characters only appeared on appending but not in a direct print

regex = re.compile('[^a-zA-Z]')
child_urls = []
names = []
for webpage in webpages:
    items = webpage.findAll('span', class_ = span_class)
    
    for item in items:
        names.append(regex.sub('', item.text))
        child_urls.append(f"https://www.yelp.co.uk{item.find('a')['href']}")

df = pd.DataFrame({f"{businesses[0]}_name".title(): names, "url": child_urls})

print(df.shape, "Should be (240,2)")