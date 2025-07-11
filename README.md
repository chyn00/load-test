# Load Test Environment (Locust 기반)

이 프로젝트는 Python 기반의 Locust를 이용한 부하 테스트용 환경입니다.  
아래 방법대로 `.venv` 가상환경에서만 종속성을 설치하고 실행할 수 있습니다.

## 사전 조건

- Python 버전: 3.9.6 (macOS)
- `.venv/` 가상환경 디렉토리는 이미 프로젝트 루트에 생성되어 있어야 합니다.

## 설치 및 실행 방법

```bash
# 가상환경 활성화
source .venv/bin/activate

# Locust 설치
pip3 install locust

# 가상환경 비활성화
deactivate

# 테스트 실행 시 다시 가상환경 활성화
source .venv/bin/activate

# 부하 테스트 실행
locust -f load_test.py  # (-f: 실행할 테스트 스크립트 파일 지정)
```

## HeadLess 실행
아래 명령어로 해야 정확한 request가 console에 출력된다.
```bash
locust -f load_test.py --headless -u 1000 -r 1000 --run-time 20s --host=http://localhost:9999
```
