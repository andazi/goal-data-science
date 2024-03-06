import streamlit as st
import pandas as pd
import numpy as np

# title
st.title("Hello DataApp")

# text
st.write('Hello World')

# table
st.title('My first table')
df = pd.DataFrame(
    {
        "Name": ['Stream', 'water', 'ice', 'vapor'],
        "range": [230,200,190, 170]
    }
)

df

# interactive table 
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


# lets style it
st.title('interactive table with style object to hightlight some elements')
dataframe = pd.DataFrame(
    np.random.randn(10,20),

    columns=('col %d' % i for i in range(20))
) 
st.dataframe(dataframe.style.highlight_max(axis=0))

# static table

st.title('static table')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.title('Reading a csv file')
dataframe = pd.read_csv('dataset/flowers and their meaning.csv', index_col=0)
st.dataframe(dataframe)

# draw line chart

st.title('line chart')

df1 = pd.DataFrame(
{   'month':  ['January','February','March','April','May','June','July','August','September','October','November', 'December',],
   'james': np.random.randint(10,50,12),
    'mary': np.random.randint(10,50,12),
    'judas': np.random.randint(10,50,12),
    'carrot': np.random.randint(10,50,12)
}
)

st.dataframe(df1)

st.line_chart(data = df1, x = 'month' )

# draw a map

st.title('map')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
    )

st.map(map_data)

# draw a widget with operation

st.title('widgets')

x = st.slider('x')
st.write('The squared of ', x, '=', x * x)

# widget on temparature, celsius to kelvin
st.write('celsius to kelvin')

celsius = st.slider('celsius temperature')

k_to_c = celsius + 273.15

st.write(celsius,'celsius  is equal to  ',k_to_c, 'kelvin')

# session

st.text_input('you name', key='name')

st.session_state.name

# checkbox

st.title('checkbox')

if st.checkbox('Show mapping dataframe'):
    chart_data = map_data

    chart_data

# selectbox

st.title('selectbox')

option = st.selectbox(
    'whose sales record do you want to check',
    [col for col in df1.columns if col != 'month']
)

option, 'sales records'

df1[['month',option]]

st.write(option, 'chart')
st.line_chart(data = df1, x='month', y=option)

# layout

st.sidebar.title('layout')
# add selectbox to sidebar
add_selectbox = st.sidebar.selectbox(
    'Please select course',
    ('Python', 'C#', 'SQL', 'javascript')
)

# add slider to sidebar

add_slider = st.sidebar.slider(
    'Select experience range',
    0,100, (50,100)
)


# columns and radio

st.title('columns and radio')

left_column, right_column = st.columns(2)

# using a column as sidebar
left_column.button('press me')

#calling a streamlit button inside a 'with' block

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# radio most be unique
with right_column:
    chosen = st.radio(
        'The Sorting has',
        ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"])
    st.write(f"You are in {chosen} house!")




import time 
    # showing progress

with st.sidebar:
    
    st.title('showing progress')
    'strating a long compution....'

    # placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
        # update the progress bar with each iteration
        latest_iteration.text(f'Iteration i+1')
        bar.progress(i+1)
        time.sleep(0.1)

    '.... and now we are done!!!'