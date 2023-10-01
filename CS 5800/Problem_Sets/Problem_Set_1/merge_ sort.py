def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
def main():

    # Test merge sort with an array of size 5
    arr = [7, 4, 3, 7, 4 ]
    merge_sort(arr)
    print("The array in numerical order is", arr)
 
    # Test merge sort with an array of size 10 
    arr = [7, 4, 3, 7, 4, 1, 2, 3, 4, 5]
    merge_sort(arr)
    print("The array in numerical order is", arr)
 
    # Test merge sort with an array of size 10 
    arr = [7, 4, 3, 7, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    merge_sort(arr)
    print("The array in numerical order is", arr)
 
if __name__ == "__main__":
    main()
