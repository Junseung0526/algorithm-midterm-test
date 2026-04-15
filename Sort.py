# [정렬(Sort) 알고리즘]
# 데이터를 특정한 기준에 따라 나열하는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. 퀵 정렬 시간 복잡도: 평균 O(n log n), 최악의 경우 O(n^2).
# 2. 최악의 경우 피하기: 피벗(Pivot)을 맨 앞/뒤가 아닌 '중앙값' 등으로 선택하여 
#    이미 정렬된 데이터에서도 균형 있게 분할하도록 전략을 짜야 함 (강조!).
# 3. 불안정 정렬(Unstable Sort): 동일한 값의 순서가 바뀔 수 있음.

def quick_sort(arr):
    # 알고리즘 진행: 1. 기저 조건 (리스트 크기가 1 이하)
    if len(arr) <= 1:
        return arr
    
    # 알고리즘 진행: 2. 피벗(Pivot) 선정 전략 (중앙값 선택으로 최악의 경우 방지!)
    pivot = arr[len(arr) // 2]
    
    # 알고리즘 진행: 3. 피벗 기준 분할 (Partition)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 알고리즘 진행: 4. 재귀적 정렬 및 결합
    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print(f"퀵 정렬 결과: {quick_sort(data)}")
