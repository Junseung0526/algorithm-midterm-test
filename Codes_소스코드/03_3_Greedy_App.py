import heapq
from collections import Counter

# [중간고사 대비] 탐욕 알고리즘 응용 시각화 및 테스트 세트

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_visualizer(text):
    """허프만 트리 생성 과정 시각화"""
    print(f"\n[Huffman Coding 과정] 입력 텍스트: {text}")
    counter = Counter(text)
    print(f"빈도수: {dict(counter)}")
    
    pq = [Node(char, freq) for char, freq in counter.items()]
    heapq.heapify(pq)
    
    step = 1
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        print(f"Step {step}: [{left.char if left.char else 'Node'}({left.freq})] + [{right.char if right.char else 'Node'}({right.freq})] => New Node({merged.freq})")
        heapq.heappush(pq, merged)
        step += 1
        
    root = pq[0]
    codes = {}
    def get_codes(node, current_code):
        if node is None: return
        if node.char:
            codes[node.char] = current_code
            return
        get_codes(node.left, current_code + "0")
        get_codes(node.right, current_code + "1")
        
    get_codes(root, "")
    return codes

def set_cover_visualizer(universe, subsets):
    """집합 커버 과정 시각화"""
    print(f"\n[Set Cover 과정] 전체 집합: {universe}")
    elements_to_cover = set(universe)
    selected = []
    
    step = 1
    while elements_to_cover:
        best_subset = None
        covered_by_best = set()
        
        for name, subset in subsets.items():
            intersection = elements_to_cover & subset
            if len(intersection) > len(covered_by_best):
                best_subset = name
                covered_by_best = intersection
        
        if not best_subset: break
        
        selected.append(best_subset)
        elements_to_cover -= covered_by_best
        print(f"Step {step}: {best_subset} 선택 (새로 커버된 원소: {covered_by_best})")
        print(f"  => 남은 원소: {elements_to_cover if elements_to_cover else '없음'}")
        step += 1
        
    return selected

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    # 1. 허프만 코딩
    codes = huffman_visualizer("AAAAAABCCD")
    print(f"\n최종 생성된 코드: {codes}")

    # 2. 집합 커버
    universe = {1, 2, 3, 4, 5, 6, 7, 8}
    subsets = {
        'S1': {1, 2, 3},
        'S2': {2, 4, 5, 6},
        'S3': {1, 3, 5, 7, 8},
        'S4': {2, 4},
        'S5': {6, 8}
    }
    set_cover_visualizer(universe, subsets)

if __name__ == "__main__":
    run_tests()
