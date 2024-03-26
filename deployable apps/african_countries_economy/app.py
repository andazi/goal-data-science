# Importing our libraries
import pandas as pd  # Data manipulation
import numpy as np   # Numerical operations
import matplotlib.pyplot as plt  # Data visualization
import streamlit as st # streamlit


# load data
df = pd.read_csv('resource/ObservationData_lavlqce.csv')

st.dataframe(df)

# clean data

# extract necessary columns

# build app

# matplotlib

data = pd.DataFrame({
    'meow':[5, 12, 30], 
    'woof':[4, 8, 12]}
    )
st.dataframe(data)
#fig, ax = plt.subplots()
#ax.scatter()
#st.pyplot(fig)

st.line_chart(x='meow', data=data)

