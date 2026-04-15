# [백트랙킹(Backtracking) 알고리즘]
# 해를 찾는 도중 정답이 될 가능성이 없으면 되돌아가는 기법

# [시험 꿀팁! - 핵심 추가]
# 1. 유망성(Promising)과 가지치기(Pruning): 
#    "현재 노드가 정답 가능성이 없다고 판단(유망하지 않음)되면, 
#    더 이상 자식 노드를 방문하지 않고 부모 노드로 퇴각(가지치기)한다!"
# 2. 상태 공간 트리(State Space Tree): DFS 기반으로 모든 가능한 경로를 탐색.
# 3. 대표 예시: N-Queens 문제가 가장 대표적인 예시로 시험 출제 확률이 매우 높음!

def is_safe(board, row, col, n):
    # 알고리즘 진행: 1. 현재 위치에 퀸을 놓을 수 있는지 '유망성(Promising)' 검사
    for i in range(row):
        # 같은 열, 혹은 양방향 대각선에 다른 퀸이 있으면 '유망하지 않음'
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def n_queens(n, row, board):
    # 모든 행에 배치 성공 시 해 1개 발견
    if row == n:
        return 1
    
    count = 0
    for col in range(n):
        if is_safe(board, row, col, n):
            # 알고리즘 진행: 2. 유망하면 자식 노드로 진행
            board[row] = col
            count += n_queens(n, row + 1, board)
        # 알고리즘 진행: 3. 유망하지 않으면 더 이상 들어가지 않고 다음 열 탐색 (가지치기/퇴각)
    return count

n = 4
board = [0] * n
print(f"{n}-Queens 해의 개수: {n_queens(n, 0, board)}")
