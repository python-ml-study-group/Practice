import json
customer_data = [
    {"customer_name": "Sirisha", "invested_amount": 200000},
    {"customer_name": "Nikhitha", "invested_amount": 300000}
]

class invoice:
    def __init__(self,customer_name, invested_amount, returns_percentage, total_fee=0, slab1=0, fee1=0, slab2=0, fee2=0, slab3=0, fee3=0):
        self.customer_name=customer_name
        self.invested_amount=invested_amount
        self.returns_percentage=returns_percentage
        self.total_fee=total_fee
        self.slab1=slab1
        self.fee1=fee1
        self.slab2=slab2
        self.fee2=fee2
        self.slab3=slab3
        self.fee3=fee3





def calculate_invoice_amount(inv:invoice):
    inv.slab1 = min(inv.returns_percentage, 10)

    inv.slab2 = max(0, min(inv.returns_percentage, 20) - 10)
    inv.slab3 = max(0, min(inv.returns_percentage, 30) - 20)

    inv.fee1 = inv.slab1 * 0.0027 * inv.invested_amount
    inv.fee2 = inv.slab2 * 0.0036 * inv.invested_amount
    inv.fee3 = inv.slab3 * 0.0045 * inv.invested_amount
    

    inv.total_fee = inv.fee1 + inv.fee2 + inv.fee3
    

def display_invoice_details(inv:invoice):
    print("\nInvoice Details")
    print(f"Customer Name: {customer_name}")
    print(f"Invested Amount: {invested_amount}")
    print(f"Returns Percentage: {returns_percentage}")
    print("\nInvoice Breakdown:")
    print(f"* Slab 1: Fee for the first 10% returns - {inv.slab1}%: {inv.fee1}")
    print(f"* Slab 2: Fee for the amount between > 10% and <= 20% returns - {inv.slab2}%: {inv.fee2}")
    print(f"* Slab 3: Fee for the amount between > 20% and <= 30% returns - {inv.slab3}%: {inv.fee3}")
    print(f"\n Total Invoice Amount: {inv.total_fee}")


customer_name = input("Enter customer name: ")
returns_percentage = float(input("Enter returns percentage: "))


invested_amount = next((customer["invested_amount"] for customer in customer_data if customer["customer_name"] == customer_name), None)
inv=invoice(customer_name,invested_amount,returns_percentage)



if invested_amount is not None:
    
    calculate_invoice_amount(inv)
    display_invoice_details(inv)
else:
    print("Customer not found.")

display_invoice_details(inv)
