def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1

def main():
    # Test binary search function with an array size of 5
    arr = [ 2, 3, 4, 10, 40]
    x = 10
    result = binary_search(arr, x)
    if result != -1:
        print("The element that the algorithm is searching for has an index of", str(result))
    else:
        print("Element is not in array")

    # Test binary search function with an array size of 10

    arr = [ 2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
    x = 70
    result = binary_search(arr, x)
    if result != -1:
        print("The element that the algorithm is searching for has an index of", str(result))
    else:
        print("Element is not in array")

    # Test binary search function with an array size of 20
    arr = [ 2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    x = 97
    result = binary_search(arr, x)
    if result != -1:
        print("The element that the algorithm is searching for has an index of", str(result))
    else:
        print("Element is not in array")

if __name__ == "__main__":
    main()
