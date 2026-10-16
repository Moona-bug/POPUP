import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if api_key is None:
    raise RuntimeError("API_KEY not found. check your .env file.")

base_url = (f"https://api.marketstack.com/v2/eod?access_key={api_key}&symbols=AAPL")

companies = ["AAPL", "MSFT","GOOGL","TSLA","AMZN"]
response = requests.get(base_url, 
                        params={"access_key": api_key, "symbols": ",".join(companies)},
                        timeout=10)

response.raise_for_status()
info = response.json()

df = pd.json_normalize(info["data"])

print(df.columns.tolist())
# print(df.head(10))

fields = ["name", "symbol", "open", "high", "low", "close", "volume", "dividend", "price_currency", "date"]

df.to_csv("stock_info.csv", index=False)

print(f"Saved {len(info['data'])} rows to stock_info.csv")