# [탐욕(Greedy) 알고리즘 - 응용]
# 허프만 코딩, 집합 커버 등 탐욕 기법을 활용한 실무적 문제 해결

# [시험 꿀팁! - 핵심 추가]
# 1. 허프만 코딩: 빈도가 낮은 문자부터 결합하여 '최적 이진 트리'를 구성하는 방식.
# 2. 접두어 코드(Prefix Code): 어떤 부호도 다른 부호의 시작 부분이 되지 않아 해석 시 모호함이 없음.
# 3. 집합 커버 문제: 최적해를 찾기 어려운 NP-완전 문제이므로 그리디로 '근사해'를 구함.

import heapq
from collections import Counter

# --- 1. Huffman Coding ---
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # 알고리즘 진행: 1. 문자의 빈도수 계산
    counter = Counter(text)
    
    # 알고리즘 진행: 2. 빈도수 기준 우선순위 큐(Heap) 생성
    priority_queue = [Node(char, freq) for char, freq in counter.items()]
    heapq.heapify(priority_queue)

    # 알고리즘 진행: 3. 가장 빈도가 낮은 두 노드를 꺼내 부모 노드로 합치기 반복
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # 빈도수의 합을 가진 새 부모 노드 생성
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    # 알고리즘 진행: 4. 최종 완성된 허프만 트리의 루트 노드 반환
    return priority_queue[0] if priority_queue else None

def generate_codes(node, current_code, huffman_codes):
    # 알고리즘 진행: 5. 트리를 순회하며 왼쪽은 0, 오른쪽은 1 부여 (가변 길이 코드)
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)
    return huffman_codes

# --- 2. Set Cover ---
def set_cover(universe, subsets):
    # 알고리즘 진행: 1. 커버해야 할 전체 원소 집합 설정
    elements_to_cover = set(universe)
    selected_subsets = []

    # 알고리즘 진행: 2. 모든 원소가 커버될 때까지 반복
    while elements_to_cover:
        best_subset = None
        covered_by_best = set()

        # 알고리즘 진행: 3. 아직 커버되지 않은 원소를 '가장 많이' 포함하는 부분집합 선택
        for name, subset in subsets.items():
            intersection = elements_to_cover & subset
            if len(intersection) > len(covered_by_best):
                best_subset = name
                covered_by_best = intersection

        if best_subset is None:
            break

        # 알고리즘 진행: 4. 선택된 부분집합을 목록에 추가하고 커버된 원소 제거
        selected_subsets.append(best_subset)
        elements_to_cover -= covered_by_best

    return selected_subsets

if __name__ == "__main__":
    # [예제 1] Huffman Coding
    text_data = "BCAADDDCCACACAC"
    root_node = build_huffman_tree(text_data)
    codes = generate_codes(root_node, "", {})
    print(f"1. 허프만 코딩 결과: {codes}")

    # [예제 2] Set Cover
    universe_set = {1, 2, 3, 4, 5, 6, 7, 8}
    subset_data = {
        'S1': {1, 2, 3},
        'S2': {2, 4, 5, 6},
        'S3': {1, 3, 5, 7, 8},
        'S4': {2, 4},
        'S5': {6, 8}
    }
    selected = set_cover(universe_set, subset_data)
    print(f"2. 집합 커버 결과: {selected}")
