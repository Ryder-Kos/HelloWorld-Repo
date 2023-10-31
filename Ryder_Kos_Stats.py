def Mean(numbers):
	if len(numbers) == 0:
		raise ValueError("Empty list")
	return sum(numbers) / len(numbers)
def Median(numbers):
	sorted_numbers = sorted(numbers)
	length = len(sorted_numbers)
    
	if length % 2 == 1:
		return sorted_numbers[length // 2]
	else:
		middle = length // 2
		return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
