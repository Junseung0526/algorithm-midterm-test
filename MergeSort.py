# 분할 정복 알고리즘

# 분할(Divide): 해결하기 어려운 문제를 동일한 유형의 더 작은 부분 문제들로 나눕니다.
# 정복(Conquer): 나눈 부분 문제들을 재귀적으로 해결합니다. (문제가 충분히 작아지면 직접 해결)
# 결합(Combine): 부분 문제의 정답들을 합쳐서 원래 문제의 정답을 만듭니다

# 대표적인 예시: 합병 정렬
# 데이터가 무작위로 섞여 있을 때, 이를 반으로 계속 쪼갠 뒤 다시 합치면서 정렬하는 방식

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
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
print(f"정렬 결과: {merge_sort(data)}")
