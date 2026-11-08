# Inventory Stock Control System

## Project Overview

The Inventory Stock Control System is a Python-based application designed to help a business manage its products, monitor stock levels, record sales, and calculate the total value of its inventory.

The system uses Object-Oriented Programming (OOP) through a `Product` class to organize product information and operations.

## Features

- **Add Product:** Register new products with a unique product ID, name, category, unit price, and quantity.
- **Search Product:** Find products using their product ID.
- **Update Stock:** Increase or decrease the quantity of an existing product.
- **Record Sale:** Record product sales and automatically reduce available stock.
- **Low Stock Alert:** Identify products whose quantities are below the low-stock threshold.
- **Inventory Valuation:** Calculate the total value of all products in stock.
- **Display Products:** View all registered products and their details.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling

## How to Run the Project

1. Make sure Python 3 is installed on your computer.
2. Open Command Prompt or a terminal.
3. Navigate to the project folder.
4. Run the following command:

```bash
python main.py
```

## Project Structure

```text
Inventory Stock Control System/
│
├── main.py
└── README.md
```

## Input Validation

The system includes validation to help prevent invalid operations, including:

- Duplicate product IDs.
- Negative product prices.
- Negative stock quantities.
- Selling more products than are available.
- Invalid numerical inputs where handled.

## Data Storage

Product information is stored in a Python dictionary while the program is running. Data is not permanently saved to a database or file.

## Author

**Trevor Danny Gitau**

Software Engineering Student