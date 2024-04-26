import requests
import re

msft_price_pattern = re.compile(r"406\.32")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

resp = requests.get(
    "https://finance.yahoo.com/quote/MSFT", headers=headers
)
# print(resp.text)

found_match = msft_price_pattern.search(resp.text)

print(
    found_match
)  # use the match on the specific price, to access the surrounding html

# then use the surrounding html to do a capture pattern to get the price no matter what it
price_pattern = re.compile(r"active><span>(.*?)</span></fin-streamer>")

print(float(price_pattern.search(resp.text).groups()[0]))
