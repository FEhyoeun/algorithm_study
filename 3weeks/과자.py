K, N, M = list(map(int, input().split()))
result = (K * N) - M
print(result if result > 0 else 0)