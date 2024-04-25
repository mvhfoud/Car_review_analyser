import streamlit as st
import requests
from bs4 import BeautifulSoup
from IPython.display import Video
# import webbrowser
# import csv
import pandas as pd
url = "https://fr.carcarekiosk.com/"
response = requests.get(url)

# import re
# def replace_special_characters(text):
#         special_characters = {
#             "é": "e",
#             "è": "e",
#             "ê": "e",
#             "à": "a",
#             "â": "a",
#             "ô": "o",
#             "û": "u",
#             "ç": "c",
#             "ë": "e",
#             "ï": "i",
#             "ü": "u",
#             "ÿ": "y",
#             "ñ": "n",
#             "É": "E",
#             "È": "E",
#             "Ê": "E",
#             "À": "A",
#             "Â": "A",
#             "Ô": "O",
#             "Û": "U",
#             "Ç": "C",
#             "Ë": "E",
#             "Ï": "I",
#             "Ü": "U",
#             "Ÿ": "Y",
#             "Ñ": "N"
#         }
#         for char, replacement in special_characters.items():
#             text = re.sub(char, replacement, text)
#         return text
def find_models(car_make):
    car_make = car_make.replace("Š", "S").replace("ë", "e")
    car_url = url + "videos/" + car_make.replace(" ", "+")
    # Find all tags with class "card-body"
    response=requests.get(car_url)
    soup_car = BeautifulSoup(response.content, "html.parser")
    # Find the h1 tag 
    h1_tag = soup_car.find("h1", string=car_make)
    models=h1_tag.find_next_sibling("div").find_all("a")
    return models
def find_brands():
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all option tags inside id Make
    make = soup.find(id="Make").find_all("option")
    return make[1:]
  
def main():
    st.title("Car Review Analyzer")
    brands=find_brands()
    cars = [brand.text for brand in brands]

    # Input car brand
    # Create a dropdown list of available car brands
    brand = st.selectbox("Select a car brand", cars)
    # Get car models based on the brand
    car_models = find_models(brand)
    car_model_names = [model.text for model in car_models]
    car_model_links = [model["href"] for model in car_models]
    selected_model = st.selectbox("Select a car model", car_model_names)
    # get titles
    response=requests.get(car_model_links[car_model_names.index(selected_model)])
    soup_videos = BeautifulSoup(response.content, "html.parser")
    list_group_elements = soup_videos.find_all(class_="list-group-item")
    for list_group in list_group_elements:
        a_tags = list_group.find_all("a")
        for a_tag in a_tags:
            st.video("https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/")
            st.write(a_tag.text)
    # Do something with the a_tags
    # Find all video tags inside the card-header class
    # videos = card_header.find_all("video")
    # Find all h4 tags inside the card-header class
    # titles = card_header.find("a")
    # # Create a grid layout
    # Iterate over the titles
  # Leave the second column empty
    # col1, col2 = st.beta_columns(2)

    # # Iterate over the videos and titles
    # for video, title in zip(videos, titles):
    #     # Display the video and title in each grid cell
    #     with col1:
    #         st.video(video["src"])
    #     with col2:
    #         st.write(title.text)

if __name__ == "__main__":
    main()