N, K = map(int, input().split())

daily_degree = list(map(int,input().split()))
daily_degree.append(0)

sum_num = sum(daily_degree[:K])
num = [sum_num]
# print(num)
for i in range(K,N):
    num.append(num[i-K] + daily_degree[i] - daily_degree[i-K])
    # num.append(sum_num + daily_degree[i] - daily_degree[i-K])
    # print(new_degree)
    # max_degree.append(degree_sum)
print(max(num))