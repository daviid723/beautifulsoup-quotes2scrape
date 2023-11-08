import requests as rq

link = "https://quotes.toscrape.com/"
response = rq.get(link)

print(response.text)
