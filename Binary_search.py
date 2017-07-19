# Define binary search function

def binary_search(list,item):
	# low and high keep track of which part of the list you'll search in
	low = 0
	high = len(list) - 1
	# while you it haven't narrowed down to one element
	while low <= high:
		mid = (low + high)// 2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	# Item doesn't exist
	return None 

my_list = [1,3,5,7,9,11,13,15,17,19,21,25]

print(binary_search(my_list, 25)) # => 11
print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -5)) # => None