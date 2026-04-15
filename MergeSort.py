# [분할 정복(Divide and Conquer) 알고리즘]
# 분할(Divide): 문제를 동일한 유형의 더 작은 부분 문제들로 나눔.
# 정복(Conquer): 나눈 부분 문제들을 재귀적으로 해결.
# 결합(Combine): 부분 문제의 정답들을 합쳐서 원래 문제의 정답을 만듦.

# [시험 꿀팁! - 핵심 추가]
# 1. 시간 복잡도: 언제나 O(n log n)으로 일정함 (최악, 평균, 최선 동일).
# 2. 공간 복잡도: 합병 과정에서 임시 배열이 필요하여 O(n)의 추가 공간이 필요함 (강조!).
# 3. 분할 정복이 '부적절한 경우': 피보나치 수열처럼 분할할수록 문제의 크기가 커지는 경우 
#    (F(n) = F(n-1) + F(n-2))에는 분할 정복보다 동적 계획법(DP)이 훨씬 효율적임.

def merge_sort(arr):
    # 알고리즘 진행: 1. 리스트 크기가 1 이하가 될 때까지 반으로 계속 쪼갬 (Divide)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 알고리즘 진행: 2. 쪼개진 부분들을 정렬하면서 다시 합침 (Conquer & Combine)
    return merge(left, right)

def merge(left, right):
    result = [] # 알고리즘 진행: 3. O(n)의 추가 공간(임시 배열) 사용
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [38, 27, 43, 3, 9, 82, 10]
print(f"합병 정렬 결과: {merge_sort(data)}")
