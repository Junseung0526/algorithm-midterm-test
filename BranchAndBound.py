# 분기 한정(Branch and Bound) 알고리즘
# 백트랙킹처럼 모든 가능한 해를 탐색하지만, 한정 함수(Bound Function)를 사용하여
# 탐색 중인 부분 해가 최적해보다 나빠질 것이 확실하면 탐색을 중지함
# 주로 최적화 문제(최대/최소값 찾기)를 풀 때 사용됨

from queue import PriorityQueue

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
    
    def __lt__(self, other):
        return self.bound > other.bound  # Max Priority Queue

def get_bound(node, n, W, items):
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
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    pq = PriorityQueue()
    
    root = Node(-1, 0, 0, 0)
    root.bound = get_bound(root, n, W, items)
    pq.put(root)
    
    max_profit = 0
    while not pq.empty():
        u = pq.get()
        
        if u.bound > max_profit:
            # Include next item
            v_inc = Node(u.level + 1, u.value + items[u.level + 1][1], u.weight + items[u.level + 1][0], 0)
            if v_inc.weight <= W and v_inc.value > max_profit:
                max_profit = v_inc.value
            
            v_inc.bound = get_bound(v_inc, n, W, items)
            if v_inc.bound > max_profit:
                pq.put(v_inc)
                
            # Exclude next item
            v_exc = Node(u.level + 1, u.value, u.weight, 0)
            v_exc.bound = get_bound(v_exc, n, W, items)
            if v_exc.bound > max_profit:
                pq.put(v_exc)
                
    return max_profit

W = 10
items = [(2, 40), (5, 30), (10, 50), (5, 10)] # (weight, value)
print(f"분기 한정 배낭 문제 최적값: {knapsack_bb(W, items)}")
