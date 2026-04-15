# [분기 한정(Branch and Bound) 알고리즘]
# 탐색 도중 한정 함수(Bound Function)를 사용하여 최적해를 구하는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. 탐색 방식의 차이: 백트래킹은 주로 DFS(깊이 우선)를 쓰지만, 
#    분기 한정은 BFS(너비 우선)나 우선순위 큐(Best-First)를 사용하는 것이 핵심!
# 2. 한정(Bounding): 유망하지 않은 마디(Node)를 잘라내어 탐색 효율을 극대화함.
# 3. 최적화 문제: 주로 최대/최소값을 찾는 문제(0/1 Knapsack 등)에 사용됨.

from queue import PriorityQueue

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
    
    def __lt__(self, other):
        # 알고리즘 진행: 1. Best-First 탐색 (가장 가망 있는 노드부터 처리)
        return self.bound > other.bound

def get_bound(node, n, W, items):
    # 알고리즘 진행: 2. 현재 상태에서 얻을 수 있는 최대 기대치(Bound) 계산
    if node.weight >= W:
        return 0
    
    profit_bound = node.value
    j = node.level + 1
    total_weight = node.weight
    
    while j < n and total_weight + items[j][0] <= W:
        total_weight += items[j][0]
        profit_bound += items[j][1]
        j += 1
    
    if j < n:
        profit_bound += (W - total_weight) * items[j][1] / items[j][0]
        
    return profit_bound

def knapsack_bb(W, items):
    # 가성비순 정렬 (한정 함수를 위해 필수!)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    pq = PriorityQueue()
    
    root = Node(-1, 0, 0, 0)
    root.bound = get_bound(root, n, W, items)
    pq.put(root)
    
    max_profit = 0
    while not pq.empty():
        u = pq.get() # 가망성 높은 노드 우선 탐색 (BFS/Best-First)
        
        # 알고리즘 진행: 3. 유망한 경우에만(현재 최고 이익보다 Bound가 클 때) 자식 탐색
        if u.bound > max_profit:
            # 왼쪽 자식: 포함하는 경우
            v_inc = Node(u.level + 1, u.value + items[u.level + 1][1], u.weight + items[u.level + 1][0], 0)
            if v_inc.weight <= W and v_inc.value > max_profit:
                max_profit = v_inc.value
            
            v_inc.bound = get_bound(v_inc, n, W, items)
            if v_inc.bound > max_profit:
                pq.put(v_inc)
                
            # 오른쪽 자식: 포함하지 않는 경우
            v_exc = Node(u.level + 1, u.value, u.weight, 0)
            v_exc.bound = get_bound(v_exc, n, W, items)
            if v_exc.bound > max_profit:
                pq.put(v_exc)
                
    return max_profit

W = 10
items = [(2, 40), (5, 30), (10, 50), (5, 10)]
print(f"분기 한정 배낭 문제 최적값: {knapsack_bb(W, items)}")
