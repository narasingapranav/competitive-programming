def countdiv(n):
    c=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            c+=1
            if i!=n//i:
                c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if countdiv(i)==3:
        print("YES")
    else:
        print("NO")
'''
1
999966000289

'''