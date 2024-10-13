# Bank App

This project is a simple Bank Application developed using Python's `tkinter` library. It provides a graphical user interface (GUI) for users to create a bank account, log in, deposit money, and transfer funds to other users.

## Features

- Create Account: Users can create an account by entering their name, password, and an initial deposit amount.
- Login Account: Existing users can log in using their credentials.
- Deposit Funds: After logging in, users can deposit money into their account.
- Transfer Funds: Users can transfer funds to other registered accounts.
- Balance Display: Users can view their current balance after login and following transactions.

## Project Structure

The project is structured with different functions to manage account creation, login, and transactions:

- Main Window: The main window has options for account creation and login.
- Login Window: Allows users to log in to their accounts with a name and password.
- Dashboard Window: Displays the user's current balance and offers options to deposit or transfer funds.
- Deposit Window: Enables users to deposit funds into their account.
- Transfer Window: Allows users to transfer money to another registered account.

## Code Overview

1. Main Window Initialization:  
   - Sets up the main window with options to create an account or log in.

2. Account Creation (`createAccount` function):  
   - Opens a new window where users can enter a name, password, and initial amount.
   - If valid, stores account data in the `Database` list.

3. Login (`loginaccount` function):  
   - Opens a login window where users can enter their name and password.
   - If credentials match, proceeds to open the dashboard.

4. Dashboard (`enterApp` function):  
   - Displays the current balance and provides options to deposit or transfer funds.
   - Includes `deposit` and `transfer` functions for respective transactions.

5. Deposit and Transfer Functions:  
   - The `deposit` function allows users to add money to their account.
   - The `transfer` function enables users to transfer funds to another account if they have sufficient balance.

## Running the Application

To run this application:
1. Ensure Python and `tkinter` are installed.
2. Run the script:
   ```bash
   python bank_app.py
   ```
3. The main window will open, allowing you to create an account or log in.

## Usage

1. Create an Account:  
   - Click "Create an Account" in the main window.
   - Enter your name, password, and an initial amount.
   - After account creation, the window will close, and you can log in with your new credentials.

2. Log In:  
   - Click "Login into Account."
   - Enter your name and password, then click "Ok."
   - If credentials are correct, you'll be directed to the dashboard.

3. Deposit Funds:  
   - Click "Deposit Amount" on the dashboard.
   - Enter the deposit amount, and it will be added to your balance.

4. Transfer Funds:  
   - Click "Transfer Amount."
   - Enter the amount and the recipient's name.
   - If the recipient exists and you have enough funds, the transfer will be completed.

## Dependencies

- **Python 3**
- **tkinter library** (usually included with Python installations)

## Notes

- This app does not use persistent storage, so account data will reset each time the app is restarted.
- This application is intended for educational purposes and is not secure for actual banking use.

## Author

Developed by Karan Moktan

## License

This project is open-source and available for modification and distribution.
