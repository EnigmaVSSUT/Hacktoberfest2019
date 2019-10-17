def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot=arr[0]
    less=[x for x in arr[1:] if x<=pivot]
    greater=[x for x in arr[1:] if x>pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def main():
    my_list = [2,5,6,4,65,0]
    print(quicksort(my_list))

if __name__ == '__main__':
    main()
