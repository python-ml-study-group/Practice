# Generate the bill, pay the bill, 

# Questions
# For each bill, we need to know:
# 1. Consumption is calcualted as curr reading - prev reading, is it right?
# 2. What is the price of 1 unit? 8 Rs. 
# 3. What is the tax rate? 12%

price_per_unit = 8
def calculate_consumtion(curr_reading, prev_reading):
    return curr_reading - prev_reading

def calculate_bill(curr_reading, prev_reading):
    consumption = calculate_consumtion(curr_reading, prev_reading)
    bill = consumption * price_per_unit
    tax = bill * 0.12
    total_amount = bill + tax
    bill_info = {"prev_reading": prev_reading, "curr_reading": curr_reading, "consumption": consumption, "bill": bill, "tax": tax, "total_amount": total_amount}
    return bill_info

def print_bill(bill_info):
    print(f"ACPDCL Bill ")
    print(f"------------------------------")
    print(f"Customer name: Mahesh ")
    print(f"------------------------------")
    print(f"Curr reading: {bill_info['curr_reading']}")
    print(f"Prev reading: {bill_info['prev_reading']}")
    print(f"Consumption: {bill_info['consumption']}")
    print(f"Subtotal: {bill_info['bill']}")
    print(f"Tax: {bill_info['tax']}")
    print(f"Total amount: {bill_info['total_amount']}")
    print(f"------------------------------")
    print(f"Thank you for using ACPDCL")

if __name__ == "__main__":
    curr_reading = int(input("Enter current reading: "))
    prev_reading = int(input("Enter previous reading: "))
    bill_info = calculate_bill(curr_reading, prev_reading)
    print_bill(bill_info)
