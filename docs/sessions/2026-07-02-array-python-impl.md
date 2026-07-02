# 2026-07-02 - Array - Python 구현

## 1. 학습 범위

진행한 체크포인트: Array - Python 구현. `implementations/python/array/`에
조회/수정/삽입/삭제를 갖춘 배열 기반 구조를 작성하는 것 (완료 기준: 학습자가
코드를 직접 짚으며 각 연산의 시간복잡도를 설명할 수 있을 것). 파이썬 리스트를
감싼 `MyArray` 클래스로 `get`/`set`/`insert`/`delete`를 학습자가 직접
작성했고, 세션 끝에 `get`/`set`은 O(1), `insert`/`delete`는 O(n)이라고 스스로
설명함 - 완료 기준 충족.

## 2. 막힌 점 / 헷갈린 점

- `insert`에서 뒤 원소를 미는 반복문 경계(시작 인덱스/끝 인덱스)를 여러 번
  틀림 - 빈 자리를 만들지 않고 바로 밀려다 `IndexError`가 나는 지점, 그리고
  `range`의 `stop`이 제외된다는 점을 손으로 예시를 따라가며 정정.
- `delete`를 처음엔 `insert`와 같은 방향(큰 인덱스 → 작은 인덱스)으로 당기려
  해서 원래 값이 밀리기 전에 덮어써지는 버그가 남 - 당기기는 작은 인덱스부터
  진행해야 한다는 점으로 정정.
- 클래스/인스턴스/`self` 개념을 처음 접함 - "클래스 안에 `def`로 정의했는데
  왜 바로 못 부르냐"는 질문에서, `self`는 여러 인스턴스 중 "이 인스턴스"를
  가리키는 용도라는 점을 `arr1`/`arr2` 예시로 정정.
- `list.append`는 항상 맨 뒤에만 추가되고 위치 지정이 안 된다는 점, `pop()`은
  인자 없으면 맨 뒤를 꺼낸다는 점도 헷갈려서 짚고 넘어감.

## 3. 변경된 산출물

- `implementations/python/array/my_array.py` - 생성 - `MyArray` 클래스:
  `get`/`set`(O(1)), `insert`/`delete`(O(n)) 구현.
- `docs/topics/array/README.md` - 갱신 - 언어별 진행 상황 표에서 Python을
  done으로, 연결된 산출물 섹션에 구현 링크 추가.
- `docs/PROGRESS.md` - 갱신 - 필드별 변경 내역은 PROGRESS.md 참고.

## 4. 다음 스텝

Array 체크포인트 계속: 언어 로테이션의 다음 순서인 **Java 재구현** -
`implementations/java/array/`에 Python 버전과 동일한 연산(조회/수정/삽입/삭제)을
Java로 다시 작성하고, Python과 다른 점(정적 타입, 클래스 문법 등) 트레이드오프
노트 1개 포함. 완료 기준: 학습자가 Python 버전과 다른 점을 최소 1가지 설명할
수 있을 것.

## 5. 근거 링크

- [implementations/python/array/my_array.py](../../implementations/python/array/my_array.py)
- [docs/topics/array/README.md](../topics/array/README.md)
- [docs/PROGRESS.md](../PROGRESS.md)
