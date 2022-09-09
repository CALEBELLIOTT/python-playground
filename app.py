

def fibonacci(limit):
    previous1 = 1
    previous2 = 2
    evenTotal = 2
    while previous1 < limit and previous2 < limit:
        current = previous1 + previous2
        if current % 2 == 0 and current < limit:
            evenTotal += current
        previous1 = previous2
        previous2 = current

    return evenTotal


print(fibonacci(400000))
