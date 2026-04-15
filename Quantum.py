# 양자(Quantum) 알고리즘
# 양자 역학의 특성(중첩, 얽힘)을 이용한 컴퓨팅 방식
# 특정 문제(인수분해, 탐색 등)에서 기존 방식보다 
# 압도적인 속도 향상을 보여줌

import random
import math

# 실제 양자 하드웨어나 라이브러리(Qiskit 등)가 없으므로
# 개념적인 시뮬레이션 코드 (양자 상태의 측정)

def quantum_measurement(state_0, state_1):
    # state_0: |0> 상태일 확률 진폭의 제곱
    # state_1: |1> 상태일 확률 진폭의 제곱
    # (state_0 + state_1 = 1 이어야 함)
    
    rand_val = random.uniform(0, 1)
    if rand_val < state_0:
        return "|0> 로 붕괴(Measured)"
    else:
        return "|1> 로 붕괴(Measured)"

# 예: 중첩 상태 (Superposition) |ψ> = 1/√2 |0> + 1/√2 |1>
# 이때 |0> 일 확률은 (1/√2)^2 = 0.5
p_0 = (1 / math.sqrt(2)) ** 2
p_1 = 1 - p_0

print("--- 양자 중첩 상태 측정 시뮬레이션 ---")
results = {"|0> 로 붕괴(Measured)": 0, "|1> 로 붕괴(Measured)": 0}
for _ in range(100):
    outcome = quantum_measurement(p_0, p_1)
    results[outcome] += 1

print(f"100번 시도 중 결과: {results}")
