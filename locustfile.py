# -*- coding: utf-8 -*-
import random

from locust import HttpUser, between, tag, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 1.5)

    def on_start(self):
        self.uid = str(random.randint(0, 100_000)).zfill(6)

    @tag("attempt", "ligth")
    @task(2)
    def attempt(self):
        self.client.get("/hello/")

    @tag("simulate", "light")
    @task(1)
    def simulate(self):
        self.client.post(
            "/simulate/",
            json={
                "uid": self.uid,
                "n_sim": random.randint(10, 20),
            },
        )

    @tag("sleep", "heavy")
    @task(2)
    def slepper(self):
        self.client.get("/sleep/")
