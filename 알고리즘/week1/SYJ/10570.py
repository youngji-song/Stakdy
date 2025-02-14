T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    count = 0
    
    for p in range(A,B+1):
        # 제곱근이 팰린드롬
        sqrt_p = p**0.5
        if sqrt_p == int(sqrt_p):
            sqrt_p = int(sqrt_p)
            
            if str(sqrt_p) == (str(sqrt_p))[::-1]:
           
                # 팰린드롬
                p = str(p)
                if p == p[::-1]:
                    count += 1
    
    print(f'#{test_case+1} {count}')