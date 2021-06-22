import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import re


business_pages = []
index = 0
response = requests.get(df['url'][index])
delay = np.random.randint(20,40)
time.sleep(delay)
soup = BeautifulSoup(response.content, 'html.parser')
business_pages.append(soup)

with open(f"business_page{index}.html", "w") as file:
    file.write(str(soup))