# -*- coding: utf-8 -*-
"""


@author: Ivan

"""

graph={
    'start':[('siwaka', 50)],
    'siwaka':[('ph1a',10),('ph1b', 230)],
    'ph1a':[('ph1b', 100),('mada',850)],
    'ph1b':[('stc',50),('phase2', 112)],
    'stc':[('phase2',50),('parking_lot', 250)],
    'phase2':[('j1', 600),('phase3', 500)],
    'phase3':[('parking_lot', 350)],
    'j1':[('mada', 200)],
    'mada':[('parking_lot', 700)],
    'parking_lot':[]
}


def path_cost(path):
    total_cost=0
    for(node,cost) in path:
        total_cost +=cost
        return total_cost, path[-1][0]
    
path=[('siwaka',10),('ph1',10),('ph1b', 100),('stc', 50),('parking_lot',250)]

    
def ucs(graph, start, goal):
    visited = []
    frontier = [[(start,0)]]
    while frontier:   
        frontier.sort(key=path_cost) #sorting by cost
        path = frontier.pop(0) # # choosing Least cost
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph. get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path. append((node2, cost))
                frontier. append(new_path)


# In[24]:


solution = ucs(graph, 'start','parking_lot')
print('path is', solution)


# In[ ]: