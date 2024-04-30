##### Similar to webscraping-tradingview #####
# Instructions #
    # Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and 
    # display as a formatted output one currency at a time. The output should display the name of the 
    # currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding 
    # price (based on % change)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table = soup.find('table', attrs={"class":"cmc-table"}) # cmc-table references the entire table
data = table.find_all('tr')[1:6]  # Selecting the first 5 rows with actual data, skipping the header

# Iterates thru each row and extracts data
for x in data:
    cols = x.find_all('td')
    name = cols[2].find('p').text.strip()  # Cryptocurrency name
    symbol = cols[2].find('p', class_='coin-item-symbol').text.strip()  # Cryptocurrency symbol
    price = cols[3].find('div').text.strip()  # Current price
    per_change = cols[4].find('span').text.strip()  # % Change in the last 24 hrs
    change_num = float(per_change.strip('+').strip('%'))  # Convert change to float for calculation
    if per_change.startswith('-'): # Checks for negative percentages
        prev_price = round(float(price.strip('$').replace(',', '')) / (1-change_num/100),2) # Negative %
    else:
        prev_price = round(float(price.strip('$').replace(',', '')) / (1+change_num/100),2) # Positive %
    #prev_price = round(prev_price, 2)  # Previous price based on the % change

    # Print Results
    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Current Price: {price}")
    print(f"% Change 24 Hrs: {per_change}")
    print(f"Price 24 Hrs Ago: ${prev_price}")
    print()

#Garrett Austin