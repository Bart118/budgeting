#budgeting main file

import account_func

def main_menu():
    """Display user options"""
    print(
        """
        1. Check account balance
        2. Check your savings progress
        3. Log an expense
        4. Log an income
        5. Add a new account
        6. Add a new goal
        7. Change the allocation for one of your goals
        8. Transfer between your accounts
        9. Check your transaction history
        10. Use the budget tool
        11. End program
        """
        )
    choice = int(input("What wouuld you like to do? (1-11) "))
    return choice

#ask user what they want
#############################
#can check account balance - finished#
#edit account names and balance
#can check savings progress
#check account + savings
#can add an expense
#can add an income
#can add an account
#can add a savings goal
#allocate to savings
#can transfer between accounts
#check transaction log
#monthly budget tool (takes info about regular income and expenses and determines a spending plan)
#############################

#check savings progress
###########################
#pulls info from text file and displays amount allocated and the goal for each item
###########################

#check account + savings
###########################
#shows remaining account balance if savings allocations are spent
###########################

#add expense
#############################
#user inputs what they spent, as well as the item they bought
#expense is logged and subtracted from the relevant account
#############################

#add income
#############################
#user inputs income as well as source
#logs the income and adds it to relevant account
#############################

#add account
#############################
#sets up an account that can be used to store income or pay expenses
#############################

#add savings goal
#############################
#sets up a goal to allocate money to, includes the item/goal, amount allocated, and ultimate goal
#############################

#allocate to savings
#############################
#changes the amount allocated to a savings goal
#############################

#transfer between accounts
#############################
#transfers a balance between two accounts
#############################

#check transaction log
#############################
#displays all of the transactions that have taken place
#should eventually include options to display only certain date ranges, income, expense, etc.
#############################

#main loop
end_it = 0

while(end_it == 0):
    choice = main_menu()
    if(choice == 1):
        account_func.check()
    elif(choice == 2):
        print("Checking savings progress...")
    elif(choice == 3):
        print("Logging an expense...")
    elif(choice == 4):
        print("4")
    elif(choice == 5):
        print("5")
    elif(choice == 6):
        print("6")
    elif(choice == 7):
        print("7")
    elif(choice == 8):
        print("8")
    elif(choice == 9):
        print("9")
    elif(choice == 10):
        print("10")
    elif(choice == 11):
        end_it = 1
    else:
        print("Error, please try again")
print("Goodbye")
