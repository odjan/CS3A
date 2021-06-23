"""
This program extends Assignment Four and explores the use of f-string
formatting to create ordered tables
"""

conversions = {"USD": 1.0,
               "EUR": 0.9,
               "CAD": 1.4,
               "GBP": 0.8,
               "CHF": 0.95,
               "NZD": 1.66,
               "AUD": 1.62,
               "JPY": 107.92}

home_currency = ""


def currency_options(base_curr: str):
    """
    need to use f-strings to generate the lines of table
    :param base_curr:
    :return:
    """
    # creating the header
    print(f"Options for converting from {base_curr}: ")
    print(f"{base_curr:10}", end='')
    for currency in conversions:
        if currency != base_curr:
            print(f"{currency:10}", end='')
    print("")

    # tabulating the contents of the table
    for i in range(10, 100, 10):
        print(f"{i:<10.2f}", end='')
        for currency in conversions:
            if currency != base_curr:
                converted = currency_converter(i, base_curr, currency)
                print(f"{converted:<10.2f}", end='')
        print("")


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
    global home_currency

    name = input("Please enter your name: ")
    print(f"Hi, {name}, welcome to Foothill's database project")

    while home_currency not in conversions:
        try:
            home_currency = input("What is your home currency? ")
        except KeyError:
            continue
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
    currency_options(home_currency)
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
    main()


r"""
Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
What is your home currency? USD
Options for converting from USD: 
USD       EUR       CAD       GBP       CHF       NZD       AUD       JPY       
10.00     9.00      14.00     8.00      9.50      16.60     16.20     1079.20   
20.00     18.00     28.00     16.00     19.00     33.20     32.40     2158.40   
30.00     27.00     42.00     24.00     28.50     49.80     48.60     3237.60   
40.00     36.00     56.00     32.00     38.00     66.40     64.80     4316.80   
50.00     45.00     70.00     40.00     47.50     83.00     81.00     5396.00   
60.00     54.00     84.00     48.00     57.00     99.60     97.20     6475.20   
70.00     63.00     98.00     56.00     66.50     116.20    113.40    7554.40   
80.00     72.00     112.00    64.00     76.00     132.80    129.60    8633.60   
90.00     81.00     126.00    72.00     85.50     149.40    145.80    9712.80   
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 1
Print Average Rent is under development. Stay tuned!
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 9
Good bye! Thanks for using the database

Process finished with exit code 0
"""
