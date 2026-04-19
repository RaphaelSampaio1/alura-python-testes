import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user

 
# Test the application complete ok
def test_serialize_user_complete(): 

    user = {
        "email": "test@example.com",
        "name": "Test User",
        "address": "123 Test St",
        "role": "admin"
    }
    result = serialize_user(user)

    expected = {
        "email": "test@example.com",
        "name": "Test User",
        "address": "123 Test St",
        "role": "admin"
    }

    # Test se o resultado é um dicionário
    assert result == expected, "O resultado deve ser um dicionário com os campos corretos"


# Test the application with missing fields
def test_serialize_missing_fields(): 

    user = {
        "email": "None",
        "name": "",
        "address": "",
        "role": "cliente"
    }
    result = serialize_user(user)

    expected = {
        "email": "None",
        "name": "",
        "address": "",
        "role": "cliente"
    }

    # Test se o resultado é um dicionário
    assert result == expected


# Test the application with int input
def test_serialize_user_int(): 
    with pytest.raises(AttributeError):
        serialize_user(123)


# Test the application with string input
def test_serialize_user_string(): 
    with pytest.raises(AttributeError):
        serialize_user("test string")


# test the application with unexpected values
def test_serialize_user_unexpected():
    user = {
        "email": 123,
        "name": ["Name 1", "Middle Name"],
        "address": {"A": "test A", "B": "teste B"}, 
        "role": True
    }
    result = serialize_user(user)

    expected = {
        "email": 123,
        "name": ["Name 1", "Middle Name"],
        "address": {"A": "test A", "B": "teste B"},
        "role": True
    }
    assert result == expected


# Test all None
def test_serialize_user_allNone():

    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None,
    }
    result = serialize_user(user)

    expected = {
        "email": None,
        "name": None,
        "address": None,
        "role": None,
    }
    assert result == expected


# Test as None input
def test_serialize_user_noneInput():
    
    with pytest.raises(AttributeError):
        user= None
        serialize_user(user)