# 매 순간마다 그 당시 가장 좋다고 생각되는 것을 선택
# 이 방식이 전체적으로 최적의 해답이 되길 바라는 것
# 하지만 모든 문제에서 통하는 것은 아니기에
# 지금의 최선이 나중에도 최선인가? 를 판단하는게 핵심

def greedy(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            total_value += fraction * value
            break

    return total_value


items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print(f"그리디 배낭 결과: {greedy(capacity, items)}")
