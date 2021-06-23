"""
This program extends Assignment Six and has list operations
"""
# Adding a class called DataSet


class EmptyDatasetError(Exception):
    pass


class NoMatchingItems(Exception):
    pass


class DataSet:

    copyright = "No copyright has been set"

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""

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

    def _cross_table_statistics(self, borough: str, property_type: str):
        """

        :param borough: borough
        :param property_type:
        :return: successful return yields tuple (minimum, average, and maximum)
        otherwise, EmptyDatasetError is raised or NoMatchingExceptions
        """
        if self._data is None:
            raise EmptyDatasetError

        rents = [entry[2] for entry in self._data if entry[0] == borough
                 and entry[1] == property_type]

        if len(rents) == 0:
            raise NoMatchingItems

        return min(rents), sum(rents)/len(rents), max(rents)

    def load_default_data(self):
        self._data = [("Staten Island", "Private room", 70),
                      ("Brooklyn", "Private room", 50),
                      ("Bronx", "Private room", 40),
                      ("Brooklyn", "Entire home/apt", 150),
                      ("Manhattan", "Private room", 125),
                      ("Manhattan", "Entire home/apt", 196),
                      ("Brooklyn", "Private room", 110),
                      ("Manhattan", "Entire home/apt", 170),
                      ("Manhattan", "Entire home/apt", 165),
                      ("Manhattan", "Entire home/apt", 150),
                      ("Manhattan", "Entire home/apt", 100),
                      ("Brooklyn", "Private room", 65),
                      ("Queens", "Entire home/apt", 350),
                      ("Manhattan", "Private room", 98),
                      ("Brooklyn", "Entire home/apt", 200),
                      ("Brooklyn", "Entire home/apt", 150),
                      ("Brooklyn", "Private room", 99),
                      ("Brooklyn", "Private room", 120)]


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


def unit_test():
    my_set = DataSet()

    print("Testing _cross_table_statistics")
    try:
        my_set._cross_table_statistics("Brooklyn", "Apt")
        print("--> Method Raises EmptyDataSet Error: Fail")
    except EmptyDatasetError:
        print("--> Method Raises EmptyDataSet Error: Pass")

    my_set.load_default_data()
    brooklyn_data = my_set._cross_table_statistics("Brooklyn", "Private room")

    try:
        my_set._cross_table_statistics("Brooklyn", "Stadium")
        print("--> Invalid Property Type Raises NoMatchingItems Error: Fail")
    except NoMatchingItems:
        print("--> Invalid Property Type Raises NoMatchingItems Error: Pass")

    try:
        my_set._cross_table_statistics("Seattle", "Private room")
        print("--> Invalid Borough Raises NoMatchingItems Error: Fail")
    except NoMatchingItems:
        print("--> Invalid Borough Raises NoMatchingItems Error: Pass")

    try:
        my_set._cross_table_statistics("Bronx", "Entire home/apt")
        print("--> No Matching Rows Raises NoMatchingItems Error: Fail")
    except NoMatchingItems:
        print("--> No Matching Rows Raises NoMatchingItems Error: Pass")

    if my_set._cross_table_statistics("Bronx", "Private room") == (40, 40, 40):
        print("--> One Matching Row Returns Correct Tuple: Pass")
    else:
        print("--> One Matching Row Returns Correct Tuple: Fail")

    # print(brooklyn_data) shows (50, 88.8, 120)
    if my_set._cross_table_statistics("Brooklyn", "Private room") \
            == brooklyn_data:
        print("--> Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("--> Multiple Matching Rows Returns Correct Tuple: Fail")


if __name__ == "__main__":
    unit_test()


r"""
Testing _cross_table_statistics
--> Method Raises EmptyDataSet Error: Pass
--> Invalid Property Type Raises NoMatchingItems Error: Pass
--> Invalid Borough Raises NoMatchingItems Error: Pass
--> No Matching Rows Raises NoMatchingItems Error: Pass
--> One Matching Row Returns Correct Tuple: Pass
--> Multiple Matching Rows Returns Correct Tuple: Pass
"""
