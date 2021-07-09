"""This is another variation of matrix chain muliplication. Here one string is given and
we parition the string in that way that all partition are palindrome and return the
number of minimum partition. we use recursion with memoization"""

import sys
def isPalindrome(arr,i,j):
    val=arr[i:j+1]
    #check the string is palindrome or not
    if(val==val[::-1]):
        return True
    return False

def palindromePartition(arr,i,j):
    table=[[-1 for i in range(100)]for j in range(100)]
    min=sys.maxsize
    if(i>=j):
        return 0
    elif(isPalindrome(arr,i,j)):
        return 0
    elif(table[i][j]!=-1):
        return table[i][j]
    #Here we take k=i;k<=j-1;k++ condition
    for k in range(i,j):
        temp=palindromePartition(arr,i,k)+palindromePartition(arr,k+1,j)+1
        if(temp<min):
            min=temp
    table[i][j]=min
    return table[i][j]

str1="manish"
print(palindromePartition(str1,0,len(str1)))