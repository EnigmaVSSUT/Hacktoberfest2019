# Closest Pair Problem

# sorting according to the y axis
def ysort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 
points_left = []
points_right=  []

# Here a is the set of points , we have to find the closest pair among them
a = [[2,3],[5,6],[7,8],[2,1],[2,7],[2,5],[6,7]]


a.sort()
ysort(a)


for i in range(0,len(a)//2):
  points_left.append(a[i])
for i in range((len(a)//2) +1 ,len(a)-1):
  points_right.append(a[i])

print('The points on the left is ',points_left)
print('The points on the right is' ,points_right)
