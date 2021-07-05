""" Here we find longest repeating subsequence given arr=aabebcdd, here longest repeating sequence=apd so 
we have to print the length ie.3"""

def lrs(str1,str2,m,n,):
    table=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(i==0 or j==0):
                return 0
            elif(str1[i-1]==str2[j-1] and i!=j):
                table[i][j]= 1+table[i-1][j-1]
            else:
                table[i][j]= max(table[i-1][j],table[i][j-1])
    return table[m][n]

str1=str2="aabebcdd"
print(lrs(str1,str2,len(str1),len(str1)))
