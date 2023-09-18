def classify_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    total = sum(divisors)
    if total < n:
        classification = "deficient"
    elif total == n:
        classification = "perfect"
    else:
        classification = "abundant"
    
    return classification

def count_numbers(lower, upper):
    deficient_count = 0
    perfect_count = 0
    abundant_count = 0

    for num in range(lower, upper + 1):
        classification = classify_number(num)
        if classification == "deficient":
            deficient_count += 1
        elif classification == "perfect":
            perfect_count += 1
        else:
            abundant_count += 1

    return deficient_count, perfect_count, abundant_count

upper_bound = int(input("Enter an upper bound for a check: "))

deficient, perfect, abundant = count_numbers(1, upper_bound)

print(f"Between 1 and {upper_bound} there are")
print(f"{deficient} deficient numbers")
print(f"{perfect} perfect numbers")
print(f"{abundant} abundant numbers")
