def linerar(arr,target):
  for i in range(len(arr)):
    if arr[i]>target: # if 0>4,1>4,2>4,3>4,4>4, 5(i)>4
      arr[i],arr[i+1]=arr[i+1],arr[i]  #5,6=6,5, so in this-5=6,6=5
      return arr  # return will be 1,2,3,4,6,5
  return -1



a = [1,2,3,4,5,6]
target = 4
d1 = linerar(a,target)
print(d1) #>>[1, 2, 3, 4, 6, 5]
