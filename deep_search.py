from functools import reduce

def member(ele, lst):
    """
    Check if an element exists in a list.

    Args:
    ele: The element to check.
    lst: The list to search.

    Returns:
    True if the element exists in the list, otherwise False.
    """
    return any(filter(lambda x: x == ele, lst))

def remove_if(fun, lst):
    """
    Remove elements from a list based on a given condition.

    Args:
    fun: The condition function.
    lst: The list to filter.

    Returns:
    A new list with elements filtered out based on the condition.
    """
    return list(filter(lambda x: not fun(x), lst))


def neighbors(node, obstacles, end):
    """
    Find neighboring coordinates of a given node.

    Args:
    node: The current coordinate.
    obstacles: List of obstacle coordinates.
    end: The target coordinate.

    Returns:
    A list of neighboring coordinates sorted by their proximity to the target.
    """
    x, y = node
    neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_neighbours = list(filter(lambda coord: 0 <= coord[0] < 18 and 0 <= coord[1] < 20 and coord[0] >= 0 and coord[1] >= 0 and coord not in obstacles, neighbours))
    sorted_neighbours = sorted(valid_neighbours, key=lambda coord: abs(coord[0] - end[0]) + abs(coord[1] - end[1]))
    return sorted_neighbours

def extend(path, obstacles, visited, end):
    """
    Extend a path to neighboring coordinates.

    Args:
    path: The current path.
    obstacles: List of obstacle coordinates.
    visited: Set of visited coordinates.
    end: The target coordinate.

    Returns:
    A list of extended paths.
    """
    return remove_if(lambda x: member(x, path) or member(x, visited), neighbors(path[-1], obstacles, end))

def depth_first_search(start, end, obstacles):
    """
    Perform depth-first search to find a path from start to end.

    Args:
    start: The starting coordinate.
    end: The target coordinate.
    obstacles: List of obstacle coordinates.

    Returns:
    The path from start to end if found, otherwise None.
    """
    return depth_first_search_aux(end, [(start,)], obstacles, set())

def depth_first_search_aux(end, paths, obstacles, visited):
    """
    Auxiliary function for depth-first search.

    Args:
    end: The target coordinate.
    paths: List of current paths.
    obstacles: List of obstacle coordinates.
    visited: Set of visited coordinates.

    Returns:
    The path from start to end if found, otherwise None.
    """
    if not paths:
        return None  # No valid path found
    elif end == paths[0][-1]:
        return list(reversed(paths[0]))  # Found a valid path
    else:
        new_paths = reduce(lambda acc, path: acc + [path + (neighbor,) for neighbor in extend(path, obstacles, visited, end)], paths, [])
        if not new_paths:
            return None  # No new paths available
        new_visited = visited.union(reduce(lambda acc, path: acc.union({path[-1]}), new_paths, set()))
        best_path = min(new_paths, key=lambda path: sum(map(lambda coord: abs(coord[0] - end[0]) + abs(coord[1] - end[1]), path)))
        return depth_first_search_aux(end, [best_path], obstacles, new_visited)
