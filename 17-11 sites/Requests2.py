from bs4 import BeautifulSoup
import  requests
# response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
# soup = BeautifulSoup(response.text, features="html.parser")
# bitcoin = soup.find("span, {"class": "sc-65e7f566-0 WXGwg base-text"})
# print("bitcoin.text")

response = requests.get ("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")
coins = soup.find_all('p', {"class": "sc-65e7f566-0 iPbTJf coin-item-name"})
coins = soup.find_all('p', {"class": "sc-65e7f566-0 iPbTJf coin-item-name"})

file = open("coins.txt", 'w')
for i in range(0, len (coins[0])):
    print(f"{coins [0][i].text"} {coins[1][i].text}")

    file.close()
