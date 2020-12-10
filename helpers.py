# -*- coding: utf-8 -*-
"""
Random user endpoint.

Using Mimesis example for this: https://bit.ly/37KUAlo

"""
from emoji import emojize
from mimesis import Generic
from mimesis.enums import Gender
from mimesis.schema import Field, Schema

_ = Field("en")
random_users = Schema(
    lambda: {
        "id": _("uuid"),
        "name": _("name", gender=Gender.MALE),
        "surname": _("surname", gender=Gender.MALE),
        "email": _("email"),
        "age": _("age"),
        "username": _("username", template="UU_d"),
        "occupation": _("occupation"),
        "address": {
            "street": _("street_name"),
            "city": _("city"),
            "zipcode": _("zip_code"),
        },
    },
)

g = Generic("en")  # Going to stick with American English.


def passwd(length: int = 8, hash: bool = False) -> str:
    """
    Helper function to generate a random password.
    """
    return g.person.password(length=length, hashed=hash)


def emojis():
    """
    Helper function to create random emojis.
    """
    return emojize(g.internet.emoji(), use_aliases=True)
