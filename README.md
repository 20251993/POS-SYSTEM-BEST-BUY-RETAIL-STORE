## Authors:
Shanese Downer
## Date Created:
April 5, 2026
## Course:
ITT103
## GitHub Public URL to Code:
[https://github.com/20251993/POS-SYSTEM-BEST-BUY-RETAIL-STORE/blob/main/Downer.Shanese-POS-ITT103-SP2026.py%20.py](https://github.com/20251993/POS-SYSTEM-BEST-BUY-RETAIL-STORE/blob/main/AsyncAvengers-POS-ITT103-SP2026.py)

## The Purpose of the Program
This program simulates a Point of Sale (POS) system for a retail store. It allows cashiers to add items to a cart, remove items, view purchases, process payments, and generate receipts for customers.
## How to Run the Program
1. Open the program in PyCharm
2. Run the file (main.py)
3. Follow the menu options displayed on the screen
## The following features and improvements were made in the POS system:
- Created a product catalog using a dictionary to store product name, price, and stock quantity.
- Added the ability for users to add items to the shopping cart with stock checks.
- Added an option to remove items from the cart.
- Created a feature to view the cart, showing items, quantities, and subtotal.
- Built a checkout system that calculates the subtotal, adds 10% tax, and gives a 5% discount for totals over $5000.
- Included payment processing with checks to ensure correct entries.
- Made sure the system verifies enough payment before completing transactions.
- Created a function to generate a receipt that summarizes purchases in a clear format.
- Used loops to allow ongoing transactions until the user decides to exit the system.
- Included error handling with try and except to avoid program crashes.
- Structured the program with functions for better readability and organization.
## Assumptions
- User enters valid product names
- Prices and Stock are predefined
- system runs in a console instead of a GUI
## Limitations of Operations
- Data resets when program stops
- There is no option to scan barcode
- Limited to one user per account
