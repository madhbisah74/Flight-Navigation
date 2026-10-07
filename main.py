import os

from flights import (
    find_flight,
    display_all_flights
)

from navigation import (
    get_airport,
    calculate_distance,
    calculate_bearing,
    bearing_direction
)

from map import create_global_map

def print_header():


    print()
    print("=" * 70)
    print("              ✈️ FLIGHT NAVIGATION SYSTEM")
    print("=" * 70)


def display_flight_information(
    flight,
    departure,
    destination,
    distance,
    bearing,
    direction
):

    print()
    print("=" * 70)
    print("                    FLIGHT INFORMATION")
    print("=" * 70)

    print(f"Flight Number : {flight['flight_number']}")
    print(f"Airline       : {flight['airline']}")
    print(f"Aircraft      : {flight['aircraft']}")

    print()
    print(
        f"Departure     : "
        f"{departure['city']} "
        f"({flight['departure']})"
    )

    print(
        f"Destination   : "
        f"{destination['city']} "
        f"({flight['destination']})"
    )

    print()
    print(f"Distance      : {distance:,.2f} km")
    print(f"Bearing       : {bearing:.2f}°")
    print(f"Direction     : {direction}")

    print("=" * 70)


def main():

    print_header()

    while True:

        print()
        print("1. Search Flight")
        print("2. Show All Flights")
        print("3. Show Global Flight Map")
        print("4. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # --------------------------------
        # SEARCH FLIGHT
        # --------------------------------

        if choice == "1":

            print()

            flight_number = input(
                "Enter flight number: "
            ).strip()

            flight = find_flight(
                flight_number
            )

            if flight is None:

                print()
                print(
                    "❌ Flight not found."
                )

                continue

            # Get airports

            departure = get_airport(
                flight["departure"]
            )

            destination = get_airport(
                flight["destination"]
            )

            if departure is None:

                print(
                    "❌ Departure airport "
                    "information not found."
                )

                continue

            if destination is None:

                print(
                    "❌ Destination airport "
                    "information not found."
                )

                continue

            # Calculate distance

            distance = calculate_distance(
                departure["latitude"],
                departure["longitude"],
                destination["latitude"],
                destination["longitude"]
            )

            # Calculate bearing

            bearing = calculate_bearing(
                departure["latitude"],
                departure["longitude"],
                destination["latitude"],
                destination["longitude"]
            )

            direction = bearing_direction(
                bearing
            )

            # Display information

            display_flight_information(
                flight,
                departure,
                destination,
                distance,
                bearing,
                direction
            )


        # --------------------------------
        # SHOW ALL FLIGHTS
        # --------------------------------

        elif choice == "2":

            display_all_flights()

        # --------------------------------
        # EXIT
        # --------------------------------


        elif choice == "3":
 
         print()
         print("Creating global flight map...")
 
         map_file = create_global_map()
 
         print()
         print("✅ Global flight map created!")
         print()
         print("Map file:")
         print(map_file)
 
         print()
         print(
            "Open global_flight_map.html "
            "in your browser."
       )
        elif choice == "4":

         print()
         print("Thank you for using Flight Navigation System!")

         break

if __name__ == "__main__":
    main()