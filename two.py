def twoSum (arr, target):
	res = []
	for i in range(0,(len(arr))):
			if arr[i-1] + arr[i] == target:
				res.append(i-1),res.append(i)
	return res

arr = [3, 5, 2, -4, 8, 11]
target = 7
print(twoSum(arr, target))
      