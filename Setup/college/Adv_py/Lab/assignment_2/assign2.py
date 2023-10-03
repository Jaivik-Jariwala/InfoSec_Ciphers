import csv

class Train:
    def __init__(self, train_id, train_name, source_station, dest_station, total_seats, fare_per_seat):
        self.train_id = train_id
        self.train_name = train_name
        self.source_station = source_station
        self.dest_station = dest_station
        self.total_seats = total_seats
        self.fare_per_seat = fare_per_seat
        self.available_seats = total_seats

class Passenger:
    def __init__(self, name, train_id, num_tickets):
        self.name = name
        self.train_id = train_id
        self.num_tickets = num_tickets

def load_trains(filename):
    trains = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            train_id, train_name, source, dest, total_seats, fare_per_seat = row
            train = Train(train_id, train_name, source, dest, int(total_seats), float(fare_per_seat))
            trains.append(train)
    return trains

def load_passengers(filename):
    passengers = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, train_id, num_tickets = row
            passenger = Passenger(name, train_id, int(num_tickets))
            passengers.append(passenger)
    return passengers

def check_seat_availability(train, num_tickets):
    return train.available_seats >= num_tickets

def update_seat_availability(train, num_tickets):
    train.available_seats -= num_tickets

def generate_reports(trains, passengers):
    print("Report 1: Train Details")
    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format("Train ID", "Train Name", "Source", "Destination", "Available Seats"))
    for train in trains:
        print("{:<10} {:<15} {:<15} {:<15} {:<10}".format(
            train.train_id, train.train_name, train.source_station, train.dest_station, train.available_seats))
    
    print("\nReport 2: Revenue Report")
    print("{:<15} {:<15} {:<10} {:<10}".format("Train ID", "Train Name", "Total Bookings", "Total Revenue"))
    for train in trains:
        total_bookings = train.total_seats - train.available_seats
        total_revenue = total_bookings * train.fare_per_seat
        print("{:<15} {:<15} {:<10} {:<10}".format(train.train_id, train.train_name, total_bookings, total_revenue))

def main():
    trains = load_trains("trains.csv")
    passengers = load_passengers("passengers.csv")
    
    for passenger in passengers:
        found_train = None
        for train in trains:
            if train.train_id == passenger.train_id:
                found_train = train
                break
        
        if found_train:
            if check_seat_availability(found_train, passenger.num_tickets):
                update_seat_availability(found_train, passenger.num_tickets)
                total_fare = passenger.num_tickets * found_train.fare_per_seat
                print(f"Booking confirmed for {passenger.name} on {found_train.train_name}. Total Fare: {total_fare}")
            else:
                print(f"Sorry, no seats available for {passenger.name} on {found_train.train_name}.")
        else:
            print(f"Invalid train ID for {passenger.name}.")
    
    generate_reports(trains, passengers)

if __name__ == "__main__":
    main()
