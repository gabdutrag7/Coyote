from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status": "PriceSafe online 🚀"}

@app.get("/search")
def search(q: str):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={q}"
    res = requests.get(url)
    data = res.json()

    results = []

    for item in data["results"][:10]:
        results.append({
            "name": item["title"],
            "price": item["price"],
            "url": item["permalink"]
        })

    return results
