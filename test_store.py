import pytest
import products
import store


def test_add_product():
    """Test adding a product to the store."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    ]
    my_store = store.Store(product_list)
    new_product = products.Product("Google Pixel 7", price=500, quantity=250)

    # Add new product to store
    my_store.add_product(new_product)

    # Check if the new product is in the store's product list
    all_products = my_store.get_all_products()
    assert len(all_products) == 3  # We should have 3 products now
    assert any(product.name == "Google Pixel 7" for product in all_products)  # Check if product is added


def test_remove_product():
    """Test removing a product from the store."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    ]
    my_store = store.Store(product_list)
    product_to_remove = my_store.get_all_products()[0]  # Get the first product

    # Remove product from store
    my_store.remove_product(product_to_remove)

    # Check if the product is removed
    all_products = my_store.get_all_products()
    assert len(all_products) == 1  # We should have 1 product now
    assert product_to_remove not in all_products  # Check if product is removed


def test_order():
    """Test placing an order and calculating the total price."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    ]
    my_store = store.Store(product_list)

    # Create shopping list for order
    shopping_list = [(my_store.get_all_products()[0], 2), (my_store.get_all_products()[1], 1)]

    # Calculate total price of the order
    total_price = my_store.order(shopping_list)

    # The expected total price = 2 * 1450 + 250 = 3050
    assert total_price == (1450 * 2 + 250)


def test_product_inactive_when_quantity_zero():
    """Test that a product becomes inactive when its quantity is 0."""
    product = products.Product("MacBook Air M2", price=1450, quantity=0)
    assert not product.is_active()  # Product should be inactive


def test_buy_more_than_available_quantity():
    """Test buying more than available quantity should raise an exception."""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=10)]
    my_store = store.Store(product_list)

    # Try to buy more products than available (10 available, trying to buy 20)
    shopping_list = [(my_store.get_all_products()[0], 20)]

    # It should raise an exception because the quantity exceeds available stock
    with pytest.raises(Exception, match="Not enough stock to complete the purchase."):
        my_store.order(shopping_list)


if __name__ == "__main__":
    pytest.main()
