# Retail Store Management System

## Project Overview:
This Retail Store Management System is a Python application designed to manage employees, items, and purchases in a retail environment. It features a robust database integration using SQLite to handle data persistence, with functionalities to add, manage, and view employees and items. Additionally, it supports purchasing items with employee discounts.

## Features:
- **Employee Management**: Add and view employees, including details such as name, type, years worked, and unique discount number.
- **Item Management**: Add and display items with their costs.
- **Purchase Management**: Employees can make purchases with automatic discount calculations based on their years of service and role.
- **Database Integration**: Utilizes SQLite for data storage, ensuring that all information is persistently stored and retrieved.

## Installation:
Ensure Python and SQLite are installed on your machine. Clone the repository:
```bash
git clone https://github.com/YasamanMVS/Semester4-Python-RetailStore.git
cd RetailStore
```
Run the setup script to install dependencies and set up the database:
```bash
python setup.py install
python database.py
```
## Usage:
Run the main application to interact with the system through the command line interface:
```bash
python main.py
```
Follow the on-screen prompts to navigate through the menu for managing employees, items, and purchases.

## Project Structure:
- **main.py**: Orchestrates user interactions and menu navigation.
- **database.py**: Handles database connections and schema creations.
- **employee_management.py**: Contains functions to manage employee information.
- **item_management.py**: Functions to add and list items in the store.
- **purchase_management.py**: Manages purchase transactions with discount calculations.
