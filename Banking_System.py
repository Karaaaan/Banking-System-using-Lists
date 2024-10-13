# Print the main interface options for the banking system
print("<---------------------NOOB_BANKING__SYSTEM------------------------------------->\n")
print("<1---Create__ACCOUNT--->\n")
print("<2---Login__ACCOUNT---->\n")

# Initialize the account list to store user account information
accList = []

# Function to deposit money into the user's account
def deposit():
    # Prompt the user for their username and the amount to deposit
    userName = input("<----ENTER__USERNAME__AGAIN---->\n")
    amount = int(input("<---ENTER_AMOUNT__TO__DEPOSIT------->\n"))
    
    # Iterate through the list of accounts
    for acc in accList:
        if acc[2] == userName:  # Check if the username matches any account
            acc[3] += amount    # Add the deposit amount to the user's balance
            print(f"New balance for {userName}: {acc[3]}")
            return  # Exit the function after deposit is successful
    
    # If no account matches the username, print an error message
    print("<---USER__NOT__FOUND--->")

# Function to transfer money between accounts
def transfer():
    # Prompt the sender for their username and the transfer amount
    sender = input("<---ENTER_YOUR_USERNAME-------------->\n")
    amount = int(input("<---ENTER_AMOUNT__TO__TRANSFER------->\n"))
    # Prompt for the recipient's username
    receiver = input("<---ENTER_RECIPIENT_USERNAME-------------->\n")
    
    # Variables to track if the sender and receiver accounts are found
    sender_found = False
    receiver_found = False

    # Iterate through the account list to find the sender
    for acc in accList:
        if acc[2] == sender:
            sender_found = True
            if acc[3] >= amount:  # Check if the sender has enough balance
                # If the sender is found and has sufficient balance, find the recipient
                for acc2 in accList:
                    if acc2[2] == receiver:
                        receiver_found = True
                        acc[3] -= amount   # Deduct the amount from the sender's balance
                        acc2[3] += amount  # Add the amount to the receiver's balance
                        print(f"Transfer Successful! New balance for {sender}: {acc[3]}")
                        print(f"New balance for {receiver}: {acc2[3]}")
                        return  # Exit the function after successful transfer
                # If recipient not found, print an error message
                if not receiver_found:
                    print("<---RECIPIENT__NOT__FOUND--->")
                    return
            else:
                print("<---INSUFFICIENT__BALANCE--->")
                return
    # If sender is not found, print an error message
    if not sender_found:
        print("<---SENDER__NOT__FOUND--->")

# Function to create a new account
def createAccount():
    # Prompt the user for first name, last name, username, and initial deposit
    fname = input("<---ENTER__YOUR__FIRST__NAME--->\n")
    lname = input("<---ENTER__YOUR__LAST___NAME--->\n")
    userName = input("<-----ENTER__A__USERNAME---->\n")
    balance = int(input("<----DEPOSIT__AN__AMOUNT----->\n"))
    
    # Store the user's details in a list and add it to the account list
    group = [fname, lname, userName, balance]
    accList.append(group)
    print("<---ACCOUNT__CREATED--->")
    print(accList)  # Display the current account list for debugging

# Function to log in to an existing account
def loginAccount():
    # Prompt the user for their username
    userName = input("<-----ENTER__YOUR__USERNAME---->\n")
    
    # Iterate through the account list to check if the username exists
    for details in accList:
        if details[2] == userName:  # If username matches, login is successful
            print("<------LOGIN__SUCCESSFUL------->\n")
            print("<-------WHAT__WOULD__YOU__LIKE__TO__DO?------------>\n")        
            print("<1---DEPOSIT--->\n")
            print("<2---TRANSFER---->\n")
            # Prompt the user to choose between deposit and transfer options
            answer = int(input("<----CHOOSE_AN_OPTION------>\n"))
            if answer == 1:
                deposit()  # Call the deposit function
            elif answer == 2:
                transfer()  # Call the transfer function
            return  # Exit after the operation is completed 
    
    # If the username is not found, print a login failure message
    print("<----LOGIN__FAILED---->\n")

# Main program loop
while True:
    # Prompt the user to choose between creating an account or logging in
    choose = int(input("----Choose__an__option---:\n"))
    if choose == 1:
        createAccount()  # Call the account creation function
    elif choose == 2:
        print("<----ENTER___CREDENTIALS----->")
        loginAccount()  # Call the login function
