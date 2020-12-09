# -*- coding: utf-8 -*-
"""
Random user endpoint.

Using Mimesis example for this: https://mimesis.name/tips.html#dummy-
api-endpoints

"""
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
