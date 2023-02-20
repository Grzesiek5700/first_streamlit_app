import streamlit as st

st.title('My Parents New Healty Diner')

st.header('Breakfast Favorites')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard_Boiled Free_Range Egg')
st.text('🥑🍞Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.multiselect("Pick some fruits:", list(my_fruit_list.index))
df = st.dataframe(my_fruit_list)
