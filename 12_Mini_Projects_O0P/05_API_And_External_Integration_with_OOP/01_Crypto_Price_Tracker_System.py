"""
Project: Crypto Price Tracker
Field: API Integration / FinTech
Concepts Used: OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)
External Library: requests
API Source: CoinGecko (Free & Public API)
"""

import requests
from abc import ABC, abstractmethod


class APIClient(ABC):
    """
    APIClient (Abstract Base Class):
    --------------------------------
    - Defines the structure for any API client.
    - Requires implementing fetch_data().
    """

    @abstractmethod
    def fetch_data(self, *args, **kwargs):
        pass


class CryptoPriceTracker(APIClient):
    """
    CryptoPriceTracker Class:
    -------------------------
    - Inherits from APIClient.
    - Uses CoinGecko API to fetch real-time cryptocurrency prices.
    """

    BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

    def __init__(self, coins: list, currency: str = "usd"):
        """
        Initialize the tracker.
        :param coins: List of crypto IDs (e.g., ["bitcoin", "ethereum"])
        :param currency: Currency to compare against (default: USD)
        """
        self.coins = coins
        self.currency = currency

    def fetch_data(self):
        """
        Fetch live prices from CoinGecko API.
        """
        try:
            params = {"ids": ",".join(self.coins), "vs_currencies": self.currency}
            response = requests.get(self.BASE_URL, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"API Error: {response.status_code}")
        except Exception as e:
            print(f"❌ Failed to fetch data: {e}")
            return {}

    def display_prices(self):
        """
        Display the current prices of selected cryptocurrencies.
        """
        data = self.fetch_data()
        if data:
            print("💰 Live Crypto Prices:")
            for coin, price in data.items():
                print(f"   - {coin.capitalize()}: {price[self.currency]} {self.currency.upper()}")


# ------------------ Example Usage ------------------ #
if __name__ == "__main__":
    # Choose cryptos to track
    coins = ["bitcoin", "ethereum", "dogecoin"]

    tracker = CryptoPriceTracker(coins, currency="usd")
    tracker.display_prices()
