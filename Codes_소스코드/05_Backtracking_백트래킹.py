# [중간고사 대비] 백트래킹 (N-Queens) 시각화 및 테스트 세트

def is_promising(board, row, col):
    """현재 자리에 퀸을 놓을 수 있는지 확인 (가지치기 조건)"""
    for i in range(row):
        # 1. 같은 열에 있는지 확인
        if board[i] == col:
            return False
        # 2. 대각선에 있는지 확인 (행 차이 == 열 차이)
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def n_queens_visualizer(board, row, n, verbose=True):
    """N-Queens 백트래킹 과정 시각화"""
    if row == n:
        print(f"\n[정답 발견!] 퀸 배치: {board}")
        return 1
    
    count = 0
    for col in range(n):
        board[row] = col
        if verbose:
            print(f"Row {row}: {col}번 열 시도 중... ", end="")
        
        if is_promising(board, row, col):
            if verbose: print("=> [유망함] 다음 행으로!")
            count += n_queens_visualizer(board, row + 1, n, verbose)
        else:
            if verbose: print("=> [가지치기] 공격 가능 지역")
            
    return count

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    N = 4
    print(f"=== {N}-Queens 백트래킹 시각화 ===")
    board = [0] * N
    total_solutions = n_queens_visualizer(board, 0, N, verbose=True)
    print(f"\n총 {total_solutions}개의 해를 찾았습니다.")

    print("\n[시험 포인트 복습]")
    print("1. 백트래킹의 핵심: 유망하지 않으면 되돌아가는 '가지치기(Pruning)'")
    print("2. 대표 문제: N-Queens, 부분집합의 합, 미로 찾기")
    print("3. DFS와 달리 모든 경로를 다 가지 않음 (효율적)")

if __name__ == "__main__":
    run_tests()
