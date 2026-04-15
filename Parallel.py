# 병렬(Parallel) 알고리즘
# 여러 개의 처리 장치(CPU 코어 등)를 사용하여
# 문제를 여러 개의 작은 태스크로 나누어 동시에 실행하는 기법
# 수행 시간을 단축하는 것이 주된 목적

import multiprocessing
import time

def square(number):
    time.sleep(1) # 부하 가정
    return number * number

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    # 순차적 실행 (Sequential)
    start = time.time()
    res_seq = [square(n) for n in numbers]
    print(f"순차 실행 시간: {time.time() - start:.2f}s")
    
    # 병렬 실행 (Parallel)
    start = time.time()
    with multiprocessing.Pool() as pool:
        res_par = pool.map(square, numbers)
    print(f"병렬 실행 시간: {time.time() - start:.2f}s")
    print(f"병렬 계산 결과: {res_par}")
