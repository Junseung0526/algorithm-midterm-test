import heapq

# [중간고사 대비] 그래프 탐욕 알고리즘 시각화 및 테스트 세트

def kruskal_visualizer(n, edges):
    """크루스칼 알고리즘 시각화"""
    print("\n[Kruskal's MST 과정]")
    # 1. 간선 정렬
    edges.sort(key=lambda x: x[2])
    print(f"정렬된 간선: {edges}")
    
    parent = [i for i in range(n + 1)]
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b: parent[b] = a
        else: parent[a] = b

    total_cost = 0
    mst_edges = []
    step = 1
    
    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        print(f"Step {step}: {u}-{v} 간선 검사 (가중치 {w})")
        if root_u != root_v:
            union(parent, u, v)
            total_cost += w
            mst_edges.append((u, v, w))
            print(f"  => [선택] 사이클 없음. 현재 비용: {total_cost}")
        else:
            print(f"  => [제외] 사이클 발생!")
        step += 1
    return total_cost, mst_edges

def dijkstra_visualizer(graph, start):
    """다익스트라 알고리즘 시각화"""
    print(f"\n[Dijkstra 최단 경로 과정 (출발: {start})]")
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    step = 1
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if distances[current_node] < current_dist:
            continue
            
        print(f"Step {step}: 현재 확정 노드 [{current_node}], 거리: {current_dist}")
        
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                print(f"  => {neighbor} 노드 갱신: {distance}")
        step += 1
    return distances

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    # 1. 크루스칼 MST 테스트
    # 정점: 1~5
    # 간선: (u, v, weight)
    k_edges = [(1, 2, 5), (1, 3, 4), (2, 3, 2), (2, 4, 7), (3, 4, 6), (4, 5, 3)]
    kruskal_visualizer(5, k_edges)

    # 2. 다익스트라 최단 경로 테스트
    d_graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'C': 1, 'D': 4},
        'C': {'D': 2},
        'D': {}
    }
    dijkstra_visualizer(d_graph, 'A')

if __name__ == "__main__":
    print("=== 그래프 탐욕 알고리즘(MST, Dijkstra) 시각화 도구 ===")
    run_tests()
