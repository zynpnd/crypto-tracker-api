import requests
from django.http import JsonResponse

TOKENS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
}

def prices(request):
    results = {}

    for symbol, query in TOKENS.items():
        url = "https://api.dexscreener.com/latest/dex/search"
        params = {"q": query}

        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        pairs = data.get("pairs", [])
        if not pairs:
            results[symbol] = None
            continue

        # En likit pair'i al (ilk gelen genelde yeterli)
        pair = pairs[0]

        results[symbol] = {
            "priceUsd": pair.get("priceUsd"),
            "dex": pair.get("dexId"),
            "chain": pair.get("chainId"),
        }

    return JsonResponse({
        "source": "dexscreener",
        "data": results
    })
