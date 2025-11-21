# importing libraries streamlit, numpy and pandas for to work with sample data.
import streamlit as st
import numpy as np
import pandas as pd
# Title of the app
st.title('My first app with Dataviz with 2025 Wuhan students of EFREI')

# Text in the app
st.write("Lets try to explore together. Here's our first attempt at using data to create a table:")
# Create a simple dataframe and display it as a table.

st.write(pd.DataFrame({ 'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]}))

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# Create chart data table
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
# Display a line chart
st.line_chart(chart_data)

# Create a data frame for map data
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [30.5928,114.3055],
    columns=['lat', 'lon'])
# Display the map
st.map(map_data)


# Add a checkbox to show/hide the dataframe
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

#explain the contexte.type of the figure (What we talk about)
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

#to load streamlit app with a progress bar
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'








