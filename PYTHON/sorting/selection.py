def selection_sort(a):
    for i in range(0, len(a)):
        min=i
        for j in range(i+1,len(a)):
            if(a[min]>a[j]):
                min=j
        a[i], a[min]=  a[min], a[i]


a = [23, 11, 56, 34, 24, 12, 19, 8, 67, 54, 11]
selection_sort(a)
print ("Array after sorting is:")
for i in range(len(a)):
    print (a[i])
