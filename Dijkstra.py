def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    previous_vertices = [-1] * n
    vertices = [i for i in range(n)]
    while vertices:
        curr_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(curr_vertex)
        if distances[curr_vertex] == float('inf'):
            break
        for neighbor, weight in enumerate(graph[curr_vertex]):
            if weight is not None:
                distance = distances[curr_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = curr_vertex
    path, curr_vertex = [], end
    while curr_vertex != -1:
        path.append(curr_vertex)
        curr_vertex = previous_vertices[curr_vertex]
    path.reverse()
    return distances[end], path
