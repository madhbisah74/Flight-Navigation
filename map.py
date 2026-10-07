import os
import webbrowser
import math

import plotly.graph_objects as go


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


# ============================================================
# AIRPORT DATA
# ============================================================

AIRPORTS = {

    "DEL": {
        "city": "Delhi",
        "country": "India",
        "lat": 28.5562,
        "lon": 77.1000
    },

    "BOM": {
        "city": "Mumbai",
        "country": "India",
        "lat": 19.0896,
        "lon": 72.8656
    },

    "BLR": {
        "city": "Bengaluru",
        "country": "India",
        "lat": 13.1986,
        "lon": 77.7066
    },

    "MAA": {
        "city": "Chennai",
        "country": "India",
        "lat": 12.9941,
        "lon": 80.1709
    },

    "HYD": {
        "city": "Hyderabad",
        "country": "India",
        "lat": 17.2403,
        "lon": 78.4294
    },

    "CCU": {
        "city": "Kolkata",
        "country": "India",
        "lat": 22.6547,
        "lon": 88.4467
    },

    "DXB": {
        "city": "Dubai",
        "country": "UAE",
        "lat": 25.2532,
        "lon": 55.3657
    },

    "LHR": {
        "city": "London",
        "country": "UK",
        "lat": 51.4700,
        "lon": -0.4543
    },

    "CDG": {
        "city": "Paris",
        "country": "France",
        "lat": 49.0097,
        "lon": 2.5479
    },

    "FRA": {
        "city": "Frankfurt",
        "country": "Germany",
        "lat": 50.0379,
        "lon": 8.5622
    },

    "JFK": {
        "city": "New York",
        "country": "USA",
        "lat": 40.6413,
        "lon": -73.7781
    },

    "LAX": {
        "city": "Los Angeles",
        "country": "USA",
        "lat": 33.9416,
        "lon": -118.4085
    },

    "YYZ": {
        "city": "Toronto",
        "country": "Canada",
        "lat": 43.6777,
        "lon": -79.6248
    },

    "SIN": {
        "city": "Singapore",
        "country": "Singapore",
        "lat": 1.3644,
        "lon": 103.9915
    },

    "HKG": {
        "city": "Hong Kong",
        "country": "Hong Kong",
        "lat": 22.3080,
        "lon": 113.9185
    },

    "NRT": {
        "city": "Tokyo",
        "country": "Japan",
        "lat": 35.5494,
        "lon": 139.7798
    },

    "SYD": {
        "city": "Sydney",
        "country": "Australia",
        "lat": -33.9399,
        "lon": 151.1753
    },

    "JNB": {
        "city": "Johannesburg",
        "country": "South Africa",
        "lat": -26.1367,
        "lon": 28.2411
    },

    "CAI": {
        "city": "Cairo",
        "country": "Egypt",
        "lat": 30.1120,
        "lon": 31.4000
    },

    "IST": {
        "city": "Istanbul",
        "country": "Turkey",
        "lat": 41.2753,
        "lon": 28.7519
    },

    "GRU": {
        "city": "São Paulo",
        "country": "Brazil",
        "lat": -23.4356,
        "lon": -46.4731
    }
}


# ============================================================
# FLIGHT DATA
# ============================================================

FLIGHTS = [

    ("AI101", "Air India", "DEL", "LHR"),
    ("AI102", "Air India", "LHR", "DEL"),

    ("AI701", "Air India", "DEL", "DXB"),
    ("AI702", "Air India", "DXB", "DEL"),

    ("6E201", "IndiGo", "DEL", "BOM"),
    ("6E305", "IndiGo", "BLR", "DEL"),

    ("AI501", "Air India", "DEL", "BLR"),
    ("AI502", "Air India", "BLR", "DEL"),

    ("EK511", "Emirates", "DEL", "DXB"),
    ("EK500", "Emirates", "DXB", "JFK"),

    ("SQ423", "Singapore Airlines", "DEL", "SIN"),
    ("SQ424", "Singapore Airlines", "SIN", "DEL"),

    ("LH761", "Lufthansa", "DEL", "FRA"),
    ("LH760", "Lufthansa", "FRA", "DEL"),

    ("AF225", "Air France", "DEL", "CDG"),

    ("BA142", "British Airways", "DEL", "LHR"),

    ("BA143", "British Airways", "LHR", "JFK"),

    ("AA100", "American Airlines", "JFK", "LAX"),
    ("AA101", "American Airlines", "LAX", "JFK"),

    ("AC700", "Air Canada", "YYZ", "LHR"),

    ("JL001", "Japan Airlines", "NRT", "JFK"),
    ("JL002", "Japan Airlines", "JFK", "NRT"),

    ("SQ012", "Singapore Airlines", "SIN", "NRT"),

    ("QF001", "Qantas", "SYD", "LHR"),

    ("EK412", "Emirates", "SYD", "DXB"),

    ("QR900", "Qatar Airways", "DXB", "LHR"),

    ("TK001", "Turkish Airlines", "IST", "JFK"),

    ("MS985", "EgyptAir", "CAI", "JFK"),

    ("SA203", "South African Airways", "JNB", "LHR"),

    ("LA8084", "LATAM", "GRU", "LHR"),

    ("EK201", "Emirates", "DXB", "JFK"),

    ("EK202", "Emirates", "JFK", "DXB"),

    ("CX830", "Cathay Pacific", "HKG", "JFK"),

    ("CX831", "Cathay Pacific", "JFK", "HKG"),

    ("SQ322", "Singapore Airlines", "SIN", "LHR"),

    ("QF002", "Qantas", "LHR", "SYD"),

    ("AI310", "Air India", "BOM", "LHR"),

    ("AI311", "Air India", "LHR", "BOM"),

    ("AI410", "Air India", "BOM", "DXB"),

    ("AI411", "Air India", "DXB", "BOM"),

    ("6E700", "IndiGo", "BOM", "SIN"),

    ("6E701", "IndiGo", "SIN", "BOM"),

    ("6E900", "IndiGo", "CCU", "DXB"),

    ("6E901", "IndiGo", "DXB", "CCU"),

    ("AI600", "Air India", "MAA", "SIN"),

    ("AI601", "Air India", "SIN", "MAA"),

    ("AI800", "Air India", "HYD", "DXB"),

    ("AI801", "Air India", "DXB", "HYD")
]


# ============================================================
# CREATE CURVED ROUTE
# ============================================================

def create_route(
    lat1,
    lon1,
    lat2,
    lon2,
    points=40
):

    lats = []
    lons = []

    for i in range(points + 1):

        t = i / points

        lat = (
            lat1
            +
            (lat2 - lat1) * t
        )

        lon = (
            lon1
            +
            (lon2 - lon1) * t
        )

        # Create slight curve
        curve = (
            math.sin(math.pi * t)
            * 8
        )

        lat += curve

        lats.append(lat)
        lons.append(lon)

    return lats, lons


# ============================================================
# CREATE GLOBAL MAP
# ============================================================

def create_global_map():

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    fig = go.Figure()

    # ========================================================
    # WORLD MAP
    # ========================================================

    # This uses Plotly's built-in geographic rendering.
    # No OpenStreetMap tiles are used.
    fig.add_trace(
        go.Scattergeo(
            lon=[0],
            lat=[0],

            mode="markers",

            marker={
                "size": 1,
                "opacity": 0
            },

            hoverinfo="skip",

            showlegend=False
        )
    )

    # ========================================================
    # FLIGHT ROUTES
    # ========================================================

    for flight_number, airline, start_code, end_code in FLIGHTS:

        start = AIRPORTS[start_code]
        end = AIRPORTS[end_code]

        route_lats, route_lons = create_route(
            start["lat"],
            start["lon"],
            end["lat"],
            end["lon"]
        )

        hover_text = (
            f"<b>✈ {flight_number}</b><br>"
            f"Airline: {airline}<br>"
            f"From: {start['city']} ({start_code})<br>"
            f"To: {end['city']} ({end_code})"
        )

        fig.add_trace(
            go.Scattergeo(

                lon=route_lons,

                lat=route_lats,

                mode="lines",

                line={
                    "color": "black",
                    "width": 1,
                    "dash": "dot"
                },

                text=hover_text,

                hoverinfo="text",

                showlegend=False
            )
        )

        # ====================================================
        # AIRCRAFT POSITION
        # ====================================================

        middle = len(route_lats) // 2

        plane_lat = route_lats[middle]
        plane_lon = route_lons[middle]

        fig.add_trace(
            go.Scattergeo(

                lon=[plane_lon],

                lat=[plane_lat],

                mode="text",

                text=["✈"],

                textfont={
                    "size": 18,
                    "color": "black"
                },

                hovertext=hover_text,

                hoverinfo="text",

                showlegend=False
            )
        )

    # ========================================================
    # AIRPORTS
    # ========================================================

    airport_lats = []
    airport_lons = []
    airport_text = []

    for code, airport in AIRPORTS.items():

        airport_lats.append(
            airport["lat"]
        )

        airport_lons.append(
            airport["lon"]
        )

        airport_text.append(
            f"<b>🔴 {airport['city']}</b><br>"
            f"{airport['country']}<br>"
            f"IATA: {code}"
        )

    fig.add_trace(
        go.Scattergeo(

            lon=airport_lons,

            lat=airport_lats,

            mode="markers",

            marker={
                "size": 7,
                "color": "red"
            },

            text=airport_text,

            hoverinfo="text",

            showlegend=False
        )
    )

    # ========================================================
    # MAP DESIGN
    # ========================================================

    fig.update_geos(

        projection_type="equirectangular",

        showland=True,

        landcolor="#b7d8ee",

        showocean=True,

        oceancolor="#ffffff",

        showlakes=True,

        lakecolor="#ffffff",

        showcountries=True,

        countrycolor="#ffffff",

        countrywidth=0.7,

        coastlinecolor="#ffffff",

        coastlinewidth=0.8,

        showframe=False,

        bgcolor="#ffffff",

        lonaxis={
            "showgrid": False
        },

        lataxis={
            "showgrid": False
        }
    )

    # ========================================================
    # TITLE
    # ========================================================

    fig.update_layout(

        title={
            "text": "✈ GLOBAL FLIGHT NAVIGATION SYSTEM",
            "x": 0.5,
            "xanchor": "center",

            "font": {
                "size": 24,
                "color": "#222222"
            }
        },

        paper_bgcolor="white",

        plot_bgcolor="white",

        margin={
            "l": 0,
            "r": 0,
            "t": 70,
            "b": 0
        },

        height=700,

        showlegend=False
    )

    # ========================================================
    # SAVE HTML
    # ========================================================

    output_file = os.path.join(
        OUTPUT_DIR,
        "global_flight_map.html"
    )

    fig.write_html(
        output_file,
        include_plotlyjs=True
    )

    # ========================================================
    # OPEN IN BROWSER
    # ========================================================

    webbrowser.open(
        "file://" +
        os.path.abspath(output_file)
    )

    return output_file


