# React Frontend Project

- 목표
  - React Project 시작하는 방법 정리
  - React 기본 정리
  - React-router-dom 정리
  - React-redux 학습

## 1. Node.js 설치하기

- 홈페이지에서 node.js 최신버전 다운로드

```
22.08.24. 현재 node version

# node --version
v12.13.0
```

- 19년도인가 20년도에 설치한 node.js

- 기존 노드.js 최신 버전으로 바꾸기

```
1. 최신 노드.js 설치 후 최신번전 노드의 시스템 환경변수를 기존 노드 환경 변수보다 위로 보내는 방법
# 시스템 환경 변수
C:\Program Files\nodejs
끝 npm 은 node_modules 폴더에 있으므로, 위에만 Path로 잡아주면 됨.

2. nvm 설치해서 기본 노드 설정 + 사용하고 싶은 node.js 선택해서 사용하는 방법
nvm 설치 
nvm exec 17 npm version 

-- option : exec + (version) => cli 명령 한번만 (version)으로 실행, cli: npm version

node.js 버전 변경 명령어
nvm ...
```

- 두가지 빙법 모두 간단한 방법들이지만, 1번으로 선택.

- create-react-app 설치하기

```
npm install -g create-react-app

# -g : 글로벌 = 시스템 디렉터리에 설치하는 옵션 없다면, 현재 디렉토리 내부에 로컬로 설치
```

- create-react-app 첫 프로젝트 만들기

```
# craetae-react-app (proejct-name)

# craetae-react-app frontend

디렉토리 구조
(project-naem)
├── README.md
├── node_modules
├── package.json
├── package-lock.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── reportWebVitals.js
```

- 실행하기

```
# cd (project-name)

# npm start
```

- Config 설정하기

```
# dev 

# product 

# Test 나누기
```

- 

