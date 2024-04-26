import requests
import re
import json
from pathlib import Path

# Mini-lab

# 1. Select 5 stock symbols, get the price for each one, and save the price and symbol for each one to a single JSON file.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
price_pattern = re.compile(r"active><span>(.*?)</span></fin-streamer>")
symbols = ["MSFT", "T", "AAPL", "AMZN", "FB"]
result = {}

for symbol in symbols:
    resp = requests.get(
        f"https://finance.yahoo.com/quote/{symbol}", headers=headers
    )

    result[symbol] = float(price_pattern.search(resp.text).groups()[0])

with Path("output.json").open("w", encoding="UTF-8") as output_file:
    json.dump(result, output_file, indent=2)
