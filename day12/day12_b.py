import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file

puzzle = read_file(12,test = True)

graph = {}
small_letters = set()
for line in puzzle:
    start, end = line.replace("\n",'').split("-")
    if start not in ("start","end") and start.islower():
        small_letters.add(start)
    if end not in ("start","end") and end.islower():
        small_letters.add(end)
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

print(graph)

def solution(graph,point,visited,path:str,small_letter,small_counter):
    path = path + point
    if point == 'end':
        my_set = set()
        my_set.add(path)
        return my_set
    if point in visited:
        return set()
    paths = set()
    for i in graph[point]:
        if point.islower():
            if point == small_letter:
                if small_counter == 0: 
                    paths.update(solution(graph, i, visited.copy(), path, small_letter, 1))
                if small_counter == 1: 
                    visited.add(point)
                    paths.update(solution(graph, i, visited.copy(), path, small_letter, 2))
            else: 
                visited.add(point)
                paths.update(solution(graph, i, visited.copy(), path, small_letter, small_counter))
        else: 
            paths.update(solution(graph,i,visited.copy(),path,small_letter,small_counter))
    return paths

total = set()
for letter in small_letters:
    total.update((solution(graph,'start',set(),'',letter,0)))

print(len(total))

