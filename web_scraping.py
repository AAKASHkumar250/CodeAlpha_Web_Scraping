import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

with open("all_books_data.csv", "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.writer(file)
    writer.writerow(["Book Name", "Price", "Rating", "Availability"])

    for page in range(1, 51):

        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            availability = book.find(
                "p", class_="instock availability"
            ).text.strip()

            writer.writerow([title, price, rating, availability])

        print("Page completed:", page)

print("All books data saved successfully!")