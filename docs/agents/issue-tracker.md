# 이슈 트래커: GitHub

이 레포의 이슈와 PRD 는 GitHub 이슈로 살아 있다. 모든 작업은 `gh` CLI 를 쓴다.

## 컨벤션

- **이슈 생성**: `gh issue create --title "..." --body "..."`. 여러 줄 본문엔 heredoc 사용.
- **이슈 읽기**: `gh issue view <번호> --comments`. 필요한 코멘트는 `jq` 로 필터링하고, 라벨도 같이 가져옴.
- **이슈 목록**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` 형태로, 적절한 `--label` 과 `--state` 필터 적용.
- **이슈 코멘트**: `gh issue comment <번호> --body "..."`
- **라벨 추가 / 제거**: `gh issue edit <번호> --add-label "..."` / `--remove-label "..."`
- **종료**: `gh issue close <번호> --comment "..."`

레포는 `git remote -v` 에서 추론한다 — `gh` 는 클론 안에서 실행하면 자동으로 잡는다.

## 스킬이 "이슈 트래커에 게시한다" 라고 할 때

GitHub 이슈를 만든다.

## 스킬이 "관련 티켓을 가져온다" 라고 할 때

`gh issue view <번호> --comments` 를 실행한다.
