"""
This program extends Assignment Five and introduces classes + OOP
"""
# Adding a class called DataSet


class DataSet:

    copyright = "No copyright has been set"

    def __init__(self, header=""):
        self.header = header
        self._data = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        max_header_length = 30
        if len(header) <= max_header_length:
            self._header = header
        else:
            raise ValueError


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
    print(f"Options for converting from {base_curr}")
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
    # Header and Copyright Unit Tests
    # Object is created with no header argument
    test1 = DataSet()
    if test1.header == "":
        print("Testing constructor with default parameter: PASS")
    else:
        print("Testing constructor with default parameter: FAIL")

    # Object is created a valid header argument
    test2 = DataSet("This is my header")
    if test2.header == "This is my header":
        print("Testing constructor with valid header argument: PASS")
    else:
        print("Testing constructor with valid header argument: FAIL")

    # Object is created with an invalid header argument
    wrong_head = "This is a very long string that is beyond 30 characters long"
    try:
        DataSet(wrong_head)
        print("Testing constructor with invalid header argument: FAIL")
    except ValueError:
        print("Testing constructor with invalid header argument: PASS")

    # Testing setter in the case of a valid header
    test1.header = "This is a valid header"
    if test1.header == "This is a valid header":
        print("Testing setting with valid argument: PASS")
    else:
        print("Testing setting with valid argument: FAIL")

    # Testing setter in the case of an invalid header
    try:
        test1.header = wrong_head
        print("Testing setting with valid argument: FAIL")
    except ValueError:
        print("Testing setting with valid argument: PASS")

    print("Setting DataSet.copy = 'copyright Oliver Jan'")
    DataSet.copyright = 'copyright Oliver Jan'
    print("Checking that I can access this using DataSet.copyright")
    if DataSet.copyright == 'copyright Oliver Jan':
        print("PASS")
    else:
        print("FAIL")

    print("Checking that I can access this after creating a test object "
          "using test.copyright")
    test = DataSet()
    if test.copyright == 'copyright Oliver Jan':
        print("PASS")
    else:
        print("FAIL")

    print("")


def main():
    """Main obtains the user's name and gives a friendly greeting
    with the provided name
    """
    global home_currency

    DataSet.copyright = "copyright Oliver Jan"
    air_bnb = DataSet()

    name = input("Please enter your name: ")
    print(f"Hi, {name}, welcome to Foothill's database project")

    while home_currency not in conversions:
        try:
            home_currency = input("What is your home currency? ")
        except KeyError:
            continue

    while True:
        try:
            air_bnb.header = input("Enter a header for the menu: ")
            break
        except ValueError:
            continue

    menu(air_bnb)


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


def menu(dataset: DataSet):
    """
    Call the print_menu() function
    Ask the user to input an option
    Take action based on the user input
    """

    currency_options(home_currency)
    print("")
    print(dataset.copyright)
    is_user_inputting = True

    while is_user_inputting:
        print(dataset.header)
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
    main()


r"""
Testing constructor with default parameter: PASS
Testing constructor with valid header argument: PASS
Testing constructor with invalid header argument: PASS
Testing setting with valid argument: PASS
Testing setting with valid argument: PASS
Setting DataSet.copy = 'copyright Oliver Jan
Checking that I can access this using DataSet.copyright
PASS
Checking that I can access this after creating a test object using 
test.copyright
PASS

Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
What is your home currency? USD
Enter a header for the menu: Welcome to the airBNB Database
Options for converting from USD
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

copyright Oliver Jan
Welcome to the airBNB Database
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
What is your choice? 
"""
