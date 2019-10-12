def binarySearch(arr, l, r, x):
    mid = (l + r) // 2
    if l <= r:
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    return -1


if __name__ == '__main__':
    number = 26
    listOfNumber = [0, 1, 6, 14, 15, 17, 18, 20, 21, 26, 28, 32, 44,
                    47, 59, 61, 63, 64, 65, 67, 70, 71, 75, 78, 80, 82, 96, 99]
    index = binarySearch(listOfNumber, 0, len(listOfNumber) - 1, number)
    print(index)
