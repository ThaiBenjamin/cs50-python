import requests
import sys
import json

if len(sys.argv) != 2:
    print("Missing command line argument!")
    sys.exit(1)

else:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number!")
        sys.exit(1)

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=86c0e223484fdc48072463a33cab86b03d908ef90904efadffed69e474b68a87")
    price_usd = float(response.json()["data"]["priceUsd"]) * float(sys.argv[1])
    print(f"${price_usd:,.4f}")
except requests.RequestException:
    print("Request Exception")
    sys.exit(1)
