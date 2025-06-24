import time 

class Reservation:
    def __init__(self, customer, table): 
        self.customer = customer
        self.table = table
        self.timestamp = None
    
    def get_customer(self):
        return self.customer

    def get_table(self):
        return self.table 

    def __str__(self):
        return f"Reservation for {self.get_customer()} at {self.get_table()}"

if __name__ == "__main__": 
    pass 
    # write your own tests here in order to debug.  