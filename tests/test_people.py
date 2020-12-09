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


def test_person_num():
    """
    Ensure when number is passed to query, the correct number of persons
    is returned.
    """
    # WHEN FastAPI GET request is given

    # GIVEN GET request to person endpoint with query of 28
    resp = client.get("/person", params={"num": 28})

    # THEN 28 persons are returned
    resp_dict = resp.json()

    assert len(resp_dict) == 28


def test_person_num_failing():
    """
    Ensure when more than 50 persons are requested, 422 is returned and
    no persons are returned.
    """
    # WHEN FastAPI GET request is given

    # GIVEN GET request to person endpoint with query of 51
    resp = client.get("/person", params={"num": 51})

    # THEN 422 is returned.
    assert resp.status_code == 422
