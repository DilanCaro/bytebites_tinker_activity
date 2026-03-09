from models import FoodItem, Menu, Transaction


def test_calculate_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 10.0, "Food", 4.7)
    soda = FoodItem("Large Soda", 5.0, "Drinks", 4.2)
    order = Transaction([burger, soda])

    assert order.computeTotal() == 15.0


def test_order_total_is_zero_when_empty():
    order = Transaction([])

    assert order.computeTotal() == 0


def test_filter_menu_items_by_category():
    burger = FoodItem("Spicy Burger", 10.0, "Food", 4.7)
    soda = FoodItem("Large Soda", 5.0, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.0, "Desserts", 4.9)

    menu = Menu([burger, soda, cake])
    drinks = menu.filterByCategory("Drinks")

    assert len(drinks) == 1
    assert drinks[0].name == "Large Soda"


def test_sort_menu_by_price():
    burger = FoodItem("Spicy Burger", 10.0, "Food", 4.7)
    soda = FoodItem("Large Soda", 5.0, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.0, "Desserts", 4.9)

    menu = Menu([burger, soda, cake])
    sorted_items = menu.sortByPrice()

    assert [item.name for item in sorted_items] == [
        "Large Soda",
        "Chocolate Cake",
        "Spicy Burger"
    ]


def test_sort_menu_by_popularity():
    burger = FoodItem("Spicy Burger", 10.0, "Food", 4.7)
    soda = FoodItem("Large Soda", 5.0, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.0, "Desserts", 4.9)

    menu = Menu([burger, soda, cake])
    sorted_items = menu.sortByPopularity()

    assert [item.name for item in sorted_items] == [
        "Chocolate Cake",
        "Spicy Burger",
        "Large Soda"
    ]