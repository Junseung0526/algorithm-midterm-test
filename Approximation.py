# [근사(Approximation) 알고리즘]
# 복잡한 문제(NP-Hard)의 최적해를 구하기 힘들어, 
# '충분히 좋은 해'를 다항 시간 내에 찾는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. P vs NP 문제: 최적해를 찾는 데 지수 시간이 걸리는 NP-Hard 문제들이 대상임.
# 2. 다항 시간 해결: 정확한 답은 못 내도 시간 복잡도가 효율적이어야 함.
# 3. 근사 비율(Approximation Ratio): 최적해와 얼마나 차이 나는지 나타내는 척도.
# 4. 목적: 시간 내에 최선의 선택을 하기 위함임 (최적화 문제에서 유용).

def approx_knapsack(capacity, items):
    # 알고리즘 진행: 1. 가성비(단위 무게당 가치) 순으로 정렬
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    greedy_res = 0
    temp_cap = capacity
    # 알고리즘 진행: 2. 순서대로 넣을 수 있는 만큼 다 넣음 (그리디 방식)
    for weight, value in items:
        if temp_cap >= weight:
            temp_cap -= weight
            greedy_res += value

    # 알고리즘 진행: 3. 가장 가치가 큰 단일 품목 선택 (무게 제한 내)
    max_single_val = max([item[1] for item in items if item[0] <= capacity])

    # 알고리즘 진행: 4. '그리디 해'와 '가장 큰 단일 품목' 중 더 큰 것을 선택 (1/2-근사 알고리즘의 핵심 로직)
    return max(greedy_res, max_single_val)

items = [(10, 60), (20, 100), (30, 120)]
capacity = 30
print(f"근사 알고리즘 결과: {approx_knapsack(capacity, items)}")
