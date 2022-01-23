arr = list(map(int, (input()).split()))
print('OK' if sum(arr) >= 100 else 'Soongsil' if min(arr) == arr[0] else 'Korea' if min(arr) == arr[1] else 'Hanyang')