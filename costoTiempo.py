import time
import matplotlib.pyplot as plt

# Dynamic Programming Algorithm

input_tests = [
    [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 1, 2, 3], [0, 1, 0, 4, 5], [0, 2, 4, 0, 6], [0, 3, 5, 6, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 10, 15], [0, 7, 0, 6, 8], [0, 10, 6, 0, 12], [0, 15, 8, 12, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 3, 5, 7], [0, 3, 0, 1, 4], [0, 5, 1, 0, 2], [0, 7, 4, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 4, 2, 1], [0, 4, 0, 3, 2], [0, 2, 3, 0, 1], [0, 1, 2, 1, 0]]
]

def fun(i, mask):
    if mask == ((1 << i) | 3):
        return dist[1][i]
 
    if memo[i][mask] != -1:
        return memo[i][mask]
 
    res = 10**9
    for j in range(1, n+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
    memo[i][mask] = res
    return res

dynamic_costs = []
dynamic_times = []

for idx, test in enumerate(input_tests[:5], 1):
    n = len(test) - 1
    dist = test
    memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]
    
    start_time = time.time()
    ans = 10**9
    for i in range(1, n+1):
        ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])
    end_time = time.time()
    
    dynamic_times.append(end_time - start_time)
    dynamic_costs.append(ans)

# Divide and Conquer Algorithm
def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def tsp_divide_conquer(points):
    if len(points) <= 2:
        return sum(distance(points[i], points[i-1]) for i in range(len(points)))
    
    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    min_dist_left = tsp_divide_conquer(left_points)
    min_dist_right = tsp_divide_conquer(right_points)
    min_dist_across = min(distance(left_points[-1], right_points[0]),
                          distance(right_points[-1], left_points[0]))

    return min_dist_left + min_dist_right + min_dist_across

divide_conquer_costs = []
divide_conquer_times = []

for idx, test in enumerate(input_tests[:5], 1):
    start_time = time.time()
    tsp_divide_conquer([(0, 0)] + [(x[1], x[2]) for x in test[1:]])
    end_time = time.time()
    
    divide_conquer_times.append(end_time - start_time)
    divide_conquer_costs.append(tsp_divide_conquer([(0, 0)] + [(x[1], x[2]) for x in test[1:]]))

# Plotting
x = range(1, 6)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, dynamic_costs, marker='o', label='Dynamic Programming', color='b')
plt.plot(x, divide_conquer_costs, marker='x', label='Divide and Conquer', color='r')
plt.xlabel('Test Case')
plt.ylabel('Cost of Tour')
plt.title('Cost of Tour Comparison')
plt.xticks(x)
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, dynamic_times, marker='o', label='Dynamic Programming', color='b')
plt.plot(x, divide_conquer_times, marker='x', label='Divide and Conquer', color='r')
plt.xlabel('Test Case')
plt.ylabel('Time (seconds)')
plt.title('Execution Time Comparison')
plt.xticks(x)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('cost_vs_time_comparison.png')
plt.show()