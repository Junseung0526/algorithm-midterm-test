# [탐욕(Greedy) 알고리즘 - 기초]
# 매 순간 최적의 선택을 하여 전체 최적해를 찾는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. 탐욕 선택 속성(Greedy Choice Property): 현재의 선택이 나중의 선택에 영향을 주지 않음.
# 2. 최적 부분 구조(Optimal Substructure): 부분 문제의 최적해가 전체 문제의 최적해가 됨.
# 3. 배낭 문제 주의: '분할 가능(Fractional)'일 때만 탐욕 알고리즘으로 최적해 보장!
#    (0/1 배낭 문제는 DP로 풀어야 함)

def fractional_knapsack(capacity, items):
    # 알고리즘 진행: 1. 단위 무게당 가치(가성비) 계산 및 내림차순 정렬
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0
    # 알고리즘 진행: 2. 가성비가 높은 순서대로 배낭에 담기
    for value, weight in items:
        if capacity >= weight:
            # 알고리즘 진행: 3. 물건을 통째로 넣을 수 있는 경우
            total_value += value
            capacity -= weight
        else:
            # 알고리즘 진행: 4. 남은 용량만큼 물건을 쪼개서 넣기 (Greedy의 핵심)
            fraction = capacity / weight
            total_value += value * fraction
            break
            
    return total_value

def job_scheduling(jobs):
    # 알고리즘 진행: 1. 작업 이익(Profit) 기준으로 내림차순 정렬
    jobs.sort(key=lambda x: x[2], reverse=True)

    # 알고리즘 진행: 2. 전체 작업 중 가장 늦은 마감시간 확인하여 스케줄 공간 확보
    max_deadline = max(job[1] for job in jobs)
    schedule = [None] * (max_deadline + 1)
    total_profit = 0

    # 알고리즘 진행: 3. 이익이 큰 작업부터 마감일 이전에 '가장 늦은' 빈 시간에 배치
    # (일찍 배치하면 다른 작업의 기회를 뺏을 수 있기 때문!)
    for name, deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if schedule[t] is None:
                schedule[t] = name
                total_profit += profit
                break

    # 알고리즘 진행: 4. 최종 확정된 스케줄 결과 반환
    result_schedule = {t: name for t, name in enumerate(schedule) if name}
    return total_profit, result_schedule

if __name__ == "__main__":
    # [예제 1] Fractional Knapsack
    item_data = [(60, 10), (100, 20), (120, 30)]
    max_capacity = 50
    print(f"1. 배낭 문제 결과: {fractional_knapsack(max_capacity, item_data)}")

    # [예제 2] Job Scheduling
    freelance_jobs = [('A', 4, 20), ('B', 1, 10), ('C', 1, 40), ('D', 1, 30)]
    profit, schedule = job_scheduling(freelance_jobs)
    print(f"2. 작업 스케줄링 결과: 총 수익 {profit}, 스케줄 {schedule}")
