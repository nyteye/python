# ---------------------------------------------------------
# Insertion Sort Algorithm in Python
# ---------------------------------------------------------
# Idea:
# - Like sorting cards in your hand.
# - You pick the next card (key),
#   shift bigger cards to the right,
#   then insert the key into the correct gap.
#
# Mnemonic: PICK → SHIFT → INSERT
# ---------------------------------------------------------

def insertion_sort(arr):
    # Loop through each element starting from index 1
    # (index 0 is already "sorted" by itself)
    for i in range(1, len(arr)):
        
        # Step 1: PICK the element to insert
        key = arr[i]        # save the element in 'key'
        j = i - 1           # j is the index of the previous element
        
        # Step 2: SHIFT all elements greater than key to the right
        # This loop creates the "gap" for the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # move element one step right
            j = j - 1             # step left
        
        # Step 3: INSERT the key into the gap
        arr[j + 1] = key
        
        # Print array after each pass (optional: good for debugging/learning)
        print(f"After pass {i}: {arr}")
    
    return arr


# ---------------------------------------------------------
# Example Run
# ---------------------------------------------------------
arr = [6, 3, 2, 5, 9]
print("Original array:", arr)

sorted_arr = insertion_sort(arr)

print("Sorted array:", sorted_arr)


#####🔹 Things to Notice#################################################################################################################################################################################

key = arr[i] → saves the element before shifting (otherwise it would get lost).

arr[j+1] = arr[j] → shifts bigger elements one step right.

arr[j+1] = key → places the key into the correct empty spot.

Loop continues until the entire list is sorted.


💡 Tip for revision:
Whenever you see arr[j+1] = key, imagine you’re finally placing the card you’ve been holding into the right slot after sliding the bigger ones.
