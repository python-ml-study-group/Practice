import json
customer_data = [
    {"customer_name": "Sirisha", "invested_amount": 200000},
    {"customer_name": "Nikhitha", "invested_amount": 300000}
]




def calculate_invoice_amount(invested_amount, returns_percentage):
    slab1 = min(returns_percentage, 10)

    slab2 = max(0, min(returns_percentage, 20) - 10)
    slab3 = max(0, min(returns_percentage, 30) - 20)

    fee1 = slab1 * 0.0027 * invested_amount
    fee2 = slab2 * 0.0036 * invested_amount
    fee3 = slab3 * 0.0045 * invested_amount
    

    total_fee = fee1 + fee2 + fee3
    return total_fee, slab1, fee1, slab2, fee2, slab3, fee3


def display_invoice_details(customer_name, invested_amount, returns_percentage, total_fee, slab1, fee1, slab2, fee2, slab3, fee3):
    print("\nInvoice Details")
    print(f"Customer Name: {customer_name}")
    print(f"Invested Amount: {invested_amount}")
    print(f"Returns Percentage: {returns_percentage}")
    print("\nInvoice Breakdown:")
    print(f"* Slab 1: Fee for the first 10% returns - {slab1}%: {fee1}")
    print(f"* Slab 2: Fee for the amount between > 10% and <= 20% returns - {slab2}%: {fee2}")
    print(f"* Slab 3: Fee for the amount between > 20% and <= 30% returns - {slab3}%: {fee3}")
    print(f"\n Total Invoice Amount: {total_fee}")


customer_name = input("Enter customer name: ")
returns_percentage = float(input("Enter returns percentage: "))


invested_amount = next((customer["invested_amount"] for customer in customer_data if customer["customer_name"] == customer_name), None)


if invested_amount is not None:
    
    total_fee, slab1, fee1, slab2, fee2, slab3, fee3 = calculate_invoice_amount(invested_amount, returns_percentage)
    display_invoice_details(customer_name, invested_amount, returns_percentage, total_fee, slab1, fee1, slab2, fee2, slab3, fee3)
else:
    print("Customer not found.")