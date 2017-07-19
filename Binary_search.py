# Define binary search function

def binary_search(list,item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = int((low + high)/ 2)
		guess = list[mid]
		if guess == item:
			return item
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None 

my_list = [1,3,5,7,9,11,13,15,17,19,21,25]

print(binary_search(my_list, 3))