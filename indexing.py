###to count occurrences of minimum element...................................................................................................

arr = [4,2,4,3,6,7,8,45,45,23,1,45,0]
size = len(arr)
print("length of array",size)
nano = 0
mint = arr[0]
for i in range(0,size):  
    if arr[i]>mint:
          mint = arr[i]
          nano = i

count = 0
for j in range(size):
     if mint==arr[j]:
         count = count+1
print("index-",nano,"max or min value", mint,"counter-->",count)







##for the index finding.......................................................................................................................... 

arr = [4, 2, 0, 3, 0, 7, 0, 45, 23, 1, 45, 0]
size = len(arr)

# Step 1: Find the minimum value
min_val = arr[0]
for i in range(1, size):
    if arr[i] < min_val:
        min_val = arr[i]

# Step 2: Print all indices where that min value occurs
print("Minimum value is:", min_val)
print("It occurs at indices:")

for i in range(size):
    if arr[i] == min_val:
        print(i)  # print index





#Code Store Indices Where Maximum Occurs:.................................................................................................................

arr = [4, 2, 0, 3, 0, 7, 0, 45, 23, 1, 45, 0]
size = len(arr)

# Step 1: Find the maximum value
maxt = arr[0]
for i in range(1, size):
    if arr[i] > maxt:
        maxt = arr[i]

# Step 2: Store indices where max occurs
max_indices = []

for i in range(size):
    if arr[i] == maxt:
        max_indices.append(i)

# Output
print("Maximum value:", maxt)
print("It occurs at indices:", max_indices)
