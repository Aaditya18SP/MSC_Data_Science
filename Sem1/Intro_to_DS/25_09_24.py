num = input("Whats the number: ")


# factorial
def fact(x):
    if x == 0 or x == 1:
        return 1
    return x * fact(x-1)


# sum of digits
def sumDigits(x):
    add = 0
    for n in x:
        add += int(n)
    return add


print("factorial is:", fact(int(num)))

# reverse a number
rev_num = [n for n in reversed(num)]

print("reversed number is: ", "".join(rev_num))


# count the number of digits
print("Number of digits in the number: ", len(num))

# sum of digits
print("sum of digits is: ", sumDigits(num))
