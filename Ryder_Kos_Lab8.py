"""
Ryder Kos 
10/16/23
Lab 8
Functions and List review
"""




#Problem 1
'''
def calc_toll(hour, is_morning, is_weekend):
    if is_weekend:
        if hour < 7:
            return 1.05
        elif hour < 20:
            return 2.15
        else:
            return 1.10
    else:
        if hour < 7:
            return 1.15
        elif hour < 10:
            return 2.95 if is_morning else 1.90
        elif hour < 15:
            return 1.90
        elif hour < 20:
            return 3.95
        else:
            return 1.40
current_hour = int(input("Current Hour? "))
is_morning = input("Is it morning? ").lower() == "yes"
is_weekend = input("Is it a weekend? ").lower() == "yes"


toll_fee = calc_toll(current_hour, is_morning, is_weekend)
print(f"The toll fee is ${toll_fee:.2f}")
'''
	




#Problem 2
'''
def LCM(num1, num2):
    greater = max(num1, num2)

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            return greater
        greater += 1
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

result = LCM(num1, num2)

print(f"The LCM of {num1} and {num2} is: {result}")
'''



		
"""
#Problem 3

def combination(m, k):
    return factorial(m) // (factorial(k) * factorial(m - k))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [combination(i, j) for j in range(i+1)]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(len(triangle[-1]) * 3))

#Example:
n = 10
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)


"""


if __name__ == '__main__':
	#print(calc_toll(8, True, False))  #answer 2.95
	#print(calc_toll(1, False, False)) #answer 1.9
	#print(calc_toll(3, False, True))  #answer 2.15
	#print(calc_toll(5, True, True))   #answer 1.05


	""" Uncomment this when working on Problem 2
	
	if LCM(10,25) == 50:
		print("LCM(10,25) is correct")
	else:
		print(f"LCM(10,25) is incorrect.  You got {LCM(10,25)}, but the correct answer should be 50.")
	if LCM(90,342) == 1710:
		print("LCM(90,342) is correct")
	else:
		print(f"LCM(90,342) is incorrect. You got {LCM(90,342)}, but the correct answer should be 1710.")
	if LCM(45,240) == 720:
		print("LCM(45,240) is correct")
	else:
		print(f"LCM(45,240) is incorrect.  You got {LCM(45,240)}, but the correct answer should be 720.")
	"""


	""" Uncomment this when working on Problem 3
	
	for i in range(10):
		for j in range(i+1):
			print(int(combination(i,j)), end=' ')
		print()
	"""	






