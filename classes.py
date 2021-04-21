class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger (self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats (self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ['Harry', 'Ron', 'Hermions', 'Draco']
for person in people:
    sucsses = flight.add_passenger(person)
    if sucsses:
        print(f'Added {person} to the flight')
    else:
        print(f'Sorry, no available seats for {person}')