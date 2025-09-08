"""
Project: Currency Converter
Field: API Integration / Finance
Concepts Used: OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)
External Library: requests
API Source: ExchangeRate API (https://api.exchangerate.host)
"""

import requests
from abc import ABC, abstractmethod


class APIClient(ABC):
    """
    APIClient (Abstract Base Class):
    --------------------------------
    - Defines a contract for API clients.
    - Requires implementing fetch_data().
    """

    @abstractmethod
    def fetch_data(self, *args, **kwargs):
        pass


class CurrencyConverter(APIClient):
    """
    CurrencyConverter Class:
    -------------------------
    - Inherits from APIClient.
    - Fetches real-time exchange rates using ExchangeRate API.
    - Converts money from one currency to another.
    """

    BASE_URL = "https://api.exchangerate.host/convert"

    def __init__(self, base_currency: str, target_currency: str):
        """
        Initialize converter with base and target currencies.
        :param base_currency: Currency to convert from (e.g., "USD")
        :param target_currency: Currency to convert to (e.g., "PKR")
        """
        self.base_currency = base_currency.upper()
        self.target_currency = target_currency.upper()

    def fetch_data(self, amount: float):
        """
        Fetch conversion data from API.
        :param amount: Amount in base currency
        :return: JSON response from API
        """
        try:
            params = {
                "from": self.base_currency,
                "to": self.target_currency,
                "amount": amount
            }
            response = requests.get(self.BASE_URL, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"API Error: {response.status_code}")
        except Exception as e:
            print(f" Failed to fetch data: {e}")
            return {}

    def convert(self, amount: float) -> float:
        """
        Convert given amount from base currency to target currency.
        """
        data = self.fetch_data(amount)
        if data and "result" in data:
            return data["result"]
        else:
            return 0.0

    def display_conversion(self, amount: float):
        """
        Print conversion details.
        """
        converted_amount = self.convert(amount)
        if converted_amount:
            print(f"💱 {amount} {self.base_currency} = {converted_amount:.2f} {self.target_currency}")
        else:
            print(" Conversion failed.")
            

# ------------------ Example Usage ------------------ #
if __name__ == "__main__":
    converter = CurrencyConverter("USD", "PKR")
    converter.display_conversion(100)   # Convert 100 USD to PKR
