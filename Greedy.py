# [탐욕(Greedy) 알고리즘]
# 매 순간마다 그 당시 가장 좋다고 생각되는 것을 선택하여 전체 최적해를 구하려는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. 탐욕적 선택 속성(Greedy Choice Property): 앞의 선택이 이후의 선택에 영향을 주지 않아야 함.
# 2. 최적 부분 구조(Optimal Substructure): 부분 문제의 최적해가 전체 문제의 최적해가 됨.
# 3. 실사례: 허프만 코딩(데이터 압축), 다익스트라(최단 경로)가 대표적인 사례임 (강조!).
# 4. 배낭 문제 종류: Fractional(쪼개기 가능)은 그리디로 해결 가능하지만, 0/1(쪼개기 불가능)은 그리디가 최적해를 보장하지 못함.

def greedy(capacity, items):
    # 알고리즘 진행: 1. 가성비(단위 무게당 가치) 순으로 정렬
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    for weight, value in items:
        # 알고리즘 진행: 2. 배낭에 통째로 넣을 수 있으면 다 넣음 (탐욕적 선택)
        if capacity >= weight:
            capacity -= weight
            total_value += value
        # 알고리즘 진행: 3. 남은 무게가 부족하면 쪼개서 넣음 (가장 이득인 선택)
        else:
            fraction = capacity / weight
            total_value += fraction * value
            break

    return total_value

items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print(f"그리디 배낭 결과: {greedy(capacity, items)}")
