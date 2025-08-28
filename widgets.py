import streamlit as st

name = st.text_input("Enter your name")
birth_year = st.number_input("Your birth year",min_value=1900,max_value=2100,step=1)

if name and birth_year:
  current_year = 2025
  age = current_year - birth_year
  st.write(f"Hello {name}! Your age is {age}")
