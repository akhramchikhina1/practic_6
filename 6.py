n, k, m= map(int, input().split())
total_children= n*2
total_time=total_children*m
rounds= total_children//k
if total_children%k!=0:
    rounds+=1
total=rounds*m
print(total)