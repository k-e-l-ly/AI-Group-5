# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:11:58 2022

@author: Kelly Mbai

# group work question 2

"""



graph = {
    'SportsComplex': [('Siwaka', 450)],
    'Siwaka':[('Ph.1A', 10), ('Ph.1B', 230)],
    'Ph.1A':[('Mada', 850), ('Ph.1B', 100)],
    'Ph.1B':[('Phase2', 112), ('STC', 50)],
    'STC':[('Phase2', 50), ('ParkingLot', 250)],
    'Phase2':[('J1', 600), ('Phase3', 500), ('STC', 50)],
    'J1':[('Mada', 200)],
    'Phase3':[('ParkingLot', 350)],
    'Mada':[('ParkingLot', 700)],
    #'ParkingLot':[]
    }

H_table = {
    'SportsComplex': 730,
    'Siwaka': 405,
    'Ph.1A': 380,
    'Ph.1B': 280,
    'STC': 213,
    'Phase2': 210,
    'J1': 500,
    'Phase3': 160,
    'Mada': 630,
    'ParkingLot': 0
    }

def path_h_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    # f_cost = g_cost + h_cost
    return h_cost, last_node


# path = [('SportsComplex', 0), ('Siwaka', 100), ('Ph.1B', 500)]
# print(path_h_cost(path))

# path = [('SportsComplex', 0), ('Siwaka', 100), ('Ph.1A', 200)]
# print(path_h_cost(path))

def Greedy_best_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_h_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)
         
solution = Greedy_best_search(graph, 'SportsComplex', 'ParkingLot')
print('Solution is', solution)
