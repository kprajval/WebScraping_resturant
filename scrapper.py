import requests
from bs4 import BeautifulSoup
import csv


def csv_function_writer(RestName, RestRating):
    with open('restaurants.csv', 'a', newline='') as file:
        fieldnames = ["NAME", "RATING"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow({"NAME": RestName, "RATING": RestRating})


for i in range(1, 63):
    url = "https://www.dineout.co.in/bangalore-restaurants/welcome-back?p=" + str(i)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    restaurants = soup.find_all("div", class_="restnt-card")

    for restaurant in restaurants:
        name = restaurant.find("a", class_="restnt-name").text
        rating = restaurant.find("div", class_="restnt-rating").text
        csv_function_writer(name, rating)
