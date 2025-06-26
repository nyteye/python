#Code for the Inner Loop (A Single Pass)

listz=[7,2,8,5,1]
n = len(listz)
print("original list",listz)

# Iterate through the list up to the second-to-last element
for j in range(n-1):
  # Compare adjacent elements
  if listz[j]>listz[j+1]:
    # Print the elements being swapped
    print("swapping>",listz[j],"",listz[j+1])
    # Swap the elements if they are in the wrong order
    listz[j],listz[j+1]=listz[j+1],listz[j]
    print(listz)

# Print the list after one pass of comparison and swapping
print(listz)


"""output-
original list [7, 2, 8, 5, 1]
swapping> 7  2
[2, 7, 8, 5, 1]
swapping> 8  5
[2, 7, 5, 8, 1]
swapping> 8  1
[2, 7, 5, 1, 8]
[2, 7, 5, 1, 8]"""
