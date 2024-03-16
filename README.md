# Culinary Business Manager Using Object-Oriented Design

## Description

This project, titled "Culinary Business Manager Using Object-Oriented Design," is a Python-based application designed to manage and simulate the operations of a culinary business with multiple franchises and diverse menu offerings. It showcases the implementation of object-oriented programming (OOP) principles to model real-world entities and their interactions within a restaurant setting.

## Features

- **Business Modeling:** Represents a business entity that can encompass multiple franchises.
- **Franchise Management:** Each franchise has a unique address and its own set of menus.
- **Menu Management:** Detailed menu management, where each menu is defined by its name, items, and availability times.
- **Dynamic Menu Availability:** Functionality to determine which menus are available at a given time of day.
- **Bill Calculation:** Capability to calculate the bill for a selected list of menu items.

## How to Use

1. **Adding a Franchise:** Create `Franchise` objects by specifying the franchise's address and associated menus.
2. **Creating Menus:** Define various `Menu` objects with specific start and end times, along with a list of items and their prices.
3. **Business Integration:** Aggregate franchises under a `Business` object to represent a cohesive business entity.
4. **Querying Menus:** Use the `available_menus` method of a `Franchise` object to check which menus are available at a given time.
5. **Calculating Bills:** Utilize the `calculate_bill` method in the `Menu` class to calculate the total bill for a chosen list of items.

## Example Usage

```python
# Create menu objects
brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00}, 11, 16)
dinner = Menu("dinner", {'pizza': 11.00, 'salad': 6.00}, 17, 23)

# Create franchise object
flagship_store = Franchise("1232 West End Road", [brunch, dinner])

# Create business object
business = Business("Basta Fazoolin' with my Heart", [flagship_store])

# Check available menus at a given time
print(flagship_store.available_menus(12))  # Output should show the brunch menu

# Calculate bill
print(brunch.calculate_bill(['pancakes', 'waffles']))  # Output should be the total cost of these items
```

## Installation

No additional installation is required. Ensure you have Python installed on your system to run this script.

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE.md).

---

This README provides a comprehensive overview of your project, guiding users on how to interact with your application and demonstrating the core functionalities. Adjust the content as necessary to match the specifics of your implementation and additional features.
