import requests
from bs4 import BeautifulSoup
import csv
import json
import os

# Target URL for practice
url = "https://books.toscrape.com/"

# Custom headers to simulate a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

# Create output directory
os.makedirs("output", exist_ok=True)

def fetch_html():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
        return None

def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")

    # Extract book titles and prices
    books = soup.find_all("article", class_="product_pod")
    book_list = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        link = url + book.h3.a["href"]
        book_list.append({"title": title, "price": price, "link": link})

    return book_list

def save_to_csv(data):
    with open("output/scraped_data.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "link"])
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data):
    with open("output/scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():
    print("🔍 Scraping book data from books.toscrape.com...")
    html = fetch_html()
    if html:
        book_data = parse_data(html)
        save_to_csv(book_data)
        save_to_json(book_data)
        print("✅ Data saved in 'output/scraped_data.csv' and 'scraped_data.json'")
    else:
        print("⚠️ Could not fetch or parse the HTML content.")

if __name__ == "__main__":
    main()
