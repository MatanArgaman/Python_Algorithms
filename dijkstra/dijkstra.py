def dijkstra(graph, source):
    """
    :param graph: dictionary: key: node, value: [[node, distance], [node, distance],....] - list of all neighbor nodes and their distance from the key node
    :param source: source node
    :return: dictionary: key: node, value: distance from source node

    Note: node must be a hashable object
    """

    import heapq
    import numpy as np

    unvisited = set(graph.keys())
    visited = {}  # dict of: key-node, value:distance from source node
    for k in unvisited:
        visited[k] = np.inf
    visited[source] = 0
    unvisited.remove(source)

    node = source
    unvisited_priority_queue = []
    while True:
        for nei_node, dist in graph[node]:
            new_distance = visited[node] + dist
            if new_distance < visited[nei_node]:
                visited[nei_node] = new_distance
                if nei_node in unvisited:
                    heapq.heappush(unvisited_priority_queue, (new_distance, nei_node))
        while (node not in unvisited) and unvisited_priority_queue:
            node = unvisited_priority_queue.pop()[1]
        if node not in unvisited:
            break
        unvisited.remove(node)
    return visited
