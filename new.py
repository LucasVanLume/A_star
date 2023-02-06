import heapq

def a_star(start, end, real_distances, heuristic_distances, line_stations):
    # Inicialização da fila de prioridade heap
    heap = [(0, start)]
    # Inicialização do conjunto de nós visitados
    visited = set()
    # Inicialização dos scores de "g" para todos os nós como infinito
    g_scores = {node: float('inf') for node in real_distances.keys()}
    g_scores[start] = 0
    
    # Loop principal para busca de caminho
    while heap:
        # Obtém o nó com o menor score "f" (soma de "g" e heurística) da fila de prioridade
        (f_score, current) = heapq.heappop(heap)
        # Verifica se o nó já foi visitado
        if current in visited:
            continue
        # Marca o nó como visitado
        visited.add(current)
        # Verifica se o nó é o destino
        if current == end:
            break
        # Verifica todos os vizinhos do nó atual
        for neighbor in real_distances[current].keys():
            # Verifica se o vizinho já foi visitado
            if neighbor in visited:
                continue
            transfer_time = 0 ######################
            if set(line_stations[current]) & set(line_stations[neighbor]):
                transfer_time = 0
            else:
                transfer_time = 4 #################
            # Calcula o score "g" para o vizinho
            tentative_g_score = g_scores[current] + real_distances[current][neighbor] / 30 + transfer_time
            # Verifica se o score "g" calculado é maior que o score "g" atual do vizinho
            if tentative_g_score >= g_scores[neighbor]:
                continue
            # Atualiza o score "g" para o vizinho
            g_scores[neighbor] = tentative_g_score
            # Calcula o score "f" (soma de "g" e heurística) para o vizinho
            f_score = g_scores[neighbor] + heuristic_distances[int(neighbor[1:])-1][int(end[1:])-1]
            # Adiciona o vizinho à fila de prioridade
            heapq.heappush(heap, (f_score, neighbor))
    
    # Criação do caminho (do destino até o início)
    path = []
    current = end
    while current != start:
        path.append(current)
        for neighbor in real_distances[current].keys():
            if neighbor in visited and g_scores[neighbor] + real_distances[current][neighbor] / 30 + transfer_time == g_scores[current]:
                current = neighbor
                break
    path.append(start)
    path.reverse()
    
    # Cálculo da distância e do tempo de viagem
    distance = 0
    for i in range(len(path) - 1):
        distance += real_distances[path[i]][path[i + 1]]
    time = distance / 30 + (len(path) - 1) * transfer_time

    lines_traversed = set()
    for station in path:
        lines_traversed |= line_stations[station]

    return path, distance, time, lines_traversed

line_stations = {
    "E1": {"blue"},
    "E2": {"blue", "red"},
    "E3": {"yellow", "green"},
    "E4": {"blue", "green"},
    "E5": {"green"}
}

real_distances = {
    "E1": {"E2": 2, "E3": 5, "E4": 1},
    "E2": {"E1": 2, "E4": 3},
    "E3": {"E1": 5, "E4": 2, "E5": 5},
    "E4": {"E1": 1, "E2": 3, "E3": 2, "E5": 2},
    "E5": {"E3": 5, "E4": 2}
}

heuristic_distances = [
    [0, 4, 5, 2, 6],
    [4, 0, 7, 3, 7],
    [5, 7, 0, 4, 5],
    [2, 3, 4, 0, 4],
    [6, 7, 5, 4, 0]
]

start = "E4"
end = "E5"

path, distance, time, lines_traversed = a_star(start, end, real_distances, heuristic_distances, line_stations)
print("Caminho:", path)
print("Distância:", distance, "km")
print("Tempo:", time, "horas")
print(lines_traversed)






'''import heapq IMPORTANTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

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
    "E1": {"E2": 2, "E3": 5, "E4": 1},
    "E2": {"E1": 2, "E4": 3},
    "E3": {"E1": 5, "E4": 2, "E5": 5},
    "E4": {"E1": 1, "E2": 3, "E3": 2, "E5": 2},
    "E5": {"E3": 5, "E4": 2}
}

heuristic_distances = [
    [0, 4, 5, 2, 6],
    [4, 0, 7, 3, 7],
    [5, 7, 0, 4, 5],
    [2, 3, 4, 0, 4],
    [6, 7, 5, 4, 0]
]

start = "E1"
end = "E5"

path, distance, time = a_star(start, end, real_distances, heuristic_distances)
print("Caminho:", path)
print("Distância:", distance, "km")
print("Tempo:", time, "horas")
'''









'''import heapq

def a_star(start, end, real_distances, heuristic_distances):
    heap = [(0, start)]
    visited = set()
    came_from = {}
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            break
        for neighbor in real_distances[current].keys():
            if neighbor in visited:
                continue
            new_cost = cost + real_distances[current][neighbor]
            heapq.heappush(heap, (new_cost + heuristic_distances[int(current[1:])-1][int(neighbor[1:])-1], neighbor))
            came_from[neighbor] = current
    
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    distance = 0
    for i in range(len(path) - 1):
        distance += real_distances[path[i]][path[i + 1]]
    time = distance / 30
    
    return path, distance, time

real_distances = {
    "E1": {"E2": 2, "E3": 5, "E4": 1},
    "E2": {"E1": 2, "E4": 3},
    "E3": {"E1": 5, "E4": 2, "E5": 5},
    "E4": {"E1": 1, "E2": 3, "E3": 2, "E5": 2},
    "E5": {"E3": 5, "E4": 2}
}

heuristic_distances = [
    [0, 4, 5, 2, 6],
    [4, 0, 7, 3, 7],
    [5, 7, 0, 4, 5],
    [2, 3, 4, 0, 4],
    [6, 7, 5, 4, 0]
]

start = "E1"
end = "E2"

path, distance, time = a_star(start, end, real_distances, heuristic_distances)
print("Caminho:", path)
print("Distância:", distance, "km")
print("Tempo:", time, "horas")'''









'''import heapq

def a_star(start, end, real_distances, heuristic_distances):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            break
        for neighbor in real_distances[current].keys():
            if neighbor in visited:
                continue
            total_cost = cost + real_distances[current][neighbor]
            heapq.heappush(heap, (total_cost + heuristic_distances[int(current[1:])-1][int(neighbor[1:])-1], neighbor))
    
    path = []
    current = end
    while current != start:
        path.append(current)
        for neighbor in real_distances[current].keys():
            if neighbor in visited and total_cost == cost + real_distances[current][neighbor]:
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
    "E1": {"E2": 2, "E3": 5, "E4": 1},
    "E2": {"E1": 2, "E4": 3},
    "E3": {"E1": 5, "E4": 2, "E5": 5},
    "E4": {"E1": 1, "E2": 3, "E3": 2, "E5": 2},
    "E5": {"E3": 5, "E4": 2}
}

heuristic_distances = [
    [0, 4, 5, 2, 6],
    [4, 0, 7, 3, 7],
    [5, 7, 0, 4, 5],
    [2, 3, 4, 0, 4],
    [6, 7, 5, 4, 0]
]

start = "E1"
end = "E4"

path, distance, time = a_star(start, end, real_distances, heuristic_distances)
print("Caminho:", path)
print("Distância:", distance, "km")
print("Tempo:", time, "horas")'''
