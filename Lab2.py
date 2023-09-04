def calculate_horse_age(human_age):
    horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)
    return horse_age
def calculate_dog_age(human_age):
    dog_age = human_age * 7
    return dog_age
def calculate_cat_age(human_age):
	cat_age = human_age / 9
	return cat_age

def convert_to_years_months_days(dog_age):
    years = int(dog_age)
    remaining_months = (dog_age - years) * 12
    months = int(remaining_months)
    remaining_days = (remaining_months - months) * 30
    days = int(remaining_days)
    return years, months, days

human_age = float(input("Enter your age:"))

dog_age = calculate_dog_age(human_age)
cat_age = calculate_cat_age(human_age)
horse_age = calculate_horse_age(human_age)

dog_years, dog_months, dog_days = convert_to_years_months_days(dog_age)
cat_years, cat_months, cat_days = convert_to_years_months_days(cat_age)
horse_years, horse_months, horse_days = convert_to_years_months_days(horse_age)

print(f"Your age in dog years is: {dog_years} years, {dog_months} months, {dog_days} days")
print(f"Your age in dog years is: {cat_years} years, {cat_months} months, {cat_days} days")
print(f"Your age in horse years is: {horse_years} years, {horse_months} months, {horse_days} days")
