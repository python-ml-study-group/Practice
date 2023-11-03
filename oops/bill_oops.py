class Bill:
    price_per_unit = 8
    def __calculate_diff(self):
        self.consumption = self.curr_reading - self.prev_reading
    def calculate_consumtion(self, curr_reading, prev_reading):
 
        self.curr_reading = curr_reading
        self.prev_reading = prev_reading
        self.__calculate_diff()
        self.bill = self.consumption * Bill.price_per_unit
        self.tax = self.bill * 0.12
        self.total_amount = self.bill + self.tax

    def print(self):
        print(f"ACPDCL Bill ")
        print(f"------------------------------")
        print(f"Curr reading: {self.curr_reading}")
        print(f"Prev reading: {self.prev_reading}")
        print(f"Consumption: {self.consumption}")
        print(f"Subtotal: {self.bill}")
        print(f"Tax: {self.tax}")
        print(f"Total amount: {self.total_amount}")
        print(f"------------------------------")
        print(f"Thank you for using ACPDCL")
