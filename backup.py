
def is_member(element, lst):
    """
    Check if an element is a member of the list.

    Parameters:
    - element: the element to check
    - lst: the list to search in

    Returns:
    - True if the element is found in the list, False otherwise.
    """
    return any(map(lambda x: x == element, lst))

def remove_if(predicate, lst):
    """
    Remove elements from the list based on the given predicate.

    Parameters:
    - predicate: the function to determine whether to remove an element
    - lst: the list to filter

    Returns:
    - A new list containing elements that do not satisfy the predicate.
    """
    return list(filter(lambda x: not predicate(x), lst))

def extend_path(path, graph):
    """
    Extend the given path in the graph.

    Parameters:
    - path: the path to extend
    - graph: the graph containing nodes and their neighbors

    Returns:
    - A list of neighbors of the last node in the path that are not already in the path.
    """
    current_node = path[0]
    neighbors_of_current_node = graph[current_node]

    return list(filter(lambda x: not is_member(x, path), neighbors_of_current_node))

def depth_first_search(start, end, graph):
    """
    Perform a depth-first search from start to end in the graph.

    Parameters:
    - start: the starting node
    - end: the target node
    - graph: the graph containing nodes and their neighbors

    Returns:
    - A list representing a path from start to end in the graph, or an empty list if no path is found.
    """
    return dfs_aux(end, [[start]], graph)

def dfs_aux(end, paths, graph):
    """
    Auxiliary function for depth-first search.

    Parameters:
    - end: the target node
    - paths: a list of paths to explore
    - graph: the graph containing nodes and their neighbors

    Returns:
    - A list representing a path from start to end in the graph, or an empty list if no path is found.
    """
    if not paths:
        return []
    if end == paths[0][0]:
        return [list(reversed(paths[0]))] + dfs_aux(end, paths[1:] + list(map(lambda x: [x] + paths[0], extend_path(paths[0], graph))), graph)
    else:
        return dfs_aux(end, paths[1:] + list(map(lambda x: [x] + paths[0], extend_path(paths[0], graph))), graph)



# Función extend_path utilizada en la versión original para extender caminos
'''def extend_path(node, graph):
    """
    Extend a path by one step in a graph.

    Parameters:
    - node: the node to extend the path from
    - graph: the graph containing nodes and their neighbors

    Returns:
    - A list of neighbors of the given node.
    """
    return graph[node]'''

def create_graph(rows, columns):
    """
    Create a graph based on the given number of rows and columns.

    Parameters:
    - rows: the number of rows
    - columns: the number of columns

    Returns:
    - A dictionary representing the graph.
    """
    graph = {}
    for i in range(rows):
        for j in range(columns):
            node = (i, j)
            neighbors = find_neighbors(node, rows, columns)
            graph[node] = neighbors
    return graph

def find_neighbors(node, rows, columns):
    """
    Find neighbors of a node in the graph.

    Parameters:
    - node: the node to find neighbors for

    Returns:
    - A list of neighboring nodes of the given node.
    """
    x, y = node
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []
    for dx, dy in movements:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < columns:
            neighbors.append((nx, ny))
    return neighbors

# Create the graph
rows = 18
columns = 20
graph = create_graph(rows, columns)
#print(graph)
# Perform depth-first search
result = depth_first_search((0, 0), (2,3), graph)
print(result)
for i in result:
    print(i)
