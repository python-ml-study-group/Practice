# Given the Opening balance and the list of transactions
# Find out the closing balance for each transaction
# ex. OB: 1000, transactions: 
# -100, +500, + 200, - 1000, +300, -1000
# 900, 1400, 1600, 600, 900, -100
from itertools import accumulate

def apply_tran(bal, tran):
    if bal + tran < 0:
        return bal
    else:
        return bal + tran

opening_balance = 1000
transactions = [-100, 500, 200, -1000, 300, -1000]
# add the opening balance to the list of transactions
transactions.insert(0, opening_balance)
# use the accumulate function
print(list(accumulate(transactions, apply_tran)))

# In the last transaction apply_tran did not execute, 
# it just bounced off the transaction as it resulted in negative balance


