import heapq

def astar(graph, start, end):
    # Initialize the f_score dictionary with all nodes set to infinity
    f_score = {node: float('inf') for node in range(len(graph))}
    f_score[start] = heuristic(start, end)

    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == end:
            break

        for neighbor, distance in enumerate(graph[current]):
            if distance is None:
                continue

            new_cost = cost_so_far[current] + distance
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    path = [end]
    while path[-1] != start:
        try:
            path.append(came_from[path[-1]])
        except:
            break

    path.reverse()

    try:
        return cost_so_far[end], path
    except:
        cost_so_far[end], path = 0, 0
        return cost_so_far[end], path

def heuristic(a, b):
    return abs(a - b)