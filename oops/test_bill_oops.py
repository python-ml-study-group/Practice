from bill_oops import Bill
b = Bill()
b.calculate_consumtion(2030, 1900)
b.print()
b.curr_reading = 2000
print ("Tax: ", b.tax)
print ("Curr reading: ", b.curr_reading)
print ("Prev reading: ", b.prev_reading)

