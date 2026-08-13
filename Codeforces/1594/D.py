from collections import defaultdict
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(m):
        u,v,c=map(str,input().split())
        u,v=int(u)-1,int(v)-1
        w=1 if c=='imposter' else 0
        graph[u].append((v,w))
        graph[v].append((u,w))
    role=[-1]*n
    ans=0
    possible=True
    for i in range(n):
        if role[i]!=-1:
            continue
        st=[i]
        role[i]=0
        count=[1,0]
        while st:
            u=st.pop()
            for v,w in graph[u]:
                exp=role[u]^w
                if role[v]==-1:
                    role[v]=exp
                    count[exp]+=1
                    st.append(v)
                elif role[v]!=exp:
                    possible=False
                    break
            if not possible:
                break
        if not possible:
            break
        ans+=max(count)
    if not possible:
        print(-1)
    else:
        print(ans)