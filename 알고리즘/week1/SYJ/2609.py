A, B = map(int, input().split())

def gcd(a,b): #최대공약수
    i = min(a,b)
    while True:
        if A%i == 0 and B%i == 0:
            gcd = i
            break
        else:
            i -= 1
    return gcd

def lcm(a,b): #최소공배수
    lcm = int(a*b/gcd(a,b))
    return lcm

print(gcd(A,B))
print(lcm(A,B))