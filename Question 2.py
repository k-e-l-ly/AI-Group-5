# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:59:02 2022

@author: Kelly Mbai
"""

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","J1","Mada","STC","Phase3","Parking Lot"]

g.add_node("SportsComplex")
g.add_node("Siwaka")
g.add_node("Ph.1A")
g.add_node("Ph.1B")
g.add_node("Phase2")
g.add_node("J1")
g.add_node("Mada")
g.add_node("STC")
g.add_node("Phase3")
g.add_node("Parking Lot")

g.add_edge("SportsComplex","Siwaka",weight="450")
g.add_edge("Siwaka","Ph.1A",weight="10")
g.add_edge("Siwaka","Ph.1B",weight="230")
g.add_edge("Ph.1A","Ph.1B",weight="100")
g.add_edge("Ph.1B","STC",weight="50")
g.add_edge("Ph.1A","Mada",weight="850")
g.add_edge("Ph.1B","Phase2",weight="112")
g.add_edge("STC","Phase2",weight="50")
g.add_edge("STC","Parking Lot",weight="250")
g.add_edge("Phase2","Phase3",weight="500")
g.add_edge("Phase2","J1",weight="600")
g.add_edge("J1","Mada",weight="200")
g.add_edge("Phase3","Parking Lot",weight="350")
g.add_edge("Mada","Parking Lot",weight="700")

g.nodes["SportsComplex"]['pos']=(0,3)
g.nodes["Siwaka"]['pos']=(1,3)
g.nodes["Ph.1A"]['pos']=(2,3)
g.nodes["Ph.1B"]['pos']=(2,2)
g.nodes["Phase2"]['pos']=(3,2)
g.nodes["J1"]['pos']=(4,2)
g.nodes["Mada"]['pos']=(5,2)
g.nodes["STC"]['pos']=(2,1)
g.nodes["Phase3"]['pos']=(4,1)
g.nodes["Parking Lot"]['pos']=(4,0)

node_pos = nx.get_node_attributes(g,'pos')


nx.draw(g, node_size =8000, with_labels = True,)
plt.savefig("filename.png")

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