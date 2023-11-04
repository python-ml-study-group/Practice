class Bill:
    price_per_unit = 8
    def __calculate_diff(self):
        self.__consumption = self.__curr_reading - self.__prev_reading

    def __init__(self):
        self.__curr_reading = 0
        self.__prev_reading = 0
        self.__consumption = 0
        self.__bill = 0
        self.__tax = 0
        self.__total_amount = 0
    
    @property
    def tax(self):
        return self.__tax
    @property
    def curr_reading(self):
        return self.__curr_reading

    @curr_reading.setter
    def curr_reading(self, val):
        if val < self.__prev_reading:
            raise ValueError("Current reading cannot be less than previous reading")
        self.__curr_reading = val
    
    @property
    def prev_reading(self):
        return self.__prev_reading

    def calculate_consumtion(self, curr_reading, prev_reading):
        self.__curr_reading = curr_reading
        self.__prev_reading = prev_reading
        self.__calculate_diff()
        self.__bill = self.__consumption * Bill.price_per_unit
        self.__tax = self.__bill * 0.12
        self.__total_amount = self.__bill + self.__tax

    def print(self):
        print(f"ACPDCL Bill ")
        print(f"------------------------------")
        print(f"Curr reading: {self.__curr_reading}")
        print(f"Prev reading: {self.__prev_reading}")
        print(f"Consumption: {self.__consumption}")
        print(f"Subtotal: {self.__bill}")
        print(f"Tax: {self.__tax}")
        print(f"Total amount: {self.__total_amount}")
        print(f"------------------------------")
        print(f"Thank you for using ACPDCL")
