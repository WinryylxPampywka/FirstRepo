from bs4 import BeautifulSoup
import  requests

response = requests.get ("https://books.toscrape.com/")
soup = BeautifulSoup()

book = soup.find_all('<a')

print("When We Collided")