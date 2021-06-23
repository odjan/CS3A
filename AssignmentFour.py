"""
This program extends Assignment Three and has unit testing to
evaluate the efficacy of a currency_converter function reading
from a conversion dictionary
"""

conversions = {"USD": 1.0,
               "EUR": 0.9,
               "CAD": 1.4,
               "GBP": 0.8,
               "CHF": 0.95,
               "NZD": 1.66,
               "AUD": 1.62,
               "JPY": 107.92}


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """
    Args:
        :param quantity: float that represents the amount of currency
        :param source_curr: original source of currency
        :param target_curr: currency after exchange
    :return:
    """
    if source_curr not in conversions:
        raise KeyError
    if target_curr not in conversions:
        raise KeyError

    usd_convert = quantity / conversions[source_curr]
    target_convert = usd_convert * conversions[target_curr]
    return target_convert


def unit_test():
    # User enters invalid source currency should raise KeyError
    try:
        currency_converter(10, "ZIM", "USD")
        print("FAIL, Source currency KeyError is not raised")
    except KeyError:
        print("PASS, Source currency KeyError is raised")

    # User enters invalid target currency should raise KeyError
    try:
        currency_converter(10, "USD", "NTD")
        print("FAIL, Target Currency KeyError is not raised")
    except KeyError:
        print("PASS, Target Currency KeyError is raised")

    # Correct conversion from USD to another currency with quantity > 1
    if currency_converter(10, "USD", "CAD") == 14:
        print("PASS, USD to another currency is correct")
    else:
        print("FAIL, USD to another currency is incorrect")

    # Correct conversion from another currency to USD with quantity > 1
    if currency_converter(3.24, "AUD", "USD") == 2.0:
        print("PASS, conversion to USD is correct")
    else:
        print("FAIL, conversion to USD is incorrect")

    # Correct conversion between two non-USD currencies with quantity > 1
    if currency_converter(100, "GBP", "EUR") == 112.5:
        print("PASS, conversion between two non-USD currencies is correct")
    else:
        print("FAIL, conversion between two non-USD currencies is incorrect")


def main():
    """Main obtains the user's name and gives a friendly greeting
    with the provided name
    """
    name = input("Please enter your name: ")
    print(f"Hi, {name}, welcome to Foothill's database project")
    menu()


def print_menu():
    """ Print out nine choices for user to select"""
    print("Main Menu")
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu():
    """
    Call the print_menu() function
    Ask the user to input an option
    Take action based on the user input
    """
    is_user_inputting = True

    while is_user_inputting:
        print_menu()

        raw_choice = input("What is your choice? ")
        try:
            choice = int(raw_choice)
        except ValueError:
            print("Next time, please enter a number")
            continue

        if choice >= 10 or choice < 1:
            print("Please input numbers ranging from 1 to 9")
        elif choice == 1:
            print("Print Average Rent is under development. Stay tuned!")
        elif choice == 2:
            print("Print Minimum Rent is not ready yet. Stay tuned!")
        elif choice == 3:
            print("Print Maximum Rent coming soon!")
        elif choice == 4:
            print("Print Min/Avg/Max by Location not implemented yet")
        elif choice == 5:
            print("We're still working on this feature! Stay tuned!")
        elif choice == 6:
            print("Adjust Location Filters sounds like a cool feature")
        elif choice == 7:
            print("Adjust Property Type Filters coming soon!")
        elif choice == 8:
            print("You'll get to load data soon!")
        elif choice == 9:
            print("Good bye! Thanks for using the database")
            is_user_inputting = False


if __name__ == "__main__":
    unit_test()


r"""
PASS, Source currency KeyError is raised
PASS, Target Currency KeyError is raised
PASS, USD to another currency is correct
PASS, conversion to USD is correct
PASS, conversion between two non-USD currencies is correct
"""
