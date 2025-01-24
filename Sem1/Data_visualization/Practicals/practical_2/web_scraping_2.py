from bs4 import BeautifulSoup as bs
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    bs_response = bs(response.content, "lxml")
    quotes_span_tag = bs_response.find_all("span", class_="text")
    authors_small_tag = bs_response.find_all("small", class_="author")

    for (quote, author) in zip(quotes_span_tag, authors_small_tag):
        print(f"{quote.text}\nby {author.text}\n------", end="\n")
else:
    print(f"some error occured {response.status_code}")
