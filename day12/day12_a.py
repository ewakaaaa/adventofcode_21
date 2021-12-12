import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file

puzzle = read_file(12,test = True)

graph = {}
for line in puzzle:
    start, end = line.replace("\n",'').split("-")
    if start not in graph.keys():
        graph[start] = [end]
    else:
        value = graph[start]
        value.append(end)
        graph[start] = value
    if end not in graph.keys():
        graph[end] = [start]
    else: 
        value = graph[end]
        value.append(start)
        graph[end] = value


def solution(graph,point,visited,path:str):
    path += point
    if point == 'end':
        my_set = set()
        my_set.add(path)
        return my_set
    if point in visited:
        return set()
    paths = set()
    for i in graph[point]:
        if point.islower():
            visited.append(point)
        paths.update(solution(graph,i,visited.copy(),path))
    return paths

print(len(solution(graph,'start',[],'')))



