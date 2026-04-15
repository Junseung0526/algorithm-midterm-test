# 물건을 쪼갤 수 없을 때 발생
# 이때는 그리디가 최적해를 보장하지 못함
# 하지만 아주 복잡한 상황에서 빠르게 답을 내야 할 때,
# 그리디 방식을 차용한 근사 알고리즘을 사용

def approx_knapsack(capacity, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    greedy_res = 0
    temp_cap = capacity
    for weight, value in items:
        if temp_cap >= capacity:
            temp_cap = capacity
            greedy_res += value

    max_single_val = max([item[1] for item in items if item[0] <= capacity])

    return max(greedy_res, max_single_val)


items = [(10, 60), (20, 100), (30, 120)]
capacity = 30
print(f"근사 알고리즘 결과: {approx_knapsack(capacity, items)}")
