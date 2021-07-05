"""here two string were given if all characters in a sequencally present in b then we print true or else print
false. This is same as lcs"""

def spm(str1,str2,m,n):
    if(m==0 or n==0):
        return 0
    elif(str1[m-1]==str2[n-1]):
        return 1+spm(str1,str2,m-1,n-1)
    else:
        return max(spm(str1,str2,m,n-1),spm(str1,str2,m-1,n))

str1="axy"
str2="adxcpy"
print(spm(str1,str2,len(str1),len(str2)))