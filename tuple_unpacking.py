arr = [1, 3] # Initialize a list named 'arr' with two integer elements: 1 at index 0 and 3 at index 1.

# Create a temporary tuple 'temp' by taking the element at index 1 of 'arr' (which is 3)
# as its first element, and the element at index 0 of 'arr' (which is 1) as its second element.
# At this point, temp will be (3, 1).
temp = (arr[1], arr[0])

# Assign the first element of the 'temp' tuple (which is 3) to the element at index 0 of 'arr'.
# 'arr' now becomes [3, 3].
arr[0] = temp[0]

# Assign the second element of the 'temp' tuple (which is 1) to the element at index 1 of 'arr'.
# 'arr' now becomes [3, 1].
arr[1] = temp[1]

# Print the current state of the list 'arr' to the console.
# The output will be [3, 1].
print(arr)
