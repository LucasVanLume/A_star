import heapq
'''
Código feito pelos alunos:
    João Victor Pereira Silvestre Cavalcanti
    Jorge Francisco de Lima Júnior
    Lucas Van-Lume Lima
'''
# Para realizar testes modifique as variaveis start e end nas linhas 
# 169 e 170 para as estações desejadas

def a_star(start, end, real_distances, heuristic_distances, line_stations):
    # Inicialização da fila de prioridade heap
    heap = [(0, start, [])]
    # Inicialização do conjunto de nós visitados
    visited = set()
    # Inicialização dos scores de "g" para todos os nós como infinito
    g_scores = {node: float('inf') for node in real_distances.keys()}
    g_scores[start] = 0
    # Variável que armazena o tempo de baldeação
    transfer_time = 0
    iteracoes = 0
    
    # Loop principal para busca do caminho
    while heap:
        # Obtém o nó com o menor score "f" (soma de "g" e heurística) da fila de prioridade
        (f_score, current, path) = heapq.heappop(heap)
        # Verifica se o nó já foi visitado
        aux_menor = heapq.nsmallest(1,heap)
        if (current in visited) and (f_score > aux_menor[0][0]):
            continue      
        iteracoes += 1
        # Armazana o f_score do nó atual
        f_score_current = f_score
        # Marca o nó como visitado
        if current not in visited:
            visited.add(current)
        # Adiciona o nó ao caminho
        path = path + [current]        
        # Verifica a linha atual percorrida entre as duas últimas estações do caminho
        if len(path) >= 2:
            station = path[-2]
            common_line = set(line_stations[station]).intersection(line_stations[current])
        # Verifica todos os vizinhos do nó atual
        for neighbor in real_distances[current].keys():
            # Verifica se o vizinho já foi visitado
            if neighbor in visited:
                continue
            # Verifica se a estação atual e sua vizinha compartilham a linha atual
            if len(path) >= 2:
                if common_line == set(line_stations[current]).intersection(line_stations[neighbor]):
                    transfer_time = 0
                else:
                    transfer_time = 4
            # Calcula o score "g" para o vizinho
            tentative_g_score = g_scores[current] + real_distances[current][neighbor] / 30 + transfer_time / 60
            # Atualiza o score "g" para o vizinho
            g_scores[neighbor] = tentative_g_score
            # Calcula o score "f" (soma de "g" e heurística) para o vizinho
            f_score = g_scores[neighbor] + heuristic_distances[int(neighbor[1:])-1][int(end[1:])-1] / 30 #km/h
            # Adiciona o vizinho à fila de prioridade
            heapq.heappush(heap, (f_score, neighbor, path))
        
        
        menor = heapq.nsmallest(1,heap)
        # Verifica se o nó é o destino
        if current == end:
            if (menor[0][0] > f_score_current):
                break
            else:
                heapq.heappush(heap,(f_score_current,current,path))
        
        # Printando as fronteiras
        front_heap = list(heap)
        front = []
        front_dist = []
        
        for neigh in front_heap:
            front.append(neigh[1])
            front_dist.append(neigh[0])
        
        print("Fronteira de ", current,": ", end="")
        for qt_neigh in range(len(front)):
            print(front[qt_neigh], f", {front_dist[qt_neigh]:.2f} || ", end="")
            
        print("")
    
    
    # Cálculo da distância
    distance = 0
    for i in range(len(path) - 1):
        distance += real_distances[path[i]][path[i + 1]]
    # Retorna as linhas percorridas entre cada estação do caminho
    lines_traversed = []
    for i in range(len(path) - 1):
        station = path[i]
        next_station = path[i + 1]
        common_lines = set(line_stations[station]).intersection(line_stations[next_station])
        for line in common_lines:
            lines_traversed.append(line)
    # Calcula o número de baldeações e o tempo do caminho
    contador = 0
    for i in range(len(lines_traversed) - 1):
        if lines_traversed[i] != lines_traversed[i + 1]:
            contador += 1
    #time = distance / 30 + contador * 4 / 60
    
    minutes = (distance / 30 + contador * 4 /60) * 60 #time
    minutes, seconds = divmod(minutes * 60, 60)
    hours, minutes = divmod(minutes, 60)
    time = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
    
    

    return path, distance, time, lines_traversed, contador
    
##################################//#//###################################

line_stations = {
    'E1': {'blue'},
    'E2': {'blue', 'yellow'},
    'E3': {'blue', 'red'},
    'E4': {'blue', 'green'},
    'E5': {'blue', 'yellow'},
    'E6': {'blue'},
    'E7': {'yellow'},
    'E8': {'yellow', 'green'},
    'E9': {'yellow', 'red'},
    'E10': {'yellow'},
    'E11': {'red'},
    'E12': {'green'},
    'E13': {'green', 'red'},
    'E14': {'green'}
}

real_distances = {
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

start = "E1"
end = "E5"

path, distance, time, lines_traversed, contador = a_star(start, end, real_distances, heuristic_distances, line_stations)
print("\n")
print("Caminho:", " -> ".join(path))
print("Linhas:", " -> ".join(lines_traversed))
print("Distancia:", distance, "km")
print("Tempo:", time, "horas")
print("Baldeacoes:", contador)
