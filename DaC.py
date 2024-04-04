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
