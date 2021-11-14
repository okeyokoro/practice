from pprint import pprint
from collections import defaultdict


def airportConnections(airports, routes, start):
    dsts = defaultdict(list)
    for src, dst in routes:
        dsts[src].append(dst)
        
        
    # we want to do a dfs from start and get all the nodes reachable from start
    visited = set()
    def dfs0(node):
        nonlocal visited
        visited.add(node)
        for dst in dsts[node]:
            if dst not in visited:
                dfs0(dst)
    dfs0(start)
    
    # ^ after doing this we subtract those nodes from `dsts` and `airports`
    airports = [port for port in airports if port not in visited]
    for v in visited:
        if v in dsts:
            dsts.pop(v)
    for key in dsts:
        dsts[key] = [ i for i in dsts[key] if i not in visited ]


    # now we just run a (modified) connected components on the rest of the graph
    marks = defaultdict(int)
    components = []
    
    def dfs(port, m):
        nonlocal marks
    
        if marks[port] != m:
            marks[port] = m
            for dst in dsts[port]:
                dfs(dst, m)
    
    for port in airports:
        if marks[port] == 0:
            components.append(port)
            dfs(port, len(components))

    mark_to_ports = defaultdict(list)
    for port, m in marks.items():
        mark_to_ports[m].append(port)

    pprint(mark_to_ports)
    potential = [ (i+1, port) for i, port in enumerate(components) if i+1 in mark_to_ports ]
    return len(potential)


