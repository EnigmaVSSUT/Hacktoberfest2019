def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j], a[j+1]=  a[j+1], a[j]

a = [23, 11, 56, 34, 24, 12, 19, 8, 67, 54, 11]
bubble_sort(a)
print ("Array after sorting is:")
for i in range(len(a)):
    print (a[i])
