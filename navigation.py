import json
import os
import math


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AIRPORT_FILE = os.path.join(BASE_DIR, "data", "airports.json")


def load_airports():
    """
    Load airport information.
    """

    try:

        with open(AIRPORT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:

        print("ERROR: airports.json was not found.")
        return {}

    except json.JSONDecodeError:

        print("ERROR: airports.json contains invalid JSON.")
        return {}


def get_airport(code):
    """
    Return airport information using its IATA code.
    """

    airports = load_airports()

    return airports.get(code.upper())


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance using the Haversine formula.

    Returns distance in kilometers.
    """

    earth_radius = 6371.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        math.sin(delta_lat / 2) ** 2
        +
        math.cos(lat1)
        * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius * c


def calculate_bearing(lat1, lon1, lat2, lon2):
    """
    Calculate initial compass bearing.

    Returns a value between 0 and 360 degrees.
    """

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    difference_longitude = math.radians(
        lon2 - lon1
    )

    x = (
        math.sin(difference_longitude)
        * math.cos(lat2)
    )

    y = (
        math.cos(lat1)
        * math.sin(lat2)
        -
        math.sin(lat1)
        * math.cos(lat2)
        * math.cos(difference_longitude)
    )

    bearing = math.degrees(
        math.atan2(x, y)
    )

    bearing = (bearing + 360) % 360

    return bearing


def bearing_direction(bearing):
    """
    Convert bearing degrees to compass direction.
    """

    directions = [
        "N",
        "NE",
        "E",
        "SE",
        "S",
        "SW",
        "W",
        "NW"
    ]

    index = int(
        (bearing + 22.5) / 45
    ) % 8

    return directions[index]