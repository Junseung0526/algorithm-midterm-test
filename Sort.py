# 정렬(Sort) 알고리즘
# 데이터를 특정한 기준(오름차순, 내림차순 등)에 따라 나열하는 기법
# 효율적인 정렬은 탐색 등 다른 알고리즘의 성능에 큰 영향을 미침

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print(f"퀵 정렬 결과: {quick_sort(data)}")
