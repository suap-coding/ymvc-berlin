import streamlit as st
import numpy as np
import pandas as pd
from tqdm import tqdm
from tqdm import trange
from time import sleep

st.title('Target Businesses: Report')

df_progress = pd.read_csv('yelp_dataset.csv')
scraping_left = sum([True for idx,row in df_progress.iterrows() if any(row.isnull())])


while scraping_left > 0:

    df_progress = pd.read_csv('yelp_dataset.csv')
    scraping_left = sum([True for idx,row in df_progress[['address','review_count']].iterrows() if any(row.isnull())])

    st.write("Scraping progress: ", scraping_left, "left off", df_progress.shape[0], "businesses")

    refresh = 30
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(refresh):
# Update the progress bar with each iteration.
        latest_iteration.text(f'Refreshing in {refresh - i + 1} seconds...')
        bar.progress(i + 1)
        sleep(1)


rest_win_subcategory = 'Street Food'
other_win_subcategory = 'Zoo'
count_businesses = 200


st.title('Best Your Momma VC Investment in Berlin by DataManiacs')
st.subheader('We will present the best option for each main subcategory')
st.write("""

How many businesses did we take into consideration? *{count_businesses}*

""".format(count_businesses=count_businesses))
if st.button("For Restaurants"):
    st.subheader('Winning sub-category: ')
    st.write('{rest_win_subcategory}'.format(rest_win_subcategory=rest_win_subcategory))
    st.subheader('Key Factors for success: ')

    st.write('Days Open: {rest_days}'.format(rest_days=rest_days))
    st.write('Days Open: {rest_att}'.format(rest_att=rest_att))


if st.button("For Other Business Types"):
    st.subheader('Winning sub-category: ')
    st.write('{other_win_subcategory}'.format(other_win_subcategory=other_win_subcategory))
    st.subheader('Key Factors for success: ')

    st.write('Days Open: {other_days}'.format(other_days=other_days))
    st.write('Days Open: {other_att}'.format(other_att=rest_att))

if st.button("Assumptions"):
    st.write("""Using the Pareto Law we looked for:
    
    + The worst rated categories - High Opportunity of Improvement (unhappy clients)

    + The categories with the most reviews - High Demand

    + The categories with the least businesses - Low Supply
    
    """)
