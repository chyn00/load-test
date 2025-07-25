import uuid
import random

from locust import FastHttpUser, task, constant_pacing


class MultiInstanceLoadTest(FastHttpUser):
  wait_time = constant_pacing(1)

  # 반드시 아무 host라도 선언해야 함 (요구사항)
  host = "http://localhost"

  ports = [9999, 9555, 9544, 9533]

  @task
  def order_stock_limit(self):
    port = random.choice(self.ports)
    full_url = f"http://localhost:{port}/order/stock/limit"

    payload = {
      "itemCode": "1234",
      "userId": str(uuid.uuid4()),
      "quantity": 1
    }

    self.client.request(
        method="POST",
        url=full_url,
        json=payload,
        name="/order/stock/limit"
    )

#locust -f MultiInstanceLoadTest.py --headless -u 1000 -r 1000 --run-time 100s
