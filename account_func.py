#budgeting account functions
import bud_file_func, bud_disp

def check():
    print("Checking account balance...")
    balance = bud_file_func.read_data("accounts.txt")
    bud_disp.balance(balance)
