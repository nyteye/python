def bubble_sort(arr):
    n = len(arr)

    # Outer loop to control number of passes
    for i in range(n - 1):
        # Inner loop for comparing adjacent elements
        # With each outer pass, the largest element is placed at the end,
        # so we can ignore the last i elements (already sorted).
        for j in range(n - i - 1):
            # Compare current element with the next one
            if arr[j] > arr[j + 1]:
                # Swap if the current element is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

# --- Example Usage ---
if __name__ == "__main__":
    my_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original List:", my_numbers)
    print("Sorted List:  ", bubble_sort(my_numbers))

    my_other_numbers = [5, 1, 4, 2, 8]
    print("\nOriginal List:", my_other_numbers)
    print("Sorted List:  ", bubble_sort(my_other_numbers))
