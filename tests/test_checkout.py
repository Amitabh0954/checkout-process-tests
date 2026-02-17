from checkout import add_to_cart, remove_from_cart, calculate_total
import pytest


def test_add_to_cart_with_valid_product():
    cart = []
    product = {"name": "Test Product", "price": 10.0}
    add_to_cart(cart, product)
    assert len(cart) == 1
    assert cart[0]["name"] == "Test Product"
    assert cart[0]["price"] == 10.0


def test_add_to_cart_with_invalid_product():
    cart = []
    product = {"price": 10.0}
    with pytest.raises(KeyError):
        add_to_cart(cart, product)


def test_remove_from_cart_with_existing_product():
    cart = [{"name": "Test Product", "price": 10.0}]
    remove_from_cart(cart, "Test Product")
    assert len(cart) == 0


def test_remove_from_cart_with_non_existing_product():
    cart = [{"name": "Test Product", "price": 10.0}]
    with pytest.raises(ValueError):
        remove_from_cart(cart, "Non-existing Product")


def test_calculate_total_with_empty_cart():
    cart = []
    total = calculate_total(cart)
    assert total == 0.0


def test_calculate_total_with_non_empty_cart():
    cart = [{"name": "Test Product 1", "price": 10.0}, {"name": "Test Product 2", "price": 20.0}]
    total = calculate_total(cart)
    assert total == 30.0
