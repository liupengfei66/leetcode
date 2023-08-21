def partition(arr, left, right):
	pivot = right
	pos = left
	for i in range(left, right):
		if arr[i] < arr[pivot]:
			arr[pos], arr[i] = arr[i], arr[pos]
			pos += 1
	arr[pivot], arr[pos] = arr[pos], arr[pivot]
	return pos


def quicksort(arr, left, right):
	if left < right:
		pivot = partition(arr, left, right)
		quicksort(arr, left, pivot-1)
		quicksort(arr, pivot+1, right)



arr = [5, 4, 3, 2, 1]
quicksort(arr, 0, len(arr)-1)
print(arr)