import sys

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def tsp_divide_conquer(points):
    if len(points) <= 2:
        return sum(distance(points[i], points[i-1]) for i in range(len(points)))
    
    # Dividir los puntos en dos conjuntos aproximadamente iguales
    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    # Resolver recursivamente para cada conjunto
    min_dist_left = tsp_divide_conquer(left_points)
    min_dist_right = tsp_divide_conquer(right_points)

    # Encontrar la distancia mínima entre los dos conjuntos
    min_dist_across = min(distance(left_points[-1], right_points[0]),
                          distance(right_points[-1], left_points[0]))

    return min_dist_left + min_dist_right + min_dist_across

# Ejemplo de uso
points = [(0, 0), (1, 2), (3, 4), (5, 1), (2, 3)]
print("Distancia mínima recorrida:", tsp_divide_conquer(points))



# def tsp_divide_conquer(cities):
#     # Base case: if there's only one city, no travel needed
#     if len(cities) == 1:
#         return 0, cities
    
#     # Divide the cities into two roughly equal subsets
#     mid_point = len(cities) // 2
#     left_subset = cities[:mid_point]
#     right_subset = cities[mid_point:]
    
#     # Conquer: Solve TSP for each subset recursively
#     cost_left, path_left = tsp_divide_conquer(left_subset)
#     cost_right, path_right = tsp_divide_conquer(right_subset)
    
#     # Combine: Find the best way to connect the two paths
#     # This step is highly simplified and would need a more complex implementation
#     # to properly merge the two paths with the minimal additional cost
#     combined_cost, combined_path = connect_paths(path_left, path_right)
    
#     return combined_cost, combined_path

# def connect_paths(path_left, path_right):
#     # Placeholder function: in a real scenario, you would need to implement a way to
#     # find the shortest path that connects the end of path_left to the start of path_right
#     # and vice versa, then choose the one that minimizes the additional cost.
#     # This might involve solving a smaller TSP instance for the connecting cities.
#     return 0, path_left + path_right  # Simplified to just concatenate paths

# # Example usage
# cities = [(x, y) for x, y in enumerate(range(10))]  # Example set of cities as (x, y) tuples
# total_cost, path = tsp_divide_conquer(cities)
# print(f"Total cost: {total_cost}, Path: {path}")