import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import re
from tqdm import tqdm

# Reference: https://jasonfavrod.com/writing-web-scraped-html-to-a-file/

df = pd.read_csv('yelp_dataset.csv')
total_webpages = range(0, df['url'].shape[0])
n = 3
sessions = [total_webpages[i:i+n] for i in range(0, len(total_webpages)+1, n)]

# print(sessions)
for session, session_range in tqdm(enumerate(sessions)):
    # print(session)
    for index in tqdm(session_range):
        # print(f"\nSession {session}", "Index: ", index)
        response = requests.get(df['url'][index])
        delay = np.random.randint(25,50)
        time.sleep(delay)
        html = response.text

        with open(f"./webpages/business_page{index}.html", "w") as file:
            page = bytes(html, 'utf-8')
            file.write(str(page))
    
    time.sleep(np.random.randint(600,800))
    # print(f"\nSession {session} completed")