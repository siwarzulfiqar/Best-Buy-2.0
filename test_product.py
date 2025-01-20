import pytest
import products

# Test that creating a product works
def test_product_creation():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()  # Product should be active initially

# Test when product quantity reaches 0, it becomes inactive
def test_product_inactive_when_quantity_zero():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    product.set_quantity(0)  # Ensure quantity change triggers deactivation
    assert not product.is_active()

# Test that creating a product with invalid details invokes an exception
def test_product_invalid_details():
    with pytest.raises(ValueError):
        products.Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        products.Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

# Test that product purchase modifies the quantity and returns the right output
def test_product_purchase():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert total_price == 14500  # 10 * 1450
    assert product.get_quantity() == 90  # Quantity should decrease by 10

# Test that buying a larger quantity than exists invokes exception
def test_product_purchase_quantity_error():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception):
        product.buy(150)  # Trying to buy more than available stock