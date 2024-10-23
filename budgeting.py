#budgeting main file

import bud_disp, bud_file_func

#ask user what they want
#############################
#can check account balance
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


#check account balance
############################
#grabs info from text file and displays the information
############################

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
    bud_disp.main_menu()
    end_it = int(input("Enter 0 to choose again or 1 to exit "))
print("Goodbye")
