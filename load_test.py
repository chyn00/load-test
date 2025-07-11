from locust import FastHttpUser, task, between, constant_pacing
import random
import uuid

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
