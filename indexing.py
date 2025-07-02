###to count occurrences of minimum element

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
