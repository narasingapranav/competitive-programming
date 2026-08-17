l = input()
ans = ''
i = 0
while i < len(l):
    if l[i] == '.':
        ans += '0'
        i += 1
    elif l[i:i+2] == '-.':
        ans += '1'
        i += 2
    elif l[i:i+2] == '--':
        ans += '2'
        i += 2
print(ans)