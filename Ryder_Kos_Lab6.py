"""
Ryder Kos
10/2/2023

Lab 6 - Lists
"""









"""
# Problem 1
# Arithmetic with corresponding elements of mutiple lists.
# here are several test cases.  Uncomment them one at a time to ensure your code works.

	#Test1 - correct answer = 8
#list1, list2, list3 = [1,2,3], [4,5,6], [7,8,9]
	#Test 2 - correct answer = 21
#list1, list2, list3 = [5,-2,4], [3,12,9], [8,4,-6]
	#Test 3 - correct answer = 0
#list1, list2, list3 = [], [], []
	#Test 4 - correct answer = -7
#list1, list2, list3 = [7,3,5,7,1], [2,2,3,-3,4], [5,6,5,4,5]
	#Test 5
#list1, list2, list3 = [4,4], [3,2], [8,9,1]
	#Test 6
#list1, list2, list3 = [6.3,8.4,9.2], [-1.2,7.6,3.2], [4.1,-2.1,9.6]

1.

def calculate_sum(list1, list2, list3):
    if len(list1) == len(list2) == len(list3):
        result = sum((x * y - z) for x, y, z in zip(list1, list2, list3))
        return result
    else:
        return "All lists are required to be the same length."

list1, list2, list3 = [1, 2 ,3], [4,5,6], [7,8,9]
print(calculate_sum(list1, list2, list3))

list1, list2, list3 = [5,-2,4], [3,12,9], [8,4,-6]
print(calculate_sum(list1, list2, list3))

list1, list2, list3 = [], [], []
print(calculate_sum(list1, list2, list3))

list1, list2, list3 = [7,3,5,7,1], [2,2,3,-3,4], [5,6,5,4,5]
print(calculate_sum(list1, list2, list3))

list1, list2, list3 = [4,4], [3,2], [8,9,1]
print(calculate_sum(list1, list2, list3))

list1, list2, list3 = [6.3,8.4,9.2], [-1.2,7.6,3.2], [4.1,-2.1,9.6]
print(calculate_sum(list1, list2, list3))


"""



"""
# Problem 2
2.

def create_new_list(list1, list2, list3):
    if len(list1) == len(list2) == len(list3):
        new_list = [(x * y - z) for x, y, z in zip(list1, list2, list3)]
        return new_list
    else:
        return "All lists are required to be the same length."

listA, listB, listC = [1,2,3], [4,5,6], [7,8,9]
listD = create_new_list(listA, listB, listC)
print(listD)

listA, listB, listC = [5,-2,4], [3,12,9], [8,4,-6]
listD = create_new_list(listA, listB, listC)
print(listD)

listA, listB, listC = [], [], []
listD = create_new_list(listA, listB, listC)
print(listD)

listA, listB, listC = [7,3,5,7,1], [2,2,3,-3,4], [5,6,5,4,5]
listD = create_new_list(listA, listB, listC)
print(listD)

listA, listB, listC = [4,4], [3,2], [8,9,1]
listD = create_new_list(listA, listB, listC)
print(listD)

listA, listB, listC = [6.3,8.4,9.2], [-1.2,7.6,3.2], [4.1,-2.1,9.6]
listD = create_new_list(listA, listB, listC)
print(listD)


"""



#Problem 3

	#Test1 - Mean = 3, Median = 3
data_set_1 = [3,2,1,4,5]

	# Test2 - Mean = 6.1146, Median = 6
data_set_2 = [
		10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
	]

	#Test3 - Think carefully about what the output should be!
data_set_3 = []

data = data_set_1


"""
3.

def calculate_mean(data_set):
    if len(data_set) == 0:
        return None
    else:
        return sum(data_set) / len(data_set)

def calculate_median(data_set):
    sorted_data = sorted(data_set)
    length = len(sorted_data)
    
    if length == 0:
        return None
    elif length % 2 == 1:
        return sorted_data[length // 2]
    else:
        mid1 = sorted_data[length // 2 - 1]
        mid2 = sorted_data[length // 2]
        return (mid1 + mid2) / 2

data_set_1 = [3,2,1,4,5]
mean_1 = calculate_mean(data_set_1)
median_1 = calculate_median(data_set_1)
print(f"Data set 1 - Mean = {mean_1}, Median = {median_1}")

data_set_2 = [
    10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
]
mean_2 = calculate_mean(data_set_2)
median_2 = calculate_median(data_set_2)
print(f"Data set 2 - Mean = {mean_2:.4f}, Median = {median_2}")

data_set_3 = []
mean_3 = calculate_mean(data_set_3)
median_3 = calculate_median(data_set_3)
print(f"Data set 3 - Mean = {mean_3}, Median = {median_3}")

"""


