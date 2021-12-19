import numpy as np
from collections import Counter

def get_small_caves(edges):
    edges_flat = np.concatenate(edges)
    small_caves=set()
    for it in edges_flat:
        if it not in ['end','start'] and it.islower():
            small_caves.add(it)
    return small_caves

def generate_graph(edges):
    graph={}
    for i in set(np.concatenate(edges)):
        graph.update({i:set()})
    for edge in edges:
        if edge[1] != 'start':
            graph[edge[0]].add(edge[1])
        if edge[1] !='end':
            graph[edge[1]].add(edge[0])
    #print(graph)
    return graph

def generate_all_paths(graph, start, end,small_caves, max_visit,path =[]):
    path = path + [start]
    # we reach an end return solutions
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        new_paths=path
        if node.isupper() or ((node in small_caves) and node not in path) or node==end :
            new_paths = generate_all_paths(graph, node, end,small_caves,max_visit, new_paths)
        elif (node in small_caves) and (node in path):
            #print("Small node in path :",node)
            occurences = Counter(path)
            if node in occurences and occurences[node]>max_visit:
                continue
            already_visitied_small_cave=False
            for i in small_caves:
                if occurences[i]>=max_visit:
                    already_visitied_small_cave =True
            if occurences[node] <max_visit and not already_visitied_small_cave:
                new_paths = generate_all_paths(graph, node, end,small_caves,max_visit, new_paths)
            else:
                continue
        else:
            continue
        for p in new_paths:
            paths.append(p)
    return paths

def get_all_paths(edges,max_visit=0):
    graph = generate_graph(edges)
    small_caves = get_small_caves(edges)
    all_paths = generate_all_paths(graph, 'start', 'end',small_caves,max_visit)
    print("{} possible path".format(len(all_paths)))
    #print(all_paths)

def get_data():
    path = str(input())
    with open(path) as file:
        edges = [[i.strip() for i in x.split("-")] for x in file.readlines()]
        print(edges)
        get_all_paths(edges,1)
        get_all_paths(edges,2)

if __name__=="__main__":
	get_data()
