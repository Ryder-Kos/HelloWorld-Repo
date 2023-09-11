earned_income = float(input("Enter earned income: "))
marital_status = input("Are you married or single? (S or M): ")

brackets = [
    (0, 11000, 0.10),
    (11001, 44725, 0.12),
    (44726, 95375, 0.22)
]

if earned_income > 190750 and marital_status == "M":
    print("You entered too much for this to work properly.")
else:
    tax_rate = None
    for bracket in brackets:
        if bracket[0] <= earned_income <= bracket[1]:
            tax_rate = bracket[2]
            break
    
    if tax_rate is not None:
        tax_owed = earned_income * tax_rate
        print(f"The tax owed for the year 2023 is: ${tax_owed:.2f}")
    else:
        print("Invalid input")
