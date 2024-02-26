class Passenger:
    def __init__(self, full_name, identification_number, frequent_flyer_number=None):
        self.full_name = full_name
        self.identification_number = identification_number
        self.frequent_flyer_number = frequent_flyer_number
        self.booked_flights = []

    def update_information(self, new_name=None, new_id=None):
        if new_name:
            self.full_name = new_name
        if new_id:
            self.identification_number = new_id
        # This function updates the passenger's personal information.

    def check_in(self, flight_number):
        # This function would interact with a Flight class to check the passenger in for a flight.
        pass


class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, origin, destination, aircraft_type):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination
        self.aircraft_type = aircraft_type
        self.passenger_list = []

    def update_schedule(self, new_departure_time=None, new_arrival_time=None):
        if new_departure_time:
            self.departure_time = new_departure_time
        if new_arrival_time:
            self.arrival_time = new_arrival_time
        # This method would update the flight's schedule.

    def get_flight_status(self):
        # This method would retrieve the current status of the flight.
        pass


class Seat:
    def __init__(self, seat_number, class_type, is_occupied=False):
        self.seat_number = seat_number
        self.class_type = class_type
        self.is_occupied = is_occupied

    def assign_passenger(self, passenger):
        if not self.is_occupied:
            self.is_occupied = True
            # This method would link a passenger to this seat.
        else:
            # Handle the case where the seat is already occupied.
            pass

    def check_availability(self):
        # This method would return the availability status of the seat.
        pass


class BoardingPass:
    def __init__(self, passenger, flight, seat, issue_date, boarding_time, gate_number):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.issue_date = issue_date
        self.boarding_time = boarding_time
        self.gate_number = gate_number
        self.barcode = self.generate_barcode()

    def generate_barcode(self):
        # This method would generate a unique barcode for the boarding pass.
        pass

    def print_pass(self):
        # This method would handle the printing or digital display of the boarding pass.
        pass

# These classes are a starting point and would need to be expanded upon with proper error handling,
# interactions between classes, and integration with a database or other persistence layer for a full implementation.
class Passenger:
    def __init__(self, full_name, identification_number, frequent_flyer_number=None):
        self.full_name = full_name
        self.identification_number = identification_number
        self.frequent_flyer_number = frequent_flyer_number

    def update_information(self, new_name=None, new_id=None):
        if new_name:
            self.full_name = new_name
        if new_id:
            self.identification_number = new_id

class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, origin, destination, aircraft_type):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination
        self.aircraft_type = aircraft_type

class Seat:
    def __init__(self, seat_number, class_type, is_occupied=False):
        self.seat_number = seat_number
        self.class_type = class_type
        self.is_occupied = is_occupied

class BoardingPass:
    def __init__(self, passenger, flight, seat, issue_date, boarding_time, gate_number):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.issue_date = issue_date
        self.boarding_time = boarding_time
        self.gate_number = gate_number

# Create objects
passenger = Passenger(full_name="ALYA ALZAABI", identification_number="AA123456")
flight = Flight(flight_number="NA4321", departure_time="11:40", arrival_time="13:30",
                origin="CHICAGO ORD", destination="NEW YORK JFK", aircraft_type="Boeing 737")
seat = Seat(seat_number="09A", class_type="First Class")
boarding_pass = BoardingPass(passenger, flight, seat, issue_date="06 DEC 20", boarding_time="11:20", gate_number="03")

# Function to display boarding pass details
def display_boarding_pass_details(boarding_pass):
    print(f"Passenger: {boarding_pass.passenger.full_name}")
    print(f"From: {boarding_pass.flight.origin}")
    print(f"To: {boarding_pass.flight.destination}")
    print(f"Flight: {boarding_pass.flight.flight_number}")
    print(f"Date: {boarding_pass.issue_date}")
    print(f"Time: {boarding_pass.flight.departure_time}")
    print(f"Gate: {boarding_pass.gate_number}")
    print(f"Boarding till: {boarding_pass.boarding_time}")
    print(f"Seat: {boarding_pass.seat.seat_number}")
    print(f"Class: {boarding_pass.seat.class_type}")

# Call the function to display the details
display_boarding_pass_details(boarding_pass)
