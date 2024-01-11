# cryptocurrency
import requests

api_key = "CG-Q9Bbx9qZhmB7QNGTw7GU3UCJ"
base_url = "https://api.coingecko.com/api/v3/coins/"

cryptocurrency = input("Enter the cryptocurrency name:-").lower()

url = f"{base_url}{cryptocurrency}"
 
'''headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}'''

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Details for {cryptocurrency.upper()}:")
    print("Name:", data['name'])
    print("Symbol:", data['symbol'])
    print("Current Price (₹):", data['market_data']['current_price']['usd']*83)
    
else:
    print(f"Failed to fetch data for {cryptocurrency}. Status code:", response.status_code)