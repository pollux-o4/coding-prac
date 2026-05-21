# PRD 는 이슈 트래커에 살고, 레포 파일로 두지 않음

PRD 와 그 AFK 준비 sub-issue 들은 GitHub 이슈로 존재하며, `docs/PRD.md` 같은 파일이 아니다. PRD 본문은 이슈 본문에 직접 작성하고, sub-issue 는 본문에 `Parent: #N` 으로 부모를 가리키며, 종료는 머지 PR 의 `Closes #N` 으로 처리한다. 이렇게 두면 PRD 가 코멘트·라벨·assignee 와 함께 트래커 안에서 버전 관리되며, 에이전트는 `에이전트 준비 (ready-for-agent)` 라벨로 작업을 가져갈 수 있다. 대가는 새 사용자가 PRD 를 보려고 파일 대신 `gh issue view 1` 을 실행해야 한다는 점인데, 이미 `docs/agents/issue-tracker.md` 가 "이슈 트래커에 게시한다" 는 컨벤션을 단일 진실 원천 (source of truth) 으로 박아둔 이상 수용 가능한 비용이다.
