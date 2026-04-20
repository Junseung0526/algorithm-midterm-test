# [중간고사 대비] 분할 정복 (Merge Sort) 시각화 및 테스트 세트

def merge_sort_visualizer(arr, depth=0):
    """합병 정렬 과정을 시각화하여 보여주는 함수"""
    indent = "  " * depth
    print(f"{indent}[Divide] {arr}")
    
    if len(arr) <= 1:
        return arr

    # 1. 분할 (Divide)
    mid = len(arr) // 2
    left = merge_sort_visualizer(arr[:mid], depth + 1)
    right = merge_sort_visualizer(arr[mid:], depth + 1)

    # 2. 정복 및 결합 (Conquer & Combine)
    merged = merge(left, right)
    print(f"{indent}[Merge ] {left} + {right} => {merged}")
    return merged

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[r]: # Stable 정렬을 위해 <= 사용
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    print("=== 합병 정렬(Merge Sort) 시각화 ===")
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"원본 데이터: {data}\n")
    
    sorted_data = merge_sort_visualizer(data)
    print(f"\n최종 결과: {sorted_data}")

    print("\n[시험 포인트 복습]")
    print("1. 시간 복잡도: 어떤 상황에서도 O(n log n)")
    print("2. 공간 복잡도: 추가 배열 필요 O(n)")
    print("3. 특징: Stable(안정) 정렬임")

if __name__ == "__main__":
    # merge 함수 내 오타 수정 (right[r] -> right[j])
    def merge_fixed(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    merge = merge_fixed
    run_tests()
