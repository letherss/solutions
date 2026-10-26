def binary_search (arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else: low = mid + 1
    return -1
if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 5, 6, 7], 4)
    binary_search([1, 2, 3, 4, 5, 6, 7], 8)
    binary_search([], 1)