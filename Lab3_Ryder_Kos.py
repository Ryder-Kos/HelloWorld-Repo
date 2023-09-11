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
    if marital_status == "S":
        if earned_income <= 11000:
            tax_rate = 0.10
        elif 11001 <= earned_income <= 44725:
            tax_rate = 0.12
        elif 44726 <= earned_income <= 95375:
            tax_rate = 0.22
    elif marital_status == "M":
        if earned_income <= 22000:
            tax_rate = 0.10
        elif 22001 <= earned_income <= 89450:
            tax_rate = 0.12
        elif 89451 <= earned_income <= 190750:
            tax_rate = 0.22
    
    if tax_rate is not None:
        tax_owed = earned_income * tax_rate
        print(f"The tax owed for the year 2023 is: ${tax_owed:.2f}")
    else:
        print("Invalid input")
