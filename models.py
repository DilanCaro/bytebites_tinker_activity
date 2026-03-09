# ByteBites models
# Customer: stores a customer's name and purchase history
# FoodItem: stores item details
# Menu: stores a collection of food items and supports filtering/sorting
# Transaction: stores selected items and computes total cost



class Customer:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchaseHistory = purchase_history if purchase_history is not None else []


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularity_rating

    def __repr__(self):
        return f"FoodItem({self.name}, {self.price}, {self.category}, {self.popularityRating})"


class Menu:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filterByCategory(self, category):
        return [item for item in self.items if item.category == category]

    def sortByPrice(self):
        return sorted(self.items, key=lambda item: item.price)

    def sortByPopularity(self):
        return sorted(self.items, key=lambda item: item.popularityRating, reverse=True)


class Transaction:
    def __init__(self, selected_items=None):
        self.selectedItems = selected_items if selected_items is not None else []

    def computeTotal(self):
        return sum(item.price for item in self.selectedItems)