import os
import time
from enum import Enum

class PaymentMethod(Enum):
    CREDIT_CARD = 1
    PAYPAL = 2
    CASH = 3
class Flight:
    def __init__(self, flight_number, departure, arrival, departure_time, arrival_time, seats, company_name):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = seats
        self.company_name = company_name

    def __str__(self):
        return f'Flight Number: {self.flight_number}\nDeparture: {self.departure}\nArrival: {self.arrival}\nDeparture Time: {self.departure_time}\nArrival Time: {self.arrival_time}\nSeat Available: {self.seats}\nCompany Name: {self.company_name}'
class FlightSystem:
    def __init__(self):
        if os.path.exists("flights.txt"):
            with open("flights.txt", "r") as f:
                self.flight_list = [Flight(*line.strip().split(',')[:7]) for line in f]
        else:
            self.flight_list = []

    def add_flight(self, flight):
        self.flight_list.append(flight)
        self.save_file()

    def search_flight(self, departure, arrival):
        found_flights = []
        for flight in self.flight_list:
            if flight.departure == departure and flight.arrival == arrival:
                found_flights.append(flight)

        return found_flights

    def buy_ticket(self, flight_number, count):
        for flight in self.flight_list:
            if flight.flight_number == flight_number:
                if int(flight.seats)>=count:
                    print("Select payment method : ")
                    for payment_method in PaymentMethod:
                        print(payment_method.value, payment_method.name)

                    selected_payment_method = int(input("--->"))
                    if selected_payment_method == PaymentMethod.CREDIT_CARD.value:
                        card_number = input("Enter your 16 digit card number : ")
                        card_password = input("Enter your 4 digit card password  : ")
                        if len(card_number) >= 15 and len(card_password) == 4:
                            print("Payment is progress, please wait...")
                            time.sleep(1.5)
                            print("Credit card payment processed.")

                        else:
                            print("Invalid card number...")
                    elif selected_payment_method == PaymentMethod.PAYPAL.value:
                        paypal_card_number = input("Enter your 16 digit card number : ")
                        paypal_card_password = input("Enter your 4 digit card password  : ")
                        if len(paypal_card_number) >= 15 and len(paypal_card_password) == 4:
                            print("Payment is progress, please wait...")
                            time.sleep(1.5)
                            print("Paypal payment processed.")
                        else:
                            print("Invalid card number...")
                    elif selected_payment_method == PaymentMethod.CASH.value:
                        print("Cash payment processed.")
                    else:
                        print("Invalid payment method.")
                    flight.seats = str(int(flight.seats)-count)
                    self.save_file()
                    return f"{count} Tickets purchase succesful"
                else:
                    return "Seat not available"
        return "Invalid flight number"

    def save_file(self):
        with open("flights.txt", "w") as f:
            for flight in self.flight_list:
                f.write(f"{flight.flight_number},{flight.departure},{flight.arrival},{flight.departure_time},{flight.arrival_time},{flight.seats},{flight.company_name}\n")

    def check_admin_credentials(self,username, password):
        if username == "admin" and password == "1234":
            print("Logging into account, please wait...")
            time.sleep(1.5)
            print("Login to the system.")
            return True
        elif username == "airport" and password == "0000":
            print("Logging into account, please wait...")
            time.sleep(1.5)
            print("Login to the system.")
            return True
        elif username == "q" or username == "Q" or password == "Q" or password =="q":
            print("The system has been logged out.")
            quit()
        else:
            print("Wrong username or password...")
            return False
    def menu(self):
        while True:
            print("Welcome to airport system. We wish you a nice day..")
            username = input("Please enter username :")
            password = input("Please enter password : ")
            if self.check_admin_credentials(username, password):
                while True:
                    print("1. Add Flight")
                    print("2. Search Flight")
                    print("3. Buy Ticket")
                    print("4. Exit")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        flight_number = input("Enter flight number : ")
                        departure = input("Enter departure city : ")
                        arrival = input("Enter arrival city : ")
                        departure_time = input("Enter departure time : ")
                        arrival_time = input("Enter arrival time : ")
                        seats = int(input("Enter number of seats : "))
                        company_name = input("Enter a company name : ")

                        flight = Flight( flight_number, departure, arrival, departure_time, arrival_time, seats, company_name)
                        self.add_flight(flight)
                        print("The flight is added to the system. Please wait....")
                        time.sleep(1.5)
                        print("Flight added successfully!")
                    elif choice == '2':
                        departure = input("Enter departure city: ")
                        arrival = input("Enter arrival city: ")
                        flights = self.search_flight(departure, arrival)
                        if flights:
                            print("Listing all flights from {} to {}, Please wait...".format(departure,arrival))
                            time.sleep(1.5)
                            for flight in flights:
                                print("\n*****\n",flight,"\n*****")
                        else:
                            print("No flights found.")
                    elif choice == '3':
                        flight_number = input("Enter flight number: ")
                        count = int(input("Enter number of tickets: "))
                        print(self.buy_ticket(flight_number, count))
                    elif choice == '4':
                        print("BYE BYE :))")
                        break
                    else:
                        print("Invalid choice. Try again.")


system = FlightSystem()
system.menu()

