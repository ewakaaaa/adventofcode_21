def make_costs_table(graph,start):
    inf = float("inf")
    costs = {}
    for node in graph.keys():
        if node != start:
            if node in graph[start].keys():
                costs[node] = graph[start][node]
            else:
                costs[node] = inf
    return costs


def make_parents_table(graph,start):
    parents = {}
    for node in graph.keys():
        if node != start:
            if node in graph[start].keys():
                parents[node] = start
            else:
                parents[node] = None
    return parents


def find_the_cheapest_node(costs, processed):
    min_value = float('inf')
    for k, v in costs.items():
        if k not in processed:
            if costs[k] < min_value:
                min_value = costs[k]
                cheapest_node = k
    return cheapest_node, min_value


def find_path(parents,start,meta):
    path = [meta]
    key = parents[meta]
    path.append(key)
    while parents[key] != start:
        path.append(parents[key])
        key = parents[key]
    path.append(start)
    path.reverse()
    return path


def dijksta(graph,start,meta):
    costs = make_costs_table(graph,start)
    parents = make_parents_table(graph,start)
    processed = set()

    while len(processed) < len(costs.keys()):
        cheapest_node, road_cost = find_the_cheapest_node(costs, processed)
        for neighbor in graph[cheapest_node].keys():
            new_road_cost = road_cost + graph[cheapest_node][neighbor]
            if costs[neighbor] > new_road_cost:
                costs[neighbor] = new_road_cost
                parents[neighbor] = cheapest_node
        processed.add(cheapest_node)
        print(len(processed), len(costs.keys()))
    return costs[meta]

