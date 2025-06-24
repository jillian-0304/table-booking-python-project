
class Table: 
    def __init__(self, table_id, capacity, is_reserved=False): 
        self.table_id = table_id
        self.capacity = capacity
        self.is_reserved = is_reserved
        self.reservation_time = None 

    def get_table_id(self): 
        return self.table_id
    
    def get_capacity(self):
        return self.capacity 

    def get_is_reserved(self): 
        return self.is_reserved 

if __name__ == "__main__": 
    pass 
    # write your own tests here in order to debug.  