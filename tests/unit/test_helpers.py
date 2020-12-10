# -*- coding: utf-8 -*-
"""
Unit tests for our function helpers.
"""
from helpers import emojis, passwd


def test_passwd():
    """
    Make sure a password string of 8 characters is returned.
    """
    assert len(passwd()) == 8


def test_emojis():
    """
    Ensure that an emoji is returned.
    """
    # GIVEN emojis helper function

    # WHEN emojis's called
    smile = emojis()

    # THEN variable is not None
    assert smile is not None
