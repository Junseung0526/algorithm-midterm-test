import time

# [중간고사 대비] 정렬 알고리즘 시각화 및 테스트 세트

def visualizer(name, step, arr, pivot=None):
    """정렬 과정을 단계별로 보여주는 시각화 함수"""
    print(f"[{name}] Step {step}: {arr}", end="")
    if pivot is not None:
        print(f" (Pivot: {pivot})")
    else:
        print()

def quick_sort(arr, step=1, verbose=True):
    """퀵 정렬: 피벗 기준 분할 정복"""
    if len(arr) <= 1:
        return arr
    
    # 전략: 중앙값 선택으로 최악의 경우 방지
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if verbose:
        visualizer("Quick Sort", step, arr, pivot)
    
    # 재귀적으로 정렬
    return quick_sort(left, step + 1, verbose) + middle + quick_sort(right, step + 1, verbose)

def merge_sort(arr, step=1, verbose=True):
    """합병 정렬: 분할 후 정렬하며 병합"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], step + 1, verbose)
    right = merge_sort(arr[mid:], step + 1, verbose)
    
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]: # <= 로 구현해야 Stable(안정) 유지
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]
    
    if verbose:
        visualizer("Merge Sort", step, merged)
    return merged

def insertion_sort(arr, verbose=True):
    """삽입 정렬: 정렬된 구간을 확장"""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if verbose:
            visualizer("Insertion Sort", i, arr)
    return arr

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    test_cases = {
        "일반 케이스": [3, 6, 8, 10, 1, 2, 1],
        "이미 정렬된 경우": [1, 2, 3, 4, 5],
        "역순 정렬된 경우": [5, 4, 3, 2, 1],
        "중복값이 많은 경우": [3, 1, 3, 3, 2]
    }
    
    for name, data in test_cases.items():
        print(f"\n--- {name} 테스트 ---")
        print(f"원본: {data}")
        
        # 1. Quick Sort
        print("\n[퀵 정렬 실행]")
        quick_sort(data.copy(), verbose=True)
        
        # 2. Insertion Sort (거의 정렬된 경우 효율성 확인용)
        print("\n[삽입 정렬 실행]")
        insertion_sort(data.copy(), verbose=True)

if __name__ == "__main__":
    print("=== 알고리즘 중간고사 대비 시각화 도구 ===")
    run_tests()
