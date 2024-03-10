
# import library
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import streamlit as st
from pandas.tseries.offsets import DateOffset


# define functions

# load data
@st.cache_resource # loads this function once and doesn't reload everytime we reload our page
def load_data():

    # load data
    df_vid = pd.read_csv('resource/Video_Performance_Over_Time.csv')

    # dropping row Total to avoid issue with calculations
    df_agg = pd.read_csv('resource/Aggregated_Metrics_By_Video.csv').iloc[1:,:]

    df_agg_sub = pd.read_csv('resource/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')

    df_com = pd.read_csv('resource/All_Comments_Final.csv')

    # converting all columns to uppercase
    for df in [df_agg,df_vid,df_agg_sub, df_com]:
        df.columns = df.columns.str.upper()

    # remove \xad
    df_agg.columns = df_agg.columns.str.replace('\xad','')
    # convert date to datetype

    df_agg['VIDEO PUBLISH TIME'] = pd.to_datetime(df_agg['VIDEO PUBLISH TIME'], format='mixed')
        
    df_agg['AVERAGE VIEW DURATION'] = df_agg['AVERAGE VIEW DURATION'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))

    # create new column for df_agg['AVERAGE VIEW SECONDS'
    df_agg['AVERAGE VIEW SECONDS'] = df_agg['AVERAGE VIEW DURATION'].apply(lambda x: x.second + x.minute * 60 + x.hour * 60 * 60)

    # engagement ration, every engagement a view could do divided by the number of viewrs
    df_agg['ENGAGEMENT RATIO'] = (df_agg['SHARES'] + df_agg['LIKES'] + df_agg['DISLIKES'] + df_agg['COMMENTS ADDED']) / df_agg['VIEWS'] 

    # ratio of views to subscribers gained
    df_agg['VIEW TO SUBSCRIBER RATIO'] = df_agg['VIEWS'] / df_agg['SUBSCRIBERS GAINED'] # how views does it take to gain a subscriber

    # ratio of views to subscribers lost, 
    df_agg['VIEW TO SUBSCRIBER LOST RATIO'] = df_agg['VIEWS'] / df_agg['SUBSCRIBERS LOST'] # how views does it take to lose a subscriber

    # sort data by 'VIDEO PUBLISH TIME'
    df_agg.sort_values(by = 'VIDEO PUBLISH TIME', ascending=False, inplace=True)

    # CONVERTING DATE to datetime
    df_vid['DATE'] = pd.to_datetime(df_vid['DATE'], format='mixed')

    df_com['DATE'] = pd.to_datetime(df_com['DATE'])

    # create dataframe
    return df_vid, df_agg, df_agg_sub, df_com

df_vid, df_agg, df_agg_sub, df_com = load_data()


# engineer data

# aggregated differential 

# create a copy of our dataframe
df_agg_diff = df_agg.copy()

# for the last 12 months, most recently date back to 12 months
metric_date_12mo = df_agg_diff['VIDEO PUBLISH TIME'].max() - DateOffset(months=12)

# dataframe from metric_date_12mo to df_agg_diff['VIDEO PUBLISH TIME'].max()
# that is, from 12 months early to current date

df_agg_diff_12mo = df_agg_diff[df_agg_diff['VIDEO PUBLISH TIME'] >= metric_date_12mo]

# median 
median_agg = df_agg_diff_12mo[df_agg_diff_12mo.columns[2:]].median()

## what metrics wil be relevant
## difference from baseline
## percent change

# build dashboard

# sidebar
add_sidebar = st.sidebar.selectbox("Aggregate or Individual Video", ("Aggregate Metrics", "Individual Video Analysis"))

## local picture
if add_sidebar == "Aggregate Metrics":

    metric_agg = df_agg[[
        'VIDEO PUBLISH TIME',
        'COMMENTS ADDED', 
        'SHARES', 
        'DISLIKES', 
        'LIKES', 
        'SUBSCRIBERS GAINED', 
        'RPM (USD)', 
        'VIEWS', 
        'YOUR ESTIMATED REVENUE (USD)',
        'AVERAGE VIEW SECONDS', 
        'ENGAGEMENT RATIO', 
        'VIEW TO SUBSCRIBER RATIO',
    ]]  

    def metric_median(n):
        # 
        metric_date_n = metric_agg['VIDEO PUBLISH TIME'].max() - DateOffset(months=n)
        median_date_n = metric_agg[metric_agg['VIDEO PUBLISH TIME'] >= metric_date_n].median()
        
        return metric_date_n,median_date_n

    metric_12mo, median_12mo = metric_median(12)
    metric_6mo, median_6mo = metric_median(6)

    col1, col2, col3,col4,col5,col6 = st.columns(6)
    columns = [col1, col2, col3,col4,col5,col6]

    count = 0
    for i in median_6mo.index:
        with columns[count]:
            delta = (median_6mo[i] - median_12mo[i])/median_12mo[i]
            st.metric(lable = i, value =round(median_12mo[i], 2), delta="{:.2%}".format(delata))
            count += 1
            if count >= 6:
                count = 0


elif add_sidebar =="Individual Video Analysis":
    st.write('Ind')
## individual video

# improvement