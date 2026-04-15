# 탐색(Search) 알고리즘
# 방대한 데이터 중에서 원하는 값을 효율적으로 찾는 기법
# 선형 탐색(O(n))부터 이진 탐색(O(log n))까지 다양한 방식이 존재함

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

data = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(data, target)
print(f"이진 탐색 결과 (값 {target}의 인덱스): {result}")
