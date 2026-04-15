# 백트랙킹(Backtracking) 알고리즘
# 해를 찾는 도중, 현재의 경로가 정답이 될 가능성이 없다고 판단되면
# 더 이상 진행하지 않고 되돌아가서 다른 경로를 탐색하는 기법
# "가지치기(Pruning)"를 통해 불필요한 탐색 범위를 줄이는 것이 핵심

def is_safe(board, row, col, n):
    # 같은 열에 퀸이 있는지 확인
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def n_queens(n, row, board):
    if row == n:
        return 1

    count = 0
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            count += n_queens(n, row + 1, board)
    return count


n = 4
board = [0] * n
print(f"{n}-Queens 해의 개수: {n_queens(n, 0, board)}")
