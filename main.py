# -*- coding: utf-8 -*-
"""
Main FastAPI app.
"""
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Query

from random_endpoints import random_users

app = FastAPI()


@app.get("/person")
async def randome_users(
    num: int = Query(
        5,
        title="Get randon set of people.",
        ge=1,
        le=50,
    )
):
    """
    Get a random list of persons.

    The defautl is 5

    """
    persons = random_users.create(iterations=num)
    return persons
