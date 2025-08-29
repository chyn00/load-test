import uuid
from locust import FastHttpUser, task, constant_pacing


class LeakTest(FastHttpUser):
  # 정확한 1,000 TPS 집계를 위해 각 유저가 1초에 1회 요청을 보내도록 설정했습니다.
  wait_time = constant_pacing(1)

  @task
  def memory_leak_test(self):
    # GET 방식으로 /bug 엔드포인트 호출 + String 파라미터 s 전송
    self.client.get("/bug", params={"s": str(uuid.uuid4())})


# 실행 예시 (1,000 TPS 목표, 20초 동안, 포트 2222):
# locust -f SingleInstanceLeakTest.py --headless -u 1000 -r 1000 --run-time 20s --host=http://localhost:2222