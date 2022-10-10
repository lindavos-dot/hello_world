from main import *


def test_get_none():
    assert get_none() == None


def test_flatten_dict(dict):
    assert flatten_dict(dict) == None