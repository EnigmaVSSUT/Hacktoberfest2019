#Jump Search algorithm works only for sorted array
import random

#Linear Search algorithm
def linear_search(arr, x):
    for index in range(0,len(arr)):
        if(arr[index] == x):
            return (index)
    else:
        return ("number not in list")

#Jump Search algorithm
def jump_search(arr, x):
    interval = 3
    count = -1
    for index in range(0,len(arr),interval):
        if (arr[index] == x):
            return index+1
        elif (arr[index] > x):
            arr2 = arr[index-interval:]
	    #implement linear_search algorithm
            index = linear_search(arr2, x)
            return (index+1)+(count*3)
        count = count + 1

    else:
        return "number not in list"

if __name__ == '__main__':
    list_of_numbers = [random.randint(1,101) for numbers in range(10)]
    #sort the list_of_numbers
    list_of_numbers.sort()
    print(list_of_numbers)
    try:
        number = int(input("Enter a number to be searched"))
    except:
        print("Not a valid number")
    index = jump_search(list_of_numbers, number)
    print('Number found at index : ',index,'[1-10]')

