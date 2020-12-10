# -*- coding: utf-8 -*-
"""
Response models for each endpoint.
"""
from pydantic import BaseModel


class RandomUsers(BaseModel):
    """
    Type Check valid Python string returned.
    """

    # Keeping this simple. May create a Union to check for valid MD5 hashed
    # string is returned.
    password: str


class Person(BaseModel):
    """
    Type check valid Persons is returned.
    """

    pass
