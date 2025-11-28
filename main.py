from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Wingo Predictor API Running"}

@app.post("/predict")
def predict(data: dict):
    url = data.get("url")

    try:
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, "html.parser")

        numbers = [int(n.text.strip()) for n in soup.find_all("div")
                   if n.text.strip().isdigit()]

        if len(numbers) == 0:
            return {"error": "No numbers found"}

        freq = {}
        for n in numbers:
            freq[n] = freq.get(n, 0) + 1

        next_num = max(freq, key=freq.get)
        big_small = "Big" if next_num >= 5 else "Small"

        return {
            "next_number": next_num,
            "big_small": big_small,
            "confidence": round((freq[next_num] / len(numbers)) * 5, 2)
        }

    except Exception as e:
        return {"error": str(e)}
