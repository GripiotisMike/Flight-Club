# Flight-Club
Flight Club is a Python application that uses the Tequila Flight Search API to find and display flight details for specified travel dates and destinations.

---

## Features
- 🛫 **Flight Search**: Fetches flight details for trips to Naxos (JNX) within a specified date range.
- 🛬 **Customizable Parameters**: Allows setting departure city, trip duration, and travel dates.

---

## Installation

1. Clone the repository

2. Install dependencies (pip install):
- requests
- python_dotenv

3. Get an API key from Tequila Flight Search API (https://tequila.kiwi.com/portal/getting-started) and replace it in my .env file

4. Run the application
- python main.py

---

## Usage
- The check_flights method in the FlightSearch class can be used to search for flights.
- Customize the origin_city_code, from_time, and to_time parameters to match your travel plans.
