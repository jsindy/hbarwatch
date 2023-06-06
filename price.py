import requests
import time
import re

def get_hbar_price():
    url = "https://cryptoprices.cc/HBAR/"
    response = requests.get(url)
    
    # Use regex to find the price
    price = re.findall("\d+\.\d+", response.text)[0]
    return float(price)

while True:
    # Using the function
    hbar_price = get_hbar_price()
    
    # Writing to a file
    with open('/var/www/html/price.txt', 'w') as f:
        f.write(str(hbar_price))

    # Waiting 30 seconds before the next run
    time.sleep(30)

