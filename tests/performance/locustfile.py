from locust import HttpUser, task, between


class RecargaUser(HttpUser):
    wait_time = between(0.1, 0.5)
    host = "http://localhost:8000"

    @task(3)
    def recarga_normal(self):
        self.client.post(
            "/recarga",
            json={"monto": 15000, "premium": False},
        )

    @task(2)
    def recarga_premium(self):
        self.client.post(
            "/recarga",
            json={"monto": 30000, "premium": True},
        )

    @task(1)
    def recarga_invalida(self):
        with self.client.post(
            "/recarga",
            json={"monto": 999, "premium": False},
            catch_response=True,
        ) as response:
            if response.status_code == 400:
                response.success()

    @task(1)
    def health_check(self):
        self.client.get("/health")