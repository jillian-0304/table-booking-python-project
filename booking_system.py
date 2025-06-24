from customer import Customer 
from reservation import Reservation
from table import Table
import time 
from collections import deque 

class BookingSystem: 
    def __init__(self, tables, reservation_duration = 60*60): 
        self.tables = tables 
        self.reservations = []  # stores the current reservations 
        self.waitlist = deque()
        self.reservation_duration = reservation_duration

    def max_table_size(self): 
        return max([table.capacity for table in self.tables])

    def find_available_table(self, party_size):
        if party_size > self.max_table_size():
            raise Exception("Party size is too big to be seated.")
        
        for table in self.tables:
            if table.get_capacity() >= party_size and not table.get_is_reserved():
                return table
        return None

    def book_table(self, customer):
        potential_table = self.find_available_table(customer.party_size)
        timestamp = time.time()

        if potential_table is not None:
            potential_table.is_reserved = True
            potential_table.reservation_time = timestamp
            res = Reservation(customer, potential_table)
            self.reservations.append(res)
            return res
        else:
            self.add_to_waitlist(customer)
            return None

    def add_to_waitlist(self, customer):
        timestamp = time.time()
        self.waitlist.append((customer, timestamp))

        #customers_before = len(self.waitlist) - 1
        #estimated_wait_time = customers_before * self.reservation_duration
        return None

    def clear_table(self, table_id):
        for table in self.tables:
            if table.get_table_id() == table_id:
                if not table.get_is_reserved():
                    return False
                table.is_reserved = False
                table.reservation_time = None
                for res in self.reservations:
                    if res.get_table() == table:
                        self.reservations.remove(res)
                        return True
        return False

    def seat_from_waitlist(self):
        """
        EXTRA CREDIT EXERCISE 

        Attempts to seat the first customer on the waitlist if a suitable table becomes available.

        This method checks the front of the waitlist and tries to find a table that can accommodate
        the customer's party size. If a table is available, the customer is removed from the waitlist,
        the table is marked as reserved, and a reservation is created.

        Returns:
            Reservation or None:
                - A Reservation object if the customer was successfully seated.
                - None if no suitable table is available or the waitlist is empty.
        """
        #need to get customer information (party_size) from customer in waitlist
        #use that info in find_available_table method
        #then use book_table method, but rewrite so can't call book_table

        # self.waitlist.popleft() is customer
        #i need customer.get_party_size

        if len(self.waitlist) == 0:
            return None

        customer, _ = self.waitlist.popleft()
        #self.find_available_table(customer.get_party_size())

        if customer.get_party_size() > self.max_table_size():
            return None

        potential_table = self.find_available_table(customer.party_size)
        timestamp = time.time()

        if potential_table is not None:
            potential_table.is_reserved = True
            potential_table.reservation_time = timestamp
            res = Reservation(customer, potential_table)
            self.reservations.append(res)
            return res
        else:
            return None



    def get_table_status(self):
        table_status = []
        for table in self.tables:
            status = {"table": table}
            if table.is_reserved:
                remaining_time = self.reservation_duration - (time.time() - table.reservation_time)
                status["remaining_time"] = max(0, int(remaining_time))
            table_status.append(status)
        return table_status

    def get_waitlist(self):
        if self.waitlist:
            for item, time_val in self.waitlist: 
                print(f"Name: {item.name}, Party Size: {item.party_size}, Booked at: {(time.time() - time_val):.2f} seconds ago.") 
        else: 
            print("There is no one in the waitlist.")

            
if __name__ == "__main__": 
    pass 
    # write your own tests here in order to debug. 


'''
class BookingSystem: 
    def __init__(self, tables, reservation_duration = 60*60): 
        self.tables = tables 
        self.reservations = []  # stores the current reservations 
        self.waitlist = deque()
        self.reservation_duration = reservation_duration

    def max_table_size(self): 
        """
        PLEASE DO NOT MODIFY THIS METHOD. 
        You can use this method to find the maximum capacity of any table in the `tables` attribute.
        Returns: 
            max capacity (int): The maximum capacity among all the tables available.
        """
        return max([table.capacity for table in self.tables])

    def find_available_table(self, party_size):
        """
        Finds an available table that can accommodate the given party size.

        This method checks if the requested party size exceeds the capacity of any table in the restaurant.
        If it does, an exception is raised. Otherwise, it searches for the first available (unreserved) table
        that has a capacity equal to or greater than the party size.

        Args:
            party_size (int): The number of people in the customer's party.

        Returns:
            Table or None: A suitable available table if found; otherwise, None.

        Raises:
            Exception: If the party size exceeds the maximum table capacity in the restaurant. 
            Error Message: "Party size is too big to be seated."
        """
        pass 
        ###################################
        ####### write your code here. #####
        ###################################

        if party_size > self.max_table_size():
            raise Exception("Party size is too big to be seated.")
        
        for table in self.tables:
            if table.get_capacity() >= party_size and not table.get_is_reserved():
                return table
        return None

    def book_table(self, customer):
        """
        Attempts to book a table for a customer or adds them to the waitlist if no table is available.

        This method searches for an available table that can accommodate the customer's party size.
        If a suitable table is found, it is marked as reserved, and a reservation is created and stored.
        If no table is available, the customer is added to the waitlist.

        Args:
            customer (Customer): The customer requesting the reservation.

        Returns:
            Reservation or None:
                - A Reservation object if a table was successfully booked.
                - None if added to the waitlist.
        """
        pass 
        ###################################
        ####### write your code here. #####
        ###################################

        potential_table = self.find_available_table(customer.party_size)
        #timestamp = time.time()

        if potential_table is not None:
            potential_table.is_reserved = True
            potential_table.reservation_time = time.time()
            res = Reservation(customer, potential_table)
            self.reservations.append(res)
            return res
        else:
            self.add_to_waitlist(customer)
            return None

    def add_to_waitlist(self, customer):
        """
        Adds a customer to the waitlist and estimates their wait time.

        This method appends the customer to the end of the waitlist along with the
        current timestamp. It then calculates the estimated wait time based on the
        number of customers ahead in the queue and the average wait time per customer.

        Note: time.time() is a common way to get the current timestamp. 

        Args:
            customer (Customer): The customer to be added to the waitlist.

        Returns:
            None
        """
        pass 
        ###################################
        ####### write your code here. #####
        ###################################

        timestamp = time.time()
        self.waitlist.append((customer, timestamp))

        customers_before = len(self.waitlist) - 1
        estimated_wait_time = customers_before * self.reservation_duration
        return None

    def clear_table(self, table_id):
        """
        Clears the reservation for a specific table by its ID.

        This method sets the table's `is_reserved` flag to False and removes
        any associated reservation time. It is typically used when a party leaves
        the table and it becomes available for new reservations.

        Note: This method must also updated self.reservations attribute as well.

        Args:
            table_id (int): The ID of the table to clear.

        Returns:
            bool: True if the table was found and cleared, False otherwise.
        """
        pass 
        ###################################
        ####### write your code here. #####
        ###################################

        for table in self.tables:
            if table.get_table_id() == table_id:
                if not table.get_is_reserved():
                    return False
                table.is_reserved = False
                table.reservation_time = None
                for res in self.reservations:
                    if res.get_table() == table:
                        self.reservations.remove(res)
                        return True
        return False

    def seat_from_waitlist(self):
        """
        EXTRA CREDIT EXERCISE 

        Attempts to seat the first customer on the waitlist if a suitable table becomes available.

        This method checks the front of the waitlist and tries to find a table that can accommodate
        the customer's party size. If a table is available, the customer is removed from the waitlist,
        the table is marked as reserved, and a reservation is created.

        Returns:
            Reservation or None:
                - A Reservation object if the customer was successfully seated.
                - None if no suitable table is available or the waitlist is empty.
        """
        pass 
        ###################################
        ####### write your code here. #####
        ###################################


    def get_table_status(self):
        """
        PLEASE DO NOT MODIFY THIS METHOD.
        Retrieves the current status of all tables in the restaurant.

        For each table, this method returns whether it is reserved and, if so,
        how much time is remaining for the current reservation. It calculates the
        remaining time based on the reservation start time and a predefined reservation duration.

        Returns:
            list: A list of dictionaries, each containing:
                - 'table' (Table): The table object.
                - 'remaining_time' (int, optional): The number of seconds remaining
                on the reservation, only included if the table is reserved.
        """
        table_status = []
        for table in self.tables:
            status = {"table": table}
            if table.is_reserved:
                remaining_time = self.reservation_duration - (time.time() - table.reservation_time)
                status["remaining_time"] = max(0, int(remaining_time))
            table_status.append(status)
        return table_status

    def get_waitlist(self):
        """
        PLEASE DO NOT MODIFY THIS METHOD.
        """
        if self.waitlist:
            for item, time_val in self.waitlist: 
                print(f"Name: {item.name}, Party Size: {item.party_size}, Booked at: {(time.time() - time_val):.2f} seconds ago.") 
        else: 
            print("There is no one in the waitlist.")
'''
'''          
if __name__ == "__main__": 
    pass 
    # write your own tests here in order to debug. 
'''