''' import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    print(f"{text} — {author}") '''

'''import requests
from bs4 import BeautifulSoup
url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
for book in soup.select("tr[itemtype='http://schema.org/Book']")[:10]:
    title = book.select_one("a.bookTitle span").get_text(strip=True)
    author = book.select_one("a.authorName span").get_text(strip=True)
    print(f"{title} — {author}")'''


import requests

query = "comedy"
url = f"https://openlibrary.org/search.json?q={query}"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    books = data.get("docs", [])

    for book in books[:10]:
        title = book.get("title")
        author = book.get("author_name", ["Unknown"])[0]
        print(f"{title} — {author}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

