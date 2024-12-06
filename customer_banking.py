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
    savings_balance_question = "Enter your initial savings account balance: "
    savings_balance = input(f"{savings_balance_question}")

    # Using check_input_type function to check if the input is a number and if so convert it to a float.
    savings_balance = check_input(savings_balance, float, savings_balance_question)

    # Prompt the user to set the savings interest rate.
    savings_interest_question = "Enter your savings account interest rate.  If 2% enter \"2\", not 0.02 or 2%: "
    savings_interest_rate = input(f"{savings_interest_question}")

    # Using check_input_type function to check if the input is a number and if so convert it to a float.
    savings_interest_rate = check_input(savings_interest_rate, float, savings_interest_question)
    savings_interest_rate = savings_interest_rate / 100

    # Promot the user to enter the number of months for the savings account.
    savings_months_question = "Enter the number of months the money has been in your savings account: "
    savings_months = input(f"{savings_months_question}")

    # Using check_input_type function to check if the input is a number and if so convert it to an int.
    savings_months = check_input(savings_months, int, savings_months_question)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Clear the terminal
    os.system('cls')

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your savings account earned ${savings_interest_earned:,.2f} in interest over {savings_months}.")
    print(f"Your updated savings account balance is ${updated_savings_balance:,.2f}.\n\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance_question = "Enter your initial CD account balance: "
    cd_balance = input(f"{cd_balance_question}")

    # Using check_input_type function to check if the input can be converted to a float.
    cd_balance = check_input(cd_balance, float, cd_balance_question)

    # Promt the user to enter the CD interest rate.
    cd_interest_question = "Enter your CD account interest rate.  If 2% enter \"2\", not 0.02 or 2%: "
    cd_interest = input(f"{cd_interest_question}")

    # Using check_input_type function to check if the input can be converted to a float.
    cd_interest = check_input(cd_interest, float, cd_interest_question)
    cd_interest = cd_interest / 100

    # Prompt the user to enter the number of months for the CD account.
    cd_maturity_question = "Enter the number of months the money has been in your CD account: "
    cd_maturity = input(f"{cd_maturity_question}")

    # Using check_input_type function to check if the input can be converted to an int.
    cd_maturity = check_input(cd_maturity, int, cd_maturity_question)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Clear the terminal
    os.system('cls')

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your CD account earned ${cd_interest_earned:,.2f} in interest over {cd_maturity}.")
    print(f"Your updated CD account balance is ${updated_cd_balance:,.2f}.")

if __name__ == "__main__":
    # Call the main function.
    main()
