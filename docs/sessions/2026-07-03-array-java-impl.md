# 2026-07-03 - Array - Java re-implementation

## 1. Learned scope

체크포인트: Array - Java 재구현 (`implementations/java/array/`), Python
버전 대비 트레이드오프 노트 1개 이상. `MyArray.java`에 `data`(고정 크기
배열)/`size`(실사용 개수) 필드, 생성자, `get`/`set`/`insert`/`delete`,
용량 부족 시 배열을 두 배로 늘리는 `grow()`를 구현했다. `insert`/`grow`는
질문-답변으로 깊게 다진 뒤 AI가 초안을 짰고, `get`/`set`/`delete`는
TODO로 비워 학습자가 직접 타이핑했다. VSCode 디버거로 `insert` 호출마다
`data` 배열이 한 칸씩 채워지는 걸 직접 관찰해 로직을 확인했다. 학습자가
"Java는 배열이 고정 크기라 용량 관리 코드(`grow`)를 직접 짜야 하지만
Python 리스트는 이게 숨겨져 있다"는 트레이드오프를 스스로 짚어 체크포인트
완료 기준을 충족했다.

## 2. Blockers or confusion

- Java 배열 리터럴 문법(`new int[]{...}` vs 축약형 `{...}`)과 `new`가
  언제 생략 가능한지(선언+초기화 동시일 때만) 헷갈렸음.
- `void` 반환 타입, 정적 타입 vs 동적 타입의 "쓰기 힘듦 vs 읽기 편함"
  트레이드오프는 처음 보는 개념이라 예시로 짚어줌.
- 카운팅 for문(`for(초기화;조건식;증감식)`)과 향상된 for문(`for(v : arr)`)
  구조를 혼동함 - 후자를 보고 "if문이 for 안에 들어간 것 같다"고 오해.
- Java에 이름 지정 인자가 없다는 걸 몰랐고, VSCode의 파라미터 이름
  인레이 힌트를 실제 문법으로 착각함.
- 환경 문제: 시스템에 JDK가 없고 JRE 1.8만 설치돼 있어 터미널
  `javac`가 즉시 실패. VSCode F5 실행도 처음엔 "기본 클래스를 찾거나
  로드할 수 없습니다" 오류가 남 (비-Maven/Gradle 단일 폴더 프로젝트라
  워크스페이스 빌드 캐시가 꼬였던 것으로 추정). VSCode Java 확장에
  내장된 JDK 21(`redhat.java-*/jre/21.0.11-win32-x86_64/bin`)로 직접
  컴파일/실행해서 우회했고, 이후 F5도 정상 동작함.
- 디버거에서 배열 내용을 보려면 `arr` -> `data`를 펼쳐야 한다는 걸
  처음엔 몰라서 "값이 안 변하는 것처럼 보인다"고 헷갈렸음 (참조와 내용의
  차이).

## 3. Changed artifacts

- `implementations/java/array/MyArray.java` - create - Array의 Java
  재구현 (`get`/`set`/`insert`/`delete`/`grow`), `get`/`set`/`delete`는
  학습자가 직접 타이핑.
- `docs/topics/array/README.md` - update - 언어별 진행 상황 표에 Java
  `done` 반영, 연결된 산출물에 Java 구현 링크와 트레이드오프 노트 추가,
  마지막 갱신 마커 갱신.
- `docs/PROGRESS.md` - updated as part of this close-out (see the
  document itself for the per-field changes).

## 4. Next step

Array - 문제 풀이 단계 시작. `solutions/array/` 아래에 배열 관련 연습
문제 1개를 처음부터 끝까지 풀어보는 것이 다음 체크포인트. 완료 기준:
문제 1개를 풀고, 학습자가 자신의 풀이 접근 방식과 시간복잡도를 스스로
설명할 수 있어야 함.

## 5. Evidence links

- [docs/topics/array/README.md](../topics/array/README.md)
- [implementations/java/array/MyArray.java](../../implementations/java/array/MyArray.java)
