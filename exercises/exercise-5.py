# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

x = input('Enter the first number of the Fibonacci sequence: ')

if int(x):
    term = 0
    y = int(x)
    print(f'term: {term} / number: {int(x)}')
    term += 1
    print(f'term: {term} / number: {y}')
    term += 1
    while term <= 50:
        z = int(x) + y
        print(f'term: {term} / number: {z}')
        if(term == 50):
            break
        term += 1
        x = y + z
        print(f'term: {term} / number: {x}')
        term += 1
        y = z + x
        print(f'term: {term} / number: {y}')
        term += 1
