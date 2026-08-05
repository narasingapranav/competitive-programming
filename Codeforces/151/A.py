n, k, l, c, d, p, nl, np=map(int, input().split())
drinks=k*l
s=drinks//nl
toasts=c*d
salt=p//np
print(min(s, toasts, salt)//n)