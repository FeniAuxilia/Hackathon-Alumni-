import json
import math

f = open("Y:\Student Handout\Input data\level0.json")
n_dict = json.load(f)
n_neighbourhoods = n_dict["n_neighbourhoods"]
n_restaurants = n_dict["n_restaurants"]
neighbourhoods = n_dict["neighbourhoods"]
restaurants = n_dict["restaurants"]
vehicles = n_dict["vehicles"]
n_vehicles = len(vehicles)
restaurant_distance = []
neighbourhood_distance = []
for i in range(n_neighbourhoods): 
    num_dict0 = neighbourhoods[f"n{i}"]
    order_quantity = num_dict0["order_quantity"]
    distances = num_dict0["distances"]
    #print(f"Order Quantity of n{i}: {order_quantity}")
    #print(f"Distance of n{i}: {distances}")

for i in range(n_restaurants):
    num_dict1 = restaurants[f"r{i}"]
    neighbourhood_distance = num_dict1["neighbourhood_distance"]
    restaurant_distance = num_dict1["restaurant_distance"]

for i in range(n_vehicles):
    num_dict2 = vehicles[f"v{i}"]
    start_point = num_dict2["start_point"]
    speed = num_dict2["speed"]
    capacity = num_dict2["capacity"]
#print(vehicles)

matrix = []

for i in range(n_neighbourhoods): 
    num_dict0 = neighbourhoods[f"n{i}"]
    order_quantity = num_dict0["order_quantity"]
    distances = num_dict0["distances"]
    #print(f"Order Quantity of n{i}: {order_quantity}")
    #print(f"Distance of n{i}: {distances}")
    matrix.append(distances)
matrix.append(neighbourhood_distance)
matrix[0].append(0)
for i in range(n_neighbourhoods + n_restaurants-1):
    matrix[i+1].append(neighbourhood_distance[i])

def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    
    current_city = 20
    tour.append(current_city)
    visited[current_city] = True

    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance
        print(tour, nearest_distance, total_distance)

    tour.append(20)
    total_distance += distances[current_city][20]

    return tour, total_distance

tour, total_distance = solve_tsp_nearest(matrix)
print("Tour:", tour)
print("Total distance:", total_distance)
