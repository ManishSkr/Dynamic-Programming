"""Here we have two strings and we need to find longest common subsequence between two strings
expl": str1:abbcfdefg, str2:adbgcghju and output we need to print the length o/p:
here we use top down approach because recursion is very slow for long strings"""

def lcs(str1,str2,m,n):
    table=[[0 for i in range(n+1)]for j in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(i==0 or j ==0):
                return 0
            elif(str1[i-1]==str2[j-1]):
                table[i][j]=1+table[i-1][j]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    

    return table[i][j]

str1="abbcfdefg"
str2="adbgcghju"

print(lcs(str1,str2,len(str1),len(str2)))