# -*- coding: utf-8 -*-
"""
Pydantic Response models for each endpoint.
"""
from pydantic import UUID4, BaseModel, EmailStr


class Password(BaseModel):
    """
    Type Check valid Python string returned.
    """

    # Keeping this simple. May create a Union to check for valid MD5 hashed
    # string is returned.
    password: str


class Address(BaseModel):
    """
    Nested submodule for Person's Pydantic model.
    """

    # Not checking for valid U.S. streets, cityies or zip codes. Ain't nobody
    # got time for that! Trusting Mimesis on that.
    street: str
    city: str
    zipcode: str


class Person(BaseModel):
    """
    Type check valid Persons is returned.
    """

    id: UUID4
    name: str
    surname: str
    email: EmailStr
    age: int
    username: str
    occupation: str
    address: Address


class Emoji(BaseModel):
    """
    Type check Respone Model for emoji.
    """

    emoji: str
