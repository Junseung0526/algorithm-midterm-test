# [탐색(Search) 알고리즘]
# 효율적으로 원하는 데이터를 찾는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. 전제 조건: 이진 탐색은 반드시 **'정렬된 데이터'**에서만 사용 가능하다! (강력 강조!).
# 2. 데이터가 섞여 있다면 선형 탐색(O(n))을 하거나 먼저 정렬을 해야 함.
# 3. 시간 복잡도: 탐색 범위를 계속 절반씩 줄여 O(log n).

def binary_search(arr, target):
    # 알고리즘 진행: 1. 탐색 범위 초기 설정
    low = 0
    high = len(arr) - 1
    
    # 알고리즘 진행: 2. 범위를 좁혀가며 탐색
    while low <= high:
        mid = (low + high) // 2
        
        # 찾았으면 반환
        if arr[mid] == target:
            return mid
        # 알고리즘 진행: 3. 타겟이 중간값보다 크면 오른쪽 범위 탐색
        elif arr[mid] < target:
            low = mid + 1
        # 알고리즘 진행: 4. 타겟이 중간값보다 작으면 왼쪽 범위 탐색
        else:
            high = mid - 1
            
    return -1 # 찾지 못함

data = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(data, target)
print(f"이진 탐색 결과 (값 {target}의 인덱스): {result}")
