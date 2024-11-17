from bs4 import BeautifulSoup
import  requests

response = requests.get ("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features="html.parser")

book = soup.find_all('h3')

print(book)