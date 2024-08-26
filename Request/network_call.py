import json
import requests

# ---------- Url ----------
# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html

# ---------- Step one ----------
"""
response = requests.get("https://codeavecjonathan.com/res/programmation.txt")

if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
else:
    print(f"Error: code {response.status_code}")
"""
# ---------- Step two ----------
"""
response = requests.get("https://codeavecjonathan.com/res/pizzas1.json")

if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
    pizzas = json.loads(response.text)
    print(f"Pizza's number: {len(pizzas)}")
else:
    print(f"Error: code {response.status_code}")
"""
# ---------- Step three ----------

response = requests.get("https://codeavecjonathan.com/res/exemple.html")

if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
else:
    print(f"Error: code {response.status_code}")