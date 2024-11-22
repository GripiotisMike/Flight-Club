import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")  # Fetch API key from environment variables

today = datetime.today()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

class FlightSearch:
    """
    A class to interact with the Tequila Flight Search API.
    """

    def check_flights(self, origin_city_code, from_time, to_time):
        """
        Searches for flights based on specified parameters.
        :param origin_city_code: IATA code for the departure city
        :param from_time: Start date of the flight search range
        :param to_time: End date of the flight search range
        :return: FlightData object or None if no flights found
        """
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": "JNX",  # Destination: Naxos
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for Naxos.")
            return None

        flight_data = {
            "price": data["price"],
            "origin_city": data["route"][0]["cityFrom"],
            "origin_airport": data["route"][0]["flyFrom"],
            "destination_city": data["route"][0]["cityTo"],
            "destination_airport": data["route"][0]["flyTo"],
            "out_date": data["route"][0]["local_departure"].split("T")[0],
            "return_date": data["route"][1]["local_departure"].split("T")[0]
        }
        print(f"{flight_data['destination_city']}: {flight_data['price']} €")
        return flight_data
