import requests as rq
from bs4 import BeautifulSoup as bs

# Send a http request to the website
link = "https://quotes.toscrape.com/"
response = rq.get(link)

# Create a soup object similar to DOM
soup = bs(response.content, 'html.parser')

# Find all authors Elements
authors = soup.find_all('small', class_ = 'author')

# Find all quote Elements
quotes = soup.find_all('span', class_ = 'text')

# Print all authors
for count, quote in enumerate(quotes):
    print(quote.text)
    print(f"By: {authors[count].text}\n\n")
