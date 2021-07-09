"""Here we are doing matrix chain multiplication and we use recursion and memoization ie. bottom up
approach. So here given a array and we need find minimum no of cost ie. number of multilpication"""
import sys
def mcm(arr,i,j):
    t=[[-1 for i in range(100)]for j in range(100)]
    min=sys.maxsize
    if(i>=j):
        return 0
    elif(t[i][j]!=-1):
        return t[i][j]
    #Here we take k=i;k<=j-1;k++ condition
    for k in range(i,j):
        temp=mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if(temp<min):
            min=temp
    t[i][j]=min
    return t[i][j]

arr=[40,20,30,10,30]
print(mcm(arr,1,len(arr)-1))