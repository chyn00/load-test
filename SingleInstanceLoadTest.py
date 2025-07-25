import uuid

from locust import FastHttpUser, task, constant_pacing, events


class OrderLoadTest(FastHttpUser):
  wait_time = constant_pacing(1)  # 1초 마다의 정확한 집계를 위해 변경

  @task
  def order_stock_limit(self):
    payload = {
      "itemCode": "1234",
      "userId": str(uuid.uuid4()),
      "quantity": 1
    }

    self.client.post("/order/stock/limit", json=payload)

#locust -f SingleInstanceLoadTest.py --headless -u 1000 -r 1000 --run-time 20s --host=http://localhost:9999
