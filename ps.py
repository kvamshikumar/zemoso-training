import heapq

def dijkstra(graph, start, end):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return dist

        for neighbor, cost in graph[current_node].items():
            new_cost = distance[current_node] + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return -1

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'A':10,'D': 2, 'E': 1},
    'C': {'A':3,'B': 4, 'F': 2},
    'D': {'B':2,'E': 7},
    'E': {'B':1,'D': 7, 'F': 6},
    'F': {'C':2,'E':6,'G': 1},
    'G': {'F':1}
}

start = input("start: ")
end = input("destination: ")

shortest_distance = dijkstra(graph, start, end)

print(f"The shortest distance from {start} to {end} is {shortest_distance}" if shortest_distance != -1 else f"There is no path from {start} to {end}")
