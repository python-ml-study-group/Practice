def getFactors(num):
    factors = []
    remaining = num
    while remaining > 1:
        for i in range(2, num):
            print (f"i: {i}, remaining: {remaining}, factors: {factors}")
            if remaining % i == 0:
                factors.append(i)
                remaining = remaining / i
                break

    return factors

a = getFactors(100)
print   (a)



