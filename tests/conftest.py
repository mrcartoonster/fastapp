# -*- coding: utf-8 -*-
"""
Location of simple fixture(s).
"""
import pytest

emojies = [":grinning_face:", ":smiling_face:", ":zany_face"]


@pytest.fixture()
def emo():
    """
    Return emojies to test against.
    """
    pass
