"""Here we see the minimum number of insertion in a string to make it a palindrome
there is string given s:acbcbda and o/p is number to insertion u make here o/p is : 2"""

"""The approach is similar to minimum number of intersion to make a palindrome"""

def lcs(str1,str2,m,n):
    table=[[0 for i in range(n+1)]for j in range(m+1)]
    str3=""
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(i==0 or j ==0):
                return 0
            elif(str1[i-1]==str2[j-1]):
                table[i][j]=1+table[i-1][j]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    

    return table[i][j]



str1="acbcdba"
str2=str1[::-1]
print(len(str1)-lcs(str1,str2,len(str1),len(str2)))