import random
#Linear Search algorithm
def linear_search(arr, x):
    for index in range(0,len(arr)):
        if arr[index] == x:
            return index+1
    else:
        return ("number not in list")



if __name__=='__main__':
    list_of_numbers = [random.randint(1,100) for numbers in range(10)]
    print(list_of_numbers)
    try:
        number = int(input("Enter the number to be searched in the list_of_numbers"))
    except:
        print("Enter a valid number")
    index = linear_search(list_of_numbers, number)
    print('Number found at index :{} [1-10]'.format(index))

