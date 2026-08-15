t=int(input())
for _ in range(t):
    mat=[input() for _ in range(10)]
    score=0
    for i in range(10):
        for j in range(10):
            if mat[i][j]=="X":
                if i==0 or i==9 or j==0 or j==9:
                    score+=1
                elif i==1 or i==8 or j==1 or j==8:
                    score+=2
                elif i==2 or i==7 or j==2 or j==7:
                    score+=3
                elif i==3 or i==6 or j==3 or j==6:
                    score+=4
                elif i==4 or i==5 or j==4 or j==5:
                    score+=5
    print(score)