from bs4 import BeautifulSoup
import  requests
response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
soup = BeautifulSoup(response.text, features="html.parser")
bitcoin = soup.find("span, {"class": "sc-65e7f566-0 WXGwg base-text"})
print("bitcoin.text")