# Find the minimal number of pillars to remove to build a perfect ride
cable_car = [10, 13, 20, 30, 40, 42, 44, 46, 48, 50, 60, 70, 80, 82, 85, 87, 90, 100, 101, 110, 113, 117, 121]
#            0    1   2   3   4  5   6    7   8   9  10   11  12 13  14  15  16  17   18   19   20    21   22
#            11      10   9   8                   7  6     5   4             3   2         1

def find_min_remove(cable_car):
    min_remove = 0
    n = len(cable_car)
    dp = [([2] * n) for i in range(n)] ######
    longest = 1

    j = n - 2
    while j >= 0:
        i = j - 1
        k = j + 1
        while i >= 0 and k < n:
            if cable_car[i] + cable_car[k] == cable_car[j] * 2:
                dp[i][j] = dp[j][k] + 1
                i -= 1
                k += 1
            elif cable_car[i] + cable_car[k] > cable_car[j] * 2:
                i -= 1
            else:
                k += 1
        j -= 1

    find_max = []
    for i in range(n):
        find_max.append(max(dp[i]))
    longest = max(find_max)
        
    min_remove = n - longest

    return min_remove

print("length:", len(cable_car))
print("min_remove", find_min_remove(cable_car))
