# -*- coding: utf-8 -*-
"""
Main FastAPI app.
"""
# -*- coding: utf-8 -*-
from typing import List

from fastapi import FastAPI, Query

from helpers import emojis, passwd, random_users
from pydantic_models import Emoji, Password, Person

app = FastAPI()


@app.get("/person", response_model=List[Person])
async def randome_users(
    num: int = Query(
        5,
        title="Get randon set of people.",
        ge=1,
        le=50,
    )
) -> List[Person]:
    """
    Get a random list of persons.

    The defautl is 5

    """
    persons = random_users.create(iterations=num)
    return persons


@app.get("/password", response_model=Password)
async def randome_password(
    num: int = Query(
        8,
        title="Length of password.",
        le=64,
    ),
    hashing: bool = Query(
        False,
        title="Return an MD5 hashed password",
    ),
):
    """
    Generate a random password.
    """
    password = passwd(num, hashing)
    return {"password": password}


@app.get("/emoji", response_model=Emoji)
async def random_emoji():
    """
    Return a random emoji.
    """
    return {"emoji": emojis()}
