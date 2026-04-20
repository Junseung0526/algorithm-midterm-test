# [탐욕(Greedy) 알고리즘 - 그래프]
# 그래프 내에서 최소 비용이나 최단 경로를 찾는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. MST(최소 신장 트리): 사이클이 없으면서 모든 정점을 연결하는 가중치 합이 최소인 트리.
# 2. 크루스칼 vs 프림: 간선이 적으면(희소 그래프) 크루스칼, 많으면(밀집 그래프) 프림이 유리!
# 3. 다익스트라 주의: 간선 가중치에 '음수'가 있으면 사용 불가 (벨만-포드 필요).

import heapq

# ---------------------------------------------------------
# [1] 크루스칼(Kruskal) 알고리즘 - 간선 중심
# ---------------------------------------------------------
# 시험 포인트: Union-Find 자료구조를 사용하여 사이클 발생 여부를 O(α(N))에 판별함.
# 간선 정렬 시간 O(E log E)이 전체 시간 복잡도를 지배함.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def kruskal(n, edges):
    # 알고리즘 진행: 1. 모든 간선을 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n + 1)]
    total_cost = 0
    mst = []

    # 알고리즘 진행: 2. 가중치가 낮은 간선부터 하나씩 확인
    for u, v, weight in edges:
        # 알고리즘 진행: 3. 사이클이 발생하지 않는 경우에만 집합에 포함 (Union-Find)
        if find_parent(parent, u) != find_parent(parent, v):
            union_parent(parent, u, v)
            total_cost += weight
            mst.append((u, v, weight))
            
    # 알고리즘 진행: 4. 최소 비용과 선택된 간선 리스트 반환
    return total_cost, mst

# ---------------------------------------------------------
# [2] 프림(Prim) 알고리즘 - 정점 중심
# ---------------------------------------------------------
# 시험 포인트: 임의의 시작점에서 확장해 나가는 방식.
# 우선순위 큐(Heap)를 사용하여 최적 간선을 추출하며 O(E log V)의 복잡도를 가짐.

def prim(start_node, graph_dict):
    mst = []
    visited = {start_node}
    edges = []
    
    # 알고리즘 진행: 1. 시작 노드와 연결된 모든 간선을 우선순위 큐에 삽입
    for next_node, weight in graph_dict[start_node]:
        heapq.heappush(edges, (weight, start_node, next_node))

    total_cost = 0
    # 알고리즘 진행: 2. 큐에서 가장 가중치가 낮은 간선부터 꺼내기
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        # 알고리즘 진행: 3. 방문하지 않은 정점과 연결된 경우에만 트리에 추가
        if v not in visited:
            visited.add(v)
            total_cost += weight
            mst.append((u, v, weight))
            
            # 알고리즘 진행: 4. 새로 추가된 정점에서 연결된 간선들을 큐에 갱신
            for next_node, next_weight in graph_dict[v]:
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, v, next_node))
                    
    return total_cost, mst

# ---------------------------------------------------------
# [3] 다익스트라(Dijkstra) 알고리즘 - 최단 경로
# ---------------------------------------------------------
# 시험 포인트: 특정 노드에서 다른 모든 노드로의 '최단 거리'를 구하는 탐욕법.
# 매 단계마다 '방문하지 않은 노드 중 최단 거리가 가장 짧은 노드'를 선택하는 것이 핵심!

def dijkstra(graph, start):
    # 알고리즘 진행: 1. 거리 테이블 초기화 (무한대) 및 시작 노드 거리 0 설정
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)] # (거리, 노드)

    while pq:
        # 알고리즘 진행: 2. 현재 가장 최단 거리인 노드를 우선순위 큐에서 추출
        current_dist, current_node = heapq.heappop(pq)
        
        # 알고리즘 진행: 3. 이미 처리된 노드(저장된 거리보다 큰 경우)는 건너뛰기
        if distances[current_node] < current_dist:
            continue
            
        # 알고리즘 진행: 4. 현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧으면 갱신
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# --- 실행 예제 ---
if __name__ == "__main__":
    # 크루스칼 예제
    edges_data = [(1, 2, 5), (1, 3, 4), (2, 3, 2), (2, 4, 7), (3, 4, 6), (4, 5, 3)]
    print(f"1. 크루스칼 MST: {kruskal(5, edges_data)}")

    # 프림 예제
    graph_data = {
        'A': [('B', 2), ('C', 5)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 5), ('B', 1), ('D', 2)],
        'D': [('B', 4), ('C', 2)]
    }
    print(f"2. 프림 MST: {prim('A', graph_data)}")

    # 다익스트라 예제
    dist_graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'C': 1, 'D': 4},
        'C': {'D': 2},
        'D': {}
    }
    print(f"3. 다익스트라 A출발: {dijkstra(dist_graph, 'A')}")
