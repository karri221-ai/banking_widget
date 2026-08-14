import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount,
    }
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return float(data["result"])
