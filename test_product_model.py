"""
Crie casos de teste para garantir que a função serialize_product():

Retorna todos os campos esperados corretamente.

Aplica os valores padrão para os campos opcionais (available e ingredients).

Converte corretamente o campo _id para uma string.
"""

"""
Best test cases:

Happy path — correct input → expected output.
Defaults/optional fields — omit keys and assert defaults.
Empty/null values — "", None, empty list/dict.
Wrong types — number instead of string, list instead of dict, etc. (assert behavior, not implementation).
Conversions/serialization — verify type transforms (e.g., id -> str).
Minimal input / missing keys — empty dict or partial dict.
Edge values (if numeric) — 0, negative, extreme floats.
Determinism/idempotence — calling twice returns same result.
Parametrize similar cases with pytest.mark.parametrize to avoid duplicate tests.
Clear assertions — assert specific fields, not only whole-dict equality when debugging is needed.
"""

import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # this get the __init__.py
from models.product_model import serialize_product


# Standard test
def test_product_standard():
    product ={
        "id": "id_test123",
        "name": "Iphone 17 Pro",
        "description": "Expensive product",
        "category": "Smartphone",
        "price": 1200.88,
        "available": True,
        "ingredients": ["Charger", "Earphone"]
    }

    result = serialize_product(product)

    expected = {
        "id": "id_test123",
        "name": "Iphone 17 Pro",
        "description": "Expensive product",
        "category": "Smartphone",
        "price": 1200.88,
        "available": True,
        "ingredients": ["Charger", "Earphone"]
    }
    assert result==expected


# Test if default values as available and ingredients will be filled by default as expected
def test_product_default_parameters():
    product ={
        "id": 123,
        "name": "Test",
        "description": None,
        "category": "None",
        "price": None,
        # Available and Ingredients missing
    }

    result = serialize_product(product)

    assert result['available'] == True 
    assert result['ingredients'] == []
    assert result['id'] == "123" # Convert to text


def test_product_partial_fields():
    product={
        "id": 999,
        "name": "Test Name",
        "price": 10.58
    }
    result = serialize_product(product)

    assert result['id'] == "999"
    assert result['name'] == "Test Name"
    assert result['price'] == 10.58
    assert result['description'] is None
    assert result['available'] == True
    assert result['category'] is None
    assert result['ingredients'] == []


def test_product_empty_dict():
    product = {}
    result = serialize_product(product)

    assert result["id"] == "None"
    assert result["name"] is None
    assert result["description"] is None
    assert result["category"] is None
    assert result["price"] is None
    assert result["available"] == True
    assert result["ingredients"] == []
