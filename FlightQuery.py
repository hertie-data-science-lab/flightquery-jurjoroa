'''
Submitted on 10th April 2023
@authors: Jorge Roa and Carmen Garro


Objective: Create a flight query system for searching available flights.

Purpose: Allow users to search for flights based on their origin, destination, departure date, and preferred time window.

Functions:

    FlightQuery class: A custom SortedTableMap implementation that handles flight data storage and retrieval. It includes the following methods:

        Key class: A nested class used to create keys for the SortedTableMap. Keys are composed of origin, destination, departure date, and departure time. This class also provides comparison methods and a string representation of the key.

        query method: Takes two Key objects, k1 and k2, and returns a list of flights that fall within the specified range.

    get_user_input: A function that prompts the user for input, such as origin, destination, departure date, and preferred time window. Returns a tuple containing the user's input.

The main section of the code initializes a FlightQuery object, stores sample flight data, and provides a user interface for querying flights based on the user's input. The results are then printed on the screen, and the user can continue searching for more flights or exit the program.
'''



from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''

    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        #Initialize the Key with origin, destination, date, and time

        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        #Less-than comparison for sorting purposes
        def __lt__(self, other):
            return (self._origin, self._dest, self._date, self._time) < (other._origin, other._dest, other._date, other._time)
        #Less-than or equal-to comparison for sorting purposes
        def __le__(self, other):
            return (self._origin, self._dest, self._date, self._time) <= (other._origin, other._dest, other._date, other._time)
        #String representation of the Key
        def __str__(self):
            return f"{self._origin} -> {self._dest} ({self._date}/{self._time})"
    #Define the query method to find flights within the specified range    
    def query(self, k1, k2):
        results = []
        for key, value in self:
            if k1 <= key < k2:
                results.append(f"{str(key)} - Flight {value}")
        return results

#Main function to test the FlightQuery class

if __name__ == "__main__":

    #Instantiate the FlightQuery class
    a = FlightQuery()

    #Sample flight data
    s = [
        ("A", "B", 622, 1200, "No1"),
        ("A", "B", 622, 1230, "No2"),
        ("A", "B", 622, 1300, "No3"),
        ("A", "C", 623, 1100, "No4"),
        ("A", "C", 623, 1400, "No5"),
        ("A", "D", 624, 1700, "No6"),
        ("B", "C", 625, 1900, "No7"),
    ]
    #Store the sample flight data in the FlightQuery object
    for each in s:
        key = a.Key(each[0], each[1], each[2], each[3])
        value = each[4]
        a[key] = value
    #Display the number of flights stored
    print("Total flights stored:", len(a))

    
    #Example queries
    print("\nFlights from A to B between 622 1200 and 622 1300:")
    k1 = a.Key("A", "B", 622, 1200)
    k2 = a.Key("A", "B", 622, 1300)
    results = a.query(k1, k2)
    for r in results:
        print(r)

    print("\nFlights from A to C between 623 1000 and 623 1500:")
    k1 = a.Key("A", "C", 623, 1000)
    k2 = a.Key("A", "C", 623, 1500)
    results = a.query(k1, k2)
    for r in results:
        print(r)

    print("\nAll flights from A to D:")
    k1 = a.Key("A", "D", 0, 0)
    k2 = a.Key("A", "D", float('inf'), float('inf'))
    results = a.query(k1, k2)
    for r in results:
        print(r)



# Example of user interface


def get_user_input():
    origin = input("Enter the origin: ")
    dest = input("Enter the destination: ")
    date = int(input("Enter the date (format: MMDD): "))
    start_time = int(input("Enter the start time (format: HHMM): "))
    end_time = int(input("Enter the end time (format: HHMM): "))

    return origin, dest, date, start_time, end_time

if __name__ == "__main__":
    a = FlightQuery()

    # Store flight data
    s = [
        ("A", "B", 622, 1200, "Flight 1"),
        ("A", "B", 622, 1230, "Flight 2"),
        ("A", "B", 622, 1300, "Flight 3"),
        ("A", "C", 623, 1100, "Flight 4"),
        ("A", "C", 623, 1400, "Flight 5"),
        ("A", "D", 624, 1700, "Flight 6"),
        ("B", "C", 625, 1900, "Flight 7"),
    ]

    for each in s:
        key = a.Key(each[0], each[1], each[2], each[3])
        value = each[4]
        a[key] = value

    print("Welcome to the Flight Query System!\n")
    print("Available flights:")
    for flight in s:
        print(f"{flight[4]}: {flight[0]} -> {flight[1]} ({flight[2]}/{flight[3]})")

    while True:
        print("\nEnter your query details:")
        origin, dest, date, start_time, end_time = get_user_input()
        k1 = a.Key(origin, dest, date, start_time)
        k2 = a.Key(origin, dest, date, end_time)
        results = a.query(k1, k2)

        if results:
            print("\nFlights found:")
            for r in results:
                print(r)
        else:
            print("\nNo flights found for the specified criteria.")

        continue_query = input("\nDo you want to search for more flights? (yes/no): ")
        if continue_query.lower() != "yes":
            break

    print("\nThank you for using the Flight Query System!")
