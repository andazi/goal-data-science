import streamlit as st
import pandas as pd
import numpy as np

st.title('Fun with buttons')

# create buttons
st.button('Click me')

if st.button('click me'):
    st.write('I was clicked')
else:
    st.write('not clicked')

st.title('play with table and line chart')

# create a dataframe

df = pd.read_csv('dataset/plant and their meaning.csv', index_col=0)

if st.button('Show Table'):
    st.dataframe(df)



# line chart and dataframe

df1 = pd.DataFrame(
{   'month':  ['January','February','March','April','May','June','July','August','September','October','November', 'December',],
   'james': np.random.randint(10,50,12),
    'mary': np.random.randint(10,50,12),
    'judas': np.random.randint(10,50,12),
    'carrot': np.random.randint(10,50,12)
}
)

if st.button('Show dataframe'):
    st.dataframe(df1)
elif st.button('Show line chart'):
    st.line_chart(data=df1, x='month')


# creating two columns with table on left and chart on right

# created 2 columns
left_column, right_column = st.columns(2)

# create title on right column

right_column.write('Charts Display')

# left column would contain the buttons for table columns

with left_column:
    st.write('left column')
    for but in df1.columns:
        if but != 'month':
            if st.button(but):

                # chart on the right column
                with right_column:
                    st.write(but,"Line chart for the year")
                    st.line_chart(data=df1, x='month', y=but)


