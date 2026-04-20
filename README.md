# Algorithm Study Repository

## 1. 개요
이 레포지토리는 알고리즘 중간/기말고사 대비를 위해 핵심 개념 이론과 파이썬 구현 코드를 체계적으로 정리한 공간입니다. 각 알고리즘의 동작 원리뿐만 아니라 시험에서 중요하게 다뤄지는 성능 분석(시간/공간 복잡도)과 최적화 전략을 포함하고 있습니다.

## 2. 프로젝트 구조 (Directory Structure)

### 2.1. Concepts (개념 정리)
핵심 이론과 시험 포인트를 정리한 Markdown 문서들입니다.

- [01_Sort_정렬.md](./Concepts_개념정리/01_Sort_정렬.md)
- [02_Search_탐색.md](./Concepts_개념정리/02_Search_탐색.md)
- [03_1_Greedy_Basic.md](./Concepts_개념정리/03_1_Greedy_Basic.md) (배낭 문제, 스케줄링)
- [03_2_Greedy_Graph.md](./Concepts_개념정리/03_2_Greedy_Graph.md) (MST-크루스칼/프림, 다익스트라)
- [03_3_Greedy_App.md](./Concepts_개념정리/03_3_Greedy_App.md) (허프만 코딩, 집합 커버)
- [04_Backtracking_백트래킹.md](./Concepts_개념정리/04_Backtracking_백트래킹.md)
- [05_BranchAndBound_분기한정.md](./Concepts_개념정리/05_BranchAndBound_분기한정.md)
- [06_Approximation_근사알고리즘.md](./Concepts_개념정리/06_Approximation_근사알고리즘.md)
- [07_Advanced_고급알고리즘.md](./Concepts_개념정리/07_Advanced_고급알고리즘.md)

### 2.2. Codes (소스 코드)
알고리즘의 실제 파이썬 구현 사례입니다. 모든 코드는 일관된 양식(시험 꿀팁, 단계별 주석)으로 정리되어 있습니다.

- [01_Sort_정렬.py](./Codes_소스코드/01_Sort_정렬.py)
- [02_Search_탐색.py](./Codes_소스코드/02_Search_탐색.py)
- [03_1_Greedy_Basic.py](./Codes_소스코드/03_1_Greedy_Basic.py)
- [03_2_Greedy_Graph.py](./Codes_소스코드/03_2_Greedy_Graph.py)
- [03_3_Greedy_App.py](./Codes_소스코드/03_3_Greedy_App.py)
- [04_MergeSort_합병정렬.py](./Codes_소스코드/04_MergeSort_합병정렬.py)
- [05_Backtracking_백트래킹.py](./Codes_소스코드/05_Backtracking_백트래킹.py)
- [06_BranchAndBound_분기한정.py](./Codes_소스코드/06_BranchAndBound_분기한정.py)
- [07_Approximation_근사알고리즘.py](./Codes_소스코드/07_Approximation_근사알고리즘.py)
- [08_Parallel_병렬알고리즘.py](./Codes_소스코드/08_Parallel_병렬알고리즘.py)
- [09_Distributed_분산알고리즘.py](./Codes_소스코드/09_Distributed_분산알고리즘.py)
- [10_Quantum_양자알고리즘.py](./Codes_소스코드/10_Quantum_양자알고리즘.py)

## 3. 학습 가이드
1. **이론 먼저**: `Concepts_개념정리` 문서를 통해 알고리즘의 성립 조건과 시험 포인트를 먼저 이해합니다.
2. **코드 실행**: `Codes_소스코드` 파이썬 파일을 실행하며 실제 데이터 처리 과정을 확인합니다. 모든 파일 상단에는 시험 대비 핵심 요약이 포함되어 있습니다.
3. **핵심 키워드**: 정렬의 피벗 전략, 그리디의 최적 부분 구조, MST의 사이클 판정, 허프만의 접두어 성질 등을 중점적으로 복습하십시오.

## 4. 환경 설정 
```bash
pip install -r requirements.txt
```
