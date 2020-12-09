# -*- coding: utf-8 -*-
"""
Tests for GET endpoints.
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_persons():
    """
    Ensure that a list of randome persons are returned.
    """
    # WHEN FastApp GET request is given

    # GIVEN GET request to persons
    resp = client.get("/person")

    # THEN a 200 is returned
    assert resp.status_code == 200
