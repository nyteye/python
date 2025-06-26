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

# ******Our sample list full******
my_list = [7, 2, 8, 5, 1]
n = len(my_list)

print(f"Original list: {my_list}\n")

# --- This is the OUTER LOOP ---
# It ensures that we repeat the passes 'n' times.
for i in range(n):
    print(f"--- Pass {i + 1} ---")

    # --- This is the INNER LOOP ---
    # With each pass 'i', the largest elements are already at the end,
    # so we can reduce the range of the inner loop to 'n - i - 1'.
    for j in range(n - i - 1):
        # Compare adjacent elements
        if my_list[j] > my_list[j+1]:
            # Swap them if the one on the left is larger
            print(f"  Swapping {my_list[j]} and {my_list[j+1]}")
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    
    print(f"List after pass {i + 1}: {my_list}\n")

print(f"Final sorted list: {my_list}")

""" Original list: [7, 2, 8, 5, 1]

--- Pass 1 ---
  Swapping 7 and 2
  Swapping 8 and 5
  Swapping 8 and 1
List after pass 1: [2, 7, 5, 1, 8]

--- Pass 2 ---
  Swapping 7 and 5
  Swapping 7 and 1
List after pass 2: [2, 5, 1, 7, 8]

--- Pass 3 ---
  Swapping 5 and 1
List after pass 3: [2, 1, 5, 7, 8]

--- Pass 4 ---
  Swapping 2 and 1
List after pass 4: [1, 2, 5, 7, 8]

--- Pass 5 ---
List after pass 5: [1, 2, 5, 7, 8]

Final sorted list: [1, 2, 5, 7, 8]"""

