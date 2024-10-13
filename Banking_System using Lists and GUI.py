from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bank App")
window.geometry("800x800")
window.configure(bg="Orange")
Database = []
label = Label(window, text="Bank App", font=("Poppins", 25), height=5, fg="white")
label.pack()
label.configure(bg="Orange")

def loginaccount():
    login = Tk()
    login.title("Login Account")
    login.geometry("800x800")
    login.configure(bg="Orange")
    
    label = Label(login, text="Login Account", font=("Poppins", 25), height=5, fg="white", bg="orange")
    label.pack()
    
    # Entry for username and password
    name_label = Label(login, text="Name", font=("Poppins", 15), height=5, fg="white", bg="orange")
    name_label.pack()
    name_entry = Entry(login)
    name_entry.pack()
    
    pass_label = Label(login, text="Password", font=("Poppins", 15), height=5, fg="white", bg="orange")
    pass_label.pack()
    pass_entry = Entry(login, show="*")
    pass_entry.pack()

    def enterApp():
        # Extract name and password input
        entered_name = name_entry.get()
        entered_password = pass_entry.get()
        account_found = False

        # Check if entered credentials exist in the Database
        for account in Database:
            if account[0] == entered_name and account[1] == entered_password:
                account_found = True
                login.destroy()  # Close the login window
                break
        
        if account_found:
            App = Tk()
            App.title("App")
            App.geometry("800x800")
            App.configure(bg="orange")

            Label(App, text="DashBoard", font=("Poppins", 25), fg="white", height=3, bg="orange").pack()

            # Display current balance label
            balance_label = Label(App, text=f"Current Balance: {account[2]}", font=("Poppins", 25), fg="white", bg="orange")
            balance_label.pack()

            # Deposit function
            def deposit():
                deposit_window = Tk()
                deposit_window.title("Deposit Amount")
                deposit_window.geometry("800x800")
                deposit_window.configure(bg="orange")

                Label(deposit_window, text="Amount", font=("Poppins", 25), fg="white", height=3, bg="orange").pack()
                amount_entry = Entry(deposit_window)
                amount_entry.pack()

                def calculate():
                    try:
                        deposit_amount = int(amount_entry.get())
                        account[2] += deposit_amount
                        balance_label.config(text=f"Current Balance: {account[2]}")
                        messagebox.showinfo("Success", "Amount Deposited Successfully")
                        deposit_window.after(1200, deposit_window.destroy)  # Close after 1.2 seconds
                    except ValueError:
                        messagebox.showwarning("Invalid Input", "Please enter a valid amount.")

                depB = Button(deposit_window, text="Deposit", command=calculate, font=("Poppins", 15))
                depB.pack()
                depB.configure(bg="orange", fg="white")

            # Transfer function
            def transfer():
                transfer_window = Tk()
                transfer_window.title("Money Transfer")
                transfer_window.geometry("800x800")
                transfer_window.configure(bg="orange")

                Label(transfer_window, text="Transfer Amount", font=("Poppins", 25), fg="white", height=3, bg="orange").pack()
                amount_entry = Entry(transfer_window)
                amount_entry.pack()
                
                Label(transfer_window, text="Recipient Account Name", font=("Poppins", 25), fg="white", height=3, bg="orange").pack()
                recipient_entry = Entry(transfer_window)
                recipient_entry.pack()

                def execute_transfer():
                    try:
                        transfer_amount = int(amount_entry.get())
                        recipient_name = recipient_entry.get()

                        if transfer_amount <= 0:
                            messagebox.showwarning("Invalid Amount", "Transfer amount must be positive.")
                            return
                        
                        if account[2] < transfer_amount:
                            messagebox.showwarning("Insufficient Funds", "You do not have enough balance for this transfer.")
                            return

                        recipient_found = False
                        for recipient_account in Database:
                            if recipient_account[0] == recipient_name:
                                recipient_account[2] += transfer_amount
                                account[2] -= transfer_amount
                                balance_label.config(text=f"Current Balance: {account[2]}")
                                messagebox.showinfo("Transfer Successful", f"{transfer_amount} transferred to {recipient_name}")
                                transfer_window.after(1200, transfer_window.destroy)
                                recipient_found = True
                                break
                        
                        if not recipient_found:
                            messagebox.showwarning("Error", "Recipient account not found.")
                    
                    except ValueError:
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for the amount.")

                transfer_button = Button(transfer_window, text="Transfer", command=execute_transfer, font=("Poppins", 15))
                transfer_button.pack()
                transfer_button.configure(bg="orange", fg="white")

            # Deposit and Transfer Buttons
            deposit_button = Button(App, text="Deposit Amount", command=deposit, font=("Poppins", 15))
            deposit_button.pack()
            deposit_button.configure(bg="orange", fg="white")
            
            transfer_button = Button(App, text="Transfer Amount", command=transfer, font=("Poppins", 15))
            transfer_button.pack()
            transfer_button.configure(bg="orange", fg="white")

        else:
            messagebox.showwarning("Error", "Your Account Does Not Exist")

    process_button = Button(login, text="Ok", command=enterApp, bg="orange", fg="white", font=("Poppins", 15))
    process_button.pack()

# Create Account Function
def createAccount():
    create_window = Tk()
    create_window.title("Create Account")
    create_window.geometry("800x800")
    create_window.configure(bg="Orange")
    
    Label(create_window, text="Create an Account", font=("Poppins", 25), height=5, fg="white", bg="orange").pack()
    name_label = Label(create_window, text="Name", font=("Poppins", 15), height=5, fg="white", bg="orange")
    name_label.pack()
    name_entry = Entry(create_window)
    name_entry.pack()

    pass_label = Label(create_window, text="Password", font=("Poppins", 15), height=5, fg="white", bg="orange")
    pass_label.pack()
    pass_entry = Entry(create_window, show="*")
    pass_entry.pack()

    amount_label = Label(create_window, text="Amount", font=("Poppins", 15), height=5, fg="white", bg="orange")
    amount_label.pack()
    amount_entry = Entry(create_window)
    amount_entry.pack()

    def process_creation():
        try:
            name = name_entry.get()
            password = pass_entry.get()
            initial_amount = int(amount_entry.get())
            
            if not name or not password:
                messagebox.showwarning("Error", "Name and Password are required.")
                return

            Database.append([name, password, initial_amount])
            messagebox.showinfo("Success", "Account Created Successfully")
            create_window.after(1000, create_window.destroy)
        
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for the initial amount.")

    create_button = Button(create_window, text="Ok", command=process_creation, bg="orange", fg="white", font=("Poppins", 15))
    create_button.pack()

create_account_button = Button(window, text="Create an Account", command=createAccount, font=("Poppins", 15), bg="orange", fg="white")
create_account_button.pack()

login_button = Button(window, text="Login into Account", command=loginaccount, font=("Poppins", 15), bg="orange", fg="white")
login_button.pack()

window.mainloop()
