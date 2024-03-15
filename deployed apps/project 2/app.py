
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
@st.cache_data # loads this function once and doesn't reload everytime we reload our page
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

    # drop Nan value
    df_agg.dropna(inplace=True)

    # convert date to datetype

    df_agg['VIDEO PUBLISH TIME'] = pd.to_datetime(df_agg['VIDEO PUBLISH TIME'], format='mixed')

    # rename column

    df_agg.rename(columns={'VIDEO PUBLISH TIME': 'PUBLISH DATE', 'COMMENTS ADDED' : 'COMMENTS'}, inplace=True)
        
    df_agg['AVERAGE VIEW DURATION'] = df_agg['AVERAGE VIEW DURATION'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))

    # create new column for df_agg['AVERAGE VIEW SECONDS'
    df_agg['AVERAGE VIEW SECONDS'] = df_agg['AVERAGE VIEW DURATION'].apply(lambda x: x.second + x.minute * 60 + x.hour * 60 * 60)

    # engagement ration, every engagement a view could do divided by the number of viewrs
    df_agg['ENGAGEMENT RATIO'] = (df_agg['SHARES'] + df_agg['LIKES'] + df_agg['DISLIKES'] + df_agg['COMMENTS']) / df_agg['VIEWS'] 

    # ratio of views to subscribers gained
    df_agg['VIEW TO SUBSCRIBER RATIO'] = df_agg['VIEWS'] / df_agg['SUBSCRIBERS GAINED'] # how views does it take to gain a subscriber

    # ratio of views to subscribers lost, 
    df_agg['VIEW TO SUBSCRIBER LOST RATIO'] = df_agg['VIEWS'] / df_agg['SUBSCRIBERS LOST'] # how views does it take to lose a subscriber

    # sort data by 'VIDEO PUBLISH TIME'
    df_agg.sort_values(by = 'PUBLISH DATE', ascending=False, inplace=True)

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
metric_date_12mo = df_agg_diff['PUBLISH DATE'].max() - DateOffset(months=12)

# dataframe from metric_date_12mo to df_agg_diff['VIDEO PUBLISH TIME'].max()
# that is, from 12 months early to current date

df_agg_diff_12mo = df_agg_diff[df_agg_diff['PUBLISH DATE'] >= metric_date_12mo]

# median 
median_agg = df_agg_diff_12mo[df_agg_diff_12mo.columns[2:]].median()

## what metrics wil be relevant
## difference from baseline
## percent change

# build dashboard

# sidebar
add_sidebar = st.sidebar.selectbox("Aggregate or Individual Video", ("Aggregate Metrics", "Individual Video Analysis"))

# styling dataframe
def styling_positive(value, props):
    try:
        return props if value >= 0 else None
    except:
        pass


def styling_negative(value, props):
    try:
        return props if value < 0 else None
    except:
        pass

## local picture
if add_sidebar == "Aggregate Metrics":

    metric_agg = df_agg[[
        'PUBLISH DATE',
        'COMMENTS', 
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
        # date range
        metric_date_n = metric_agg['PUBLISH DATE'].max() - DateOffset(months=n)
        median_date_n = metric_agg[metric_agg['PUBLISH DATE'] >= metric_date_n].median()
        
        return metric_date_n,median_date_n

    metric_12mo, median_12mo = metric_median(12)
    metric_6mo, median_6mo = metric_median(6)

    col1, col2, col3,col4,col5,col6 = st.columns(6)
    columns = [col1, col2, col3,col4,col5,col6]

    count = 0
    for i in median_6mo.index:
        with columns[count]:
            if i != 'PUBLISH DATE':
                delta = (median_6mo[i] - median_12mo[i])/median_12mo[i]
                st.metric(label = i, value =round(median_6mo[i]), delta="{:.4%}".format(delta))
            else:
                delta = median_6mo[i] - median_12mo[i]
                st.metric(label = 'Duration', value = delta.days, delta=f"{(delta//30)} Months")
            count += 1
            if count >= 6:
                count = 0


    df_agg_diff_final = df_agg_diff.loc[:,[
    'VIDEO',
    'VIDEO TITLE',
    'PUBLISH DATE',
    'COMMENTS',
    'SHARES',
    'DISLIKES',
    'LIKES',
    'SUBSCRIBERS LOST',
    'SUBSCRIBERS GAINED',
    'VIEWS',
    'SUBSCRIBERS',
    'YOUR ESTIMATED REVENUE (USD)',
    'IMPRESSIONS',
    'IMPRESSIONS CLICK-THROUGH RATE (%)',
    'AVERAGE VIEW DURATION',
    'AVERAGE VIEW SECONDS',
    'ENGAGEMENT RATIO',
    'VIEW TO SUBSCRIBER RATIO',
    'VIEW TO SUBSCRIBER LOST RATIO']
    ]
    
    # extract only date
    df_agg_diff_final['PUBLISH DATE'] = df_agg_diff_final['PUBLISH DATE'].dt.date

    # extracting time
    df_agg_diff_final['AVERAGE VIEW DURATION'] = df_agg_diff_final['AVERAGE VIEW DURATION'].dt.time

    # table
    table_sidebar = st.sidebar.selectbox("Count or percentage", ("Count values", "Percentage value"))
    
    if table_sidebar != 'Count values':

        # Select only the numeric columns
        numeric_columns = df_agg_diff_final.select_dtypes(include=['number'])

        df_agg_numeric_lst = df_agg_diff_final[df_agg_diff_final.columns[2:]].columns.tolist()
        
        #df_to_percent

        # Calculate column sums
        column_sums = numeric_columns.sum()

        # Divide each element by its column sum and multiply by 100 to get percentages and round
        #df_agg_diff_final = numeric_columns.applymap(lambda val: ((val / column_sums) * 100).round(4))

        df_to_percent = {}
        for i in numeric_columns:
            df_to_percent[i] = '{:.1%}'.format
            


        # Divide each element by its column sum and multiply by 100 to get percentages and round
        #df_percentage = (((numeric_columns / column_sums) * 100).round(4)).astype(str) + '%'



        # Include the previously excluded non-numeric columns
        #non_numeric_columns = df_agg_diff_final.select_dtypes(exclude=['number'])

        # Concatenate numeric and non-numeric columns
        #df_agg_diff_final = pd.concat([non_numeric_columns, df_percentage], axis=1)

        
        st.dataframe(df_agg_diff_final.style.hide().map(styling_positive, props = 'color:green;').map(styling_negative, props = 'color:red;').format(df_to_percent))
   
    else:
       # 
        st.dataframe(df_agg_diff_final.style.hide().map(styling_positive, props = 'color:green;').map(styling_negative, props = 'color:red;'))

elif add_sidebar =="Individual Video Analysis":

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    st.session_state.counter += 1

    st.header(f"This page has run {st.session_state.counter} times.")
    st.button("Run it again")

## individual video

# improvement

# styling

