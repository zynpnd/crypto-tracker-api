import requests
from django.http import JsonResponse

COINS = "bitcoin,ethereum,solana"

def prices(request):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": COINS,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params, timeout=5)
    data = response.json()

    return JsonResponse(data)
