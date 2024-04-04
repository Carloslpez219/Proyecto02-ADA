import time
import matplotlib.pyplot as plt

# Dynamic Programming Algorithm

input_tests = [
    [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 1, 2, 3], [0, 1, 0, 4, 5], [0, 2, 4, 0, 6], [0, 3, 5, 6, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 10, 15], [0, 7, 0, 6, 8], [0, 10, 6, 0, 12], [0, 15, 8, 12, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 3, 5, 7], [0, 3, 0, 1, 4], [0, 5, 1, 0, 2], [0, 7, 4, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 4, 2, 1], [0, 4, 0, 3, 2], [0, 2, 3, 0, 1], [0, 1, 2, 1, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 5, 8, 3], [0, 5, 0, 1, 6], [0, 8, 1, 0, 2], [0, 3, 6, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 3, 6], [0, 7, 0, 5, 8], [0, 3, 5, 0, 4], [0, 6, 8, 4, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 2, 6, 4], [0, 2, 0, 4, 5], [0, 6, 4, 0, 3], [0, 4, 5, 3, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 8, 5, 7], [0, 8, 0, 2, 4], [0, 5, 2, 0, 3], [0, 7, 4, 3, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 6, 4, 3], [0, 6, 0, 2, 5], [0, 4, 2, 0, 1], [0, 3, 5, 1, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 1, 2, 3], [0, 1, 0, 4, 5], [0, 2, 4, 0, 6], [0, 3, 5, 6, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 10, 15], [0, 7, 0, 6, 8], [0, 10, 6, 0, 12], [0, 15, 8, 12, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 3, 5, 7], [0, 3, 0, 1, 4], [0, 5, 1, 0, 2], [0, 7, 4, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 4, 2, 1], [0, 4, 0, 3, 2], [0, 2, 3, 0, 1], [0, 1, 2, 1, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 5, 8, 3], [0, 5, 0, 1, 6], [0, 8, 1, 0, 2], [0, 3, 6, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 3, 6], [0, 7, 0, 5, 8], [0, 3, 5, 0, 4], [0, 6, 8, 4, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 2, 6, 4], [0, 2, 0, 4, 5], [0, 6, 4, 0, 3], [0, 4, 5, 3, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 8, 5, 7], [0, 8, 0, 2, 4], [0, 5, 2, 0, 3], [0, 7, 4, 3, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 6, 4, 3], [0, 6, 0, 2, 5], [0, 4, 2, 0, 1], [0, 3, 5, 1, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 1, 2, 3], [0, 1, 0, 4, 5], [0, 2, 4, 0, 6], [0, 3, 5, 6, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 10, 15], [0, 7, 0, 6, 8], [0, 10, 6, 0, 12], [0, 15, 8, 12, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 3, 5, 7], [0, 3, 0, 1, 4], [0, 5, 1, 0, 2], [0, 7, 4, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 4, 2, 1], [0, 4, 0, 3, 2], [0, 2, 3, 0, 1], [0, 1, 2, 1, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 5, 8, 3], [0, 5, 0, 1, 6], [0, 8, 1, 0, 2], [0, 3, 6, 2, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 7, 3, 6], [0, 7, 0, 5, 8], [0, 3, 5, 0, 4], [0, 6, 8, 4, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 2, 6, 4], [0, 2, 0, 4, 5], [0, 6, 4, 0, 3], [0, 4, 5, 3, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 8, 5, 7], [0, 8, 0, 2, 4], [0, 5, 2, 0, 3], [0, 7, 4, 3, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 6, 4, 3], [0, 6, 0, 2, 5], [0, 4, 2, 0, 1], [0, 3, 5, 1, 0]]
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

dynamic_times = []
for test in input_tests:
    n = len(test) - 1
    dist = test
    memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]
    
    total_time = 0
    num_runs = 1000
    for _ in range(num_runs):
        start_time = time.time()
        ans = 10**9
        for i in range(1, n+1):
            ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])
        end_time = time.time()
        total_time += end_time - start_time
    
    average_time = total_time / num_runs
    dynamic_times.append(average_time)

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

divide_conquer_times = []
for test in input_tests:
    total_time = 0
    num_runs = 1000
    for _ in range(num_runs):
        start_time = time.time()
        tsp_divide_conquer([(0, 0)] + [(x[1], x[2]) for x in test[1:]])
        end_time = time.time()
        total_time += end_time - start_time
    
    average_time = total_time / num_runs
    divide_conquer_times.append(average_time)

# Plotting
x = range(1, len(input_tests) + 1)

plt.figure(figsize=(12, 6))
plt.plot(x, dynamic_times, marker='o', label='Dynamic Programming', color='b')
plt.plot(x, divide_conquer_times, marker='x', label='Divide and Conquer', color='r')
plt.xlabel('Test Case')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Execution Times')
plt.xticks(x)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('execution_times_comparison.png')
plt.show()
