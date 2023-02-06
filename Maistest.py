import heapq

def search(start, end, distances, heuristics, subway_lines):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (time, node, path) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return (time, path)

        for (adjacent, time_adjacent) in distances[node].items():
            if adjacent in visited:
                continue
            subway_line = None
            for line, stations in subway_lines.items():
                if node in stations and adjacent in stations:
                    subway_line = line
                    break
            time_heuristic = heuristics[int(node[1:]) - 1][int(adjacent[1:]) - 1]
            if subway_line:
                heapq.heappush(heap, (time + time_adjacent + 4, adjacent, path))
            else:
                heapq.heappush(heap, (time + time_adjacent + time_heuristic, adjacent, path))
    return float("inf"), []

start = "E1"
end = "E10"

distances = {
    "E1": {"E2": 10},
    "E2": {"E1": 10, "E3": 8.5, "E9": 10, "E10": 3.5},
    "E3": {"E2": 8.5, "E4": 6.3, "E9": 9.4, "E13": 18.7},
    "E4": {"E3": 6.3, "E5": 13, "E8": 15.3, "E13": 12.8},
    "E5": {"E4": 13, "E6": 3, "E7": 2.4, "E8": 30},
    "E6": {"E5": 3},
    "E7": {"E5": 2.4},
    "E8": {"E4": 15.3, "E5": 30, "E9": 9.6, "E12": 6.4},
    "E9": {"E2": 10, "E3": 9.4, "E8": 9.6, "E11": 12.2},
    "E10": {"E2": 3.5},
    "E11": {"E9": 12.2},
    "E12": {"E8": 6.4},
    "E13": {"E3": 18.7, "E4": 12.8, "E14": 5.1},
    "E14": {"E13": 5.1}
    }

heuristics = [
        [0,    10,   18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8], # Estação E1
        [10,   0,    8.5,  14.8, 26.6, 29.1, 26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8], # Estação E2
        [18.5, 8.5,  0,    6.3,  18.2, 20.6, 17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6], # Estação E3
        [24.8, 14.8, 6.3,  0,    12,   14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], # Estação E4
        [36.4, 26.6, 18.2, 12,   0,    3,    2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], # Estação E5
        [38.8, 29.1, 20.6, 14.4, 3,    0,    3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], # Estação E6
        [35.8, 26.1, 17.6, 11.5, 2.4,  3.3,  0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6], # Estação E7
        [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6], # Estação E8
        [17.6, 10,   9.4,  12.6, 23.3, 25.7, 23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6], # Estação E9
        [9.1,  3.5,  10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2], # Estação E10
        [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5], # Estação E11
        [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6], # Estação E12
        [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1 ], # Estação E13
        [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0   ]  # Estação E14
    ]

subway_lines = {
    "blue": ["E1", "E2", "E3", "E4", "E5", "E6"],
    "yellow": ["E2", "E5", "E7", "E8", "E9", "E10"],
    "green": ["E4", "E8", "E12", "E13", "E14"],
    "red": ["E3", "E9", "E11", "E13"],
}

print(search(start, end, distances, heuristics, subway_lines))










'''import heapq

def a_star(start, end, real_distances, heuristic_distances):
    heap = [(0, start)]
    visited = set()
    g_scores = {node: float('inf') for node in real_distances.keys()}
    g_scores[start] = 0
    while heap:
        (f_score, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            break
        for neighbor in real_distances[current].keys():
            if neighbor in visited:
                continue
            tentative_g_score = g_scores[current] + real_distances[current][neighbor] / 30
            if tentative_g_score >= g_scores[neighbor]:
                continue
            g_scores[neighbor] = tentative_g_score
            f_score = g_scores[neighbor] + heuristic_distances[int(neighbor[1:])-1][int(end[1:])-1]
            heapq.heappush(heap, (f_score, neighbor))
    
    path = []
    current = end
    while current != start:
        path.append(current)
        for neighbor in real_distances[current].keys():
            if neighbor in visited and g_scores[neighbor] + real_distances[current][neighbor] / 30 == g_scores[current]:
                current = neighbor
                break
    path.append(start)
    path.reverse()
    
    distance = 0
    for i in range(len(path) - 1):
        distance += real_distances[path[i]][path[i + 1]]
    time = distance / 30
    
    return path, distance, time

real_distances = {
    1: {2: 10},
    2: {3: 8.5, 9: 10, 10: 3.5},
    3: {4: 6.3, 9: 9.4, 13: 18.7},
    4: {5: 13, 8: 15.3, 13: 12.8},
    5: {6: 3, 7: 2.4, 8: 30},
    8: {9: 9.6, 12: 6.4},
    9: {11: 12.2},
    13: {14: 5.1}
    }

heuristic_distances = [
        [0,    10,   18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8], # Estação E1
        [10,   0,    8.5,  14.8, 26.6, 29.1, 26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8], # Estação E2
        [18.5, 8.5,  0,    6.3,  18.2, 20.6, 17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6], # Estação E3
        [24.8, 14.8, 6.3,  0,    12,   14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], # Estação E4
        [36.4, 26.6, 18.2, 12,   0,    3,    2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], # Estação E5
        [38.8, 29.1, 20.6, 14.4, 3,    0,    3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], # Estação E6
        [35.8, 26.1, 17.6, 11.5, 2.4,  3.3,  0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6], # Estação E7
        [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6], # Estação E8
        [17.6, 10,   9.4,  12.6, 23.3, 25.7, 23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6], # Estação E9
        [9.1,  3.5,  10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2], # Estação E10
        [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5], # Estação E11
        [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6], # Estação E12
        [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1 ], # Estação E13
        [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0   ]  # Estação E14
    ]

line_stations = {
"E1": ["blue"],
"E2": ["blue", "yellow"],
"E3": ["blue", "red"],
"E4": ["blue", "green"],
"E5": ["blue", "yellow"],
"E6": ["blue"],
"E7": ["yellow"],
"E8": ["yellow", "green"],
"E9": ["yellow", "red"],
"E10": ["yellow"],
"E11": ["red"],
"E12": ["green"],
"E13": ["red", "green"],
"E14": ["green"]
}

start = "E1"
end = "E1"

def find_path(start, end, real_distances, heuristic_distances, line_stations):
    path, distance, time = a_star(start, end, real_distances, heuristic_distances)
    if not path:
        return None, None, None
    for i in range(len(path) - 1):
        if len(set(line_stations[path[i]]) & set(line_stations[path[i + 1]])) == 0:
            return None, None, None
    return path, distance, time

def transfer_path(start, end, real_distances, heuristic_distances, line_stations):
    source_station = start
    destination_station = end
    source_lines = line_stations[start]
    destination_lines = line_stations[end]
    transfer_station = None
    min_transfer_time = float('inf')
    transfer_stations = []
    for station, lines in line_stations.items():
        if len(set(lines) & set(source_lines)) and len(set(lines) & set(destination_lines)):
            path, distance, time = find_path(source_station, station, real_distances, heuristic_distances, line_stations)
            if not path:
                continue
            if time < min_transfer_time:
                transfer_station = station
                min_transfer_time = time
    if not transfer_station:
        return None, None, None
    path1, distance1, time1 = find_path(source_station, transfer_station, real_distances, heuristic_distances, line_stations)
    path2, distance2, time2 = find_path(transfer_station, destination_station, real_distances, heuristic_distances, line_stations)
    if not path1 or not path2:
        return None, None, None
    transfer_stations.append(transfer_station)
    return path1[:-1] + path2, distance1 + distance2, time1 + time2, transfer_stations

path, distance, time, transfer_stations = transfer_path(start, end, real_distances, heuristic_distances, line_stations)
if not path:
    print("Não foi possível encontrar uma rota")
else:
    print("Caminho:", path)
    print("Distância:", distance)
    print("Tempo:", time)
    print(transfer_stations)'''
