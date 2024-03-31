# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
from Input_Type_Check import check_input
import os

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance_question = "What is the balance on your savings account?"
    savings_balance = input(f"{savings_balance_question} ")

    # Check that the input can be converted to a float and if so do so.
    savings_balance = check_input(savings_balance, float, savings_balance_question)
    
    savings_interest_rate_question = "What is the interest rate on your savings account? If 2% enter \"2\", not 0.02 or 2%:"
    savings_interest_rate = input(f"{savings_interest_rate_question} ")

    # Check that the input can be converted to a float and if so do so.
    savings_interest_rate = check_input(savings_interest_rate, float, savings_interest_rate_question)
    savings_interest_rate = savings_interest_rate/100

    savings_months_question = "How many months has this money been in your savings account?"
    savings_months = input(f"{savings_months_question} ")

    # Check that the input can be converted to a int and if so do so.
    savings_months = check_input(savings_months, int, savings_months_question)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Clear the console
    os.system("cls")

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your savings account earned ${savings_interest_earned:,.2f} in interest over {savings_months} months.")
    print(f"Bringing your total savings account balnce to: ${updated_savings_balance:,.2f}.\n\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance_question = "What is the balance on your CD account?"
    cd_balance = input(f"{cd_balance_question} ")

    # Check that the input can be converted to a float and if so do so.
    cd_balance = check_input(cd_balance, float, cd_balance_question)

    cd_interest_rate_question = "What is the interest rate on your CD account? If 2% enter \"2\", not 0.02 or 2%: "
    cd_interest_rate = input(f"{cd_interest_rate_question}" )

    # Check that the input can be converted to a float and if so do so.
    cd_interest_rate = check_input(cd_interest_rate, float, cd_interest_rate_question)
    cd_interest_rate = cd_interest_rate/100

    cd_months_quesiton = "How many months has this money been in your CD account?"
    cd_months = input(f"{cd_months_quesiton} ")

    # Check that the input can be converted to a int and if so do so.
    cd_months = check_input(cd_months, int, cd_months_quesiton)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Clear the console
    os.system("cls")

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your CD earned ${cd_interest_earned:,.2f} in interest over {cd_months} months.")
    print(f"Bringing your total CD account balnce to: ${updated_cd_balance:,.2f}.")

if __name__ == "__main__":
    # Call the main function.
    main()