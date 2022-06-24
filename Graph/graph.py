import re
from collections import deque

def get_graph(filename):
    adjacent_list = {}
    with open(filename, "r") as file:
        for edge in file:
            file_content = re.split('[ \n]', edge)
            if len(file_content) == 3:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2]]
            elif len(file_content) == 4:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2]]
            elif len(file_content) == 5:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2], file_content[3]]
            elif len(file_content) == 6:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2], file_content[3],
                                                  file_content[4]]
    return adjacent_list
vertex=[]
adjacent=[]
edges=[] 
def bfs(graph, src, dest):
    queue = deque()
    visited = {src: 1}
    parent = {}
    queue.append(src)
    while queue:
        last = queue.popleft()
        if last == dest:
            node = last
            path = []
            while node:
                path.append(node)
                node = parent.get(node, None)
            return path[::-1]
        for neighbors in graph[last]:
            if neighbors[0] not in visited:
                visited[neighbors[0]] = 1
                parent[neighbors[0]] = last
                queue.append(neighbors[0])
    return "graph is not connected"