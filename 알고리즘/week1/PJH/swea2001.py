T = int(input())

for test_case in range(1,T+1):
    M,N = map(int,input().split())
    list_bug = [list(map(int,input().split())) for _ in range(M)]
    bug_n = []
    bug_sum = []
    for i in range(M-N+1):
        for j in range(M-N+1):
            bugs = 0
            for a in range(N):
                for b in range(N):
                    bugs += list_bug[i+a][j+b]
            bug_sum.append(bugs)
    print(f'#{test_case} {max(bug_sum)}')
                





