import sys
N = int(sys.stdin.readline())

dp = [0] * 91 # N은 90까지

# N=3 : 101, 100 (2개) (N=1 + N=2)
# N=4 : 1010, 1000, 1001 (3개) (N=1 + N =2)
# N=5 : 10100, 10000, 10010, 10101, 10001 (5개) = (N=3 + N=4)
# N=6 : 101000, 100000, 100100, 101010, 100010, 101001, 100001, 100101 (8개) = (N=4 + N=5)
# 위의 결과로 보았을때는 dp[N] = dp[N-1] + dp[N-2]로 보인다.
# 밑의 식으로 확인
dp[1] = 1
dp[2] = 1
for n in range(3, N + 1):# 3부터 N까지 해당 인덱스에 값 넣어줌
    dp[n] = dp[n-1] + dp[n-2]

print(dp[N])