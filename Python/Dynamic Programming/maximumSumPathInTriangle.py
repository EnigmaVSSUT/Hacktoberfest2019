# trunc8
import math

arr = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
N = int(math.sqrt(2*len(arr)))
arr2 = []
start = 0
endVar = 1
end = 1

while len(arr2) is not N:
    arr2.append(arr[start:end])
    start = end
    endVar = endVar + 1
    end = end + endVar

for i in arr2:
    print(i)

tempArr = []

while len(arr2) is not 1:
    arr2[-2][-1] = arr2[-2][-1] + max(arr2[-1][-1], arr2[-1][-2])
    tempArr.insert(0, arr2[-2][-1])
    del arr2[-1][-1]
    del arr2[-2][-1]
    if len(arr2[-2]) == 0:
        arr2[-1] = tempArr
        del arr2[-2]
        tempArr = []
    print("Array2 is: ", arr2)
    print("TempArr is: ", tempArr)

print("Largest Sum is: ", arr2[0][0])