# Test graph application

# function to find out path

from time import sleep


def find_path(graph, start, end, path=[]):
    path = path + [start];
    if start == end:
        return path
    if not start in graph:
        return None
    
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Create graph dictionary
graph = {
    'A':['B', 'C','R'],
    'B':['C', 'D'],
    'C':['D'],
    'D':['C'],
    'E':['F'],
    'F':['C'],
    'R':['W'],
    'W':['R']
}


# print(graph);

path=find_path(graph, 'A', 'D');
all_path=find_all_paths(graph, 'A', 'D');
print (path);
print (all_path)
