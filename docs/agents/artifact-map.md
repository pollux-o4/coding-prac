# 산출물 라우팅 표 (Artifact map)

세션 (Session) 이 지속 보관할 무언가를 만들었을 때, 이게 어디로 가는지 30초 안에 확인하는 표.

파일이 어디에 들어가는지만 알면 되는 상황이라면 이 표만으로 충분하다. 실제로 그 산출물의 내용을 작성할 때만 우측의 풀 계약 문서를 펼친다.

| 저장하려는 것 | 경로 | 풀 계약 |
|---|---|---|
| 학습 단위의 설명 | `docs/topics/<slug>/README.md` | [TOPIC_FORMAT.md](../TOPIC_FORMAT.md) |
| 학습 단위의 학습 코드 | `implementations/<lang>/<slug>/` | [ARTIFACT_POLICY.md](../ARTIFACT_POLICY.md) |
| 연습 문제 풀이 코드 | `solutions/<slug>/` | [ARTIFACT_POLICY.md](../ARTIFACT_POLICY.md) |
| 세션 마감 요약 | `docs/sessions/<YYYY-MM-DD>-<slug>.md` | [SESSION_SUMMARY_FORMAT.md](../SESSION_SUMMARY_FORMAT.md) |
| 현재 학습 상태 갱신 | `docs/PROGRESS.md` (직접 편집) | [PROGRESS.md](../PROGRESS.md) |
| 새 학습 단위 자리표시자 (스캐폴드) | `python scripts/scaffold_topic.py <slug>` 실행 | [scripts/scaffold_topic.py](../../scripts/scaffold_topic.py) |
| PRD 또는 새 이슈 | `gh` CLI 로 GitHub 이슈 생성 | [issue-tracker.md](./issue-tracker.md) |
| 나중에 보면 의아할 만한 결정 기록 | `docs/adr/NNNN-<slug>.md` | [CONTEXT.md](../../CONTEXT.md) (도메인 용어) |

## 메모

- `<slug>` 는 학습 단위 슬러그 (예: `binary-tree`). `docs/topics/`, `implementations/<lang>/`, `solutions/`, `docs/PROGRESS.md` 에서 같은 슬러그가 그 학습 단위를 묶는다.
- `<lang>` 은 `python`, `java`, `c`, `typescript` 중 하나. Python 이 주 언어이고, 학습 단위가 여러 언어로 공부되면서 다른 언어가 추가된다.
- 표에 나오는 "학습 단위" 같은 도메인 용어는 [CONTEXT.md](../../CONTEXT.md) 에 정의되어 있다.
- 이 표는 파생 문서다. 경로와 계약의 진실 원천은 우측 링크의 파일들에 있다. 계약이 바뀌면 계약 문서를 먼저 고치고 이 표를 따라 갱신한다.
