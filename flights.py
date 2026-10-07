import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FLIGHTS_FILE = os.path.join(BASE_DIR, "data", "flights.json")


def load_flights():
    """
    Load all flight information from flights.json.
    """

    try:
        with open(FLIGHTS_FILE, "r", encoding="utf-8") as file:
            flights = json.load(file)

        return flights

    except FileNotFoundError:
        print("ERROR: flights.json file was not found.")
        return []

    except json.JSONDecodeError:
        print("ERROR: flights.json contains invalid JSON.")
        return []


def find_flight(flight_number):
    """
    Search for a flight using its flight number.
    """

    flights = load_flights()

    flight_number = flight_number.strip().upper()

    for flight in flights:

        if flight["flight_number"].upper() == flight_number:
            return flight

    return None


def display_all_flights():
    """
    Display all available flights.
    """

    flights = load_flights()

    if not flights:
        print("No flights available.")
        return

    print("\nAvailable Flights")
    print("=" * 70)

    for flight in flights:

        print(
            f'{flight["flight_number"]:8} | '
            f'{flight["airline"]:20} | '
            f'{flight["departure"]} -> {flight["destination"]}'
        )

    print("=" * 70)