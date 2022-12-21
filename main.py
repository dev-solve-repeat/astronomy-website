import streamlit as st
import requests

st.set_page_config(layout="centered")

api_key = "QAe5fujLLi5W1eUkVcMwKJIcam9al0q8cygQ9bYX"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

response1 = requests.get(url)
data1 = response1.json()

title = data1["title"]
image_url = data1["hdurl"]
explanation = data1["explanation"]

response2 = requests.get(image_url)
data2 = response2.content

image_filepath = "image.png"
with open(image_filepath, "wb") as image_file:
    image_file.write(data2)

st.title(title)
st.image(image_filepath)
st.info(explanation)