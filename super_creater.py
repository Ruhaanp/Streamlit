
#super creater 
import streamlit as st

st.title("Super profile creator")

name = st.text_input("Enter your super name")

age = st.number_input("Enter your super's age")

backstory = st.text_area("Write your super backstory")

superpower = st.selectbox("Choose your main superpower", ["Flying","Invisibility","Mind Reading","Time Travel", "Super Strength", "Iron Hands"])

sidekicks = st.multiselect("Pick your super team", ["Robin", "Bucky Barnes", "Kid Flash", "Speedy", "Aqualad", "Superboy", "Wonder Girl", "Harley Quinn", "Black Tom Cassidy", "Rhino", "Executioner", "Toad with Magneto"])

strength = st.slider("Rate your power level", 1,100,50)

alignment = st.radio("Are you a hero or a villain?", ["Hero","villain"])

if st.button("Generate Superhero story"):
  st.subheader("Your superhero profile:")
  st.write(f"Name: {name}")
  st.write(f"Age: {age}")
  st.write(f"Backstory: {backstory}")
  st.write(f"Superpower: {superpower}")
  st.write(f"sidekicks: {sidekicks}")
  st.write(f"Strength: {strength}")
  st.write(f"Alignment: {alignment}")
