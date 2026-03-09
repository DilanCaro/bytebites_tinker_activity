# ByteBites Design Document

ByteBites is a food-ordering backend system composed of exactly four classes:
`Customer`, `FoodItem`, `Menu`, and `Transaction`.

## Primary Diagram

```mermaid
classDiagram
    class Customer {
        +name : String
        +purchaseHistory : List~Transaction~
    }

    class FoodItem {
        +name : String
        +price : float
        +category : String
        +popularityRating : float
    }

    class Menu {
        +items : List~FoodItem~
        +filterByCategory(category : String) List~FoodItem~
        +sortByPrice() List~FoodItem~
        +sortByPopularity() List~FoodItem~
    }

    class Transaction {
        +selectedItems : List~FoodItem~
        +computeTotal() float
    }

    Customer "1" --> "0..*" Transaction : purchase history
    Menu "1" --> "0..*" FoodItem : contains
    Transaction "1" --> "0..*" FoodItem : selected items