"""
This program extends Assignment Nine and builds a Location and Property
type filter.
"""
# Adding a class called DataSet

from enum import Enum


class EmptyDatasetError(Exception):
    pass


class NoMatchingItems(Exception):
    pass


class DataSet:

    class Categories(Enum):
        LOCATION = 0
        PROPERTY_TYPE = 1

    class Stats(Enum):
        MIN = 0
        AVG = 1
        MAX = 2

    copyright = "No copyright has been set"

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""
        self._labels = {DataSet.Categories.LOCATION: set(),
                        DataSet.Categories.PROPERTY_TYPE: set()}
        self._active_labels = {DataSet.Categories.LOCATION: set(),
                               DataSet.Categories.PROPERTY_TYPE: set()}

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

    def get_labels(self, category: Categories):
        """ returns a list of the items in _labels[category] """
        return [item for item in self._labels[category]]

    def get_active_labels(self, category: Categories):
        """ returns a list of the items in _active_labels[category] """
        return [item for item in self._active_labels[category]]

    def toggle_active_label(self, category: Categories, descriptor: str):
        """ method to add or remove labels from _active_labels"""
        if descriptor in self.get_labels(category):
            if descriptor in self.get_active_labels(category):
                self._active_labels[category].remove(descriptor)
                print(f"{descriptor} removed from active_labels")
            else:
                self._active_labels[category].add(descriptor)
                print(f"{descriptor} added to active_labels")

        else:
            raise KeyError("descriptor not there")

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

    def _table_statistics(self, row_category: Categories, label: str):
        """
        Calculate filtered min, avg, and max values
        :param row_category: type DataSet.Categories; location or property type
        :param label: specific label that we are looking for, i.e. Manhattan
        :return: successful return yields a tuple of (min, avg, and max)
        """
        if self._data is None:
            raise EmptyDatasetError

        if row_category == DataSet.Categories.PROPERTY_TYPE:
            specifier = DataSet.Categories.LOCATION
            rents = [entry[2] for entry in self._data if entry[1] == label and
                     entry[0] in list(self._active_labels[specifier])]
        else:
            specifier = DataSet.Categories.PROPERTY_TYPE
            rents = [entry[2] for entry in self._data if entry[0] == label and
                     entry[1] in list(self._active_labels[specifier])]

        # print(row_category)
        # print(specifier)
        # print(self._active_labels[DataSet.Categories.PROPERTY_TYPE])
        # print(label)
        # print(rents)

        if len(rents) == 0:
            raise NoMatchingItems

        return min(rents), sum(rents) / len(rents), max(rents)

    def display_field_table(self, rows: Categories):
        """
        Creates a tabular way of viewing min, avg, max data based on current
        active labels
        :param rows:
        :return: None
        """

        if self._data is None:
            raise EmptyDatasetError

        error = "N/A"

        if rows == DataSet.Categories.LOCATION:
            criteria = self.get_active_labels(DataSet.Categories.PROPERTY_TYPE)
        else:
            criteria = self.get_active_labels(DataSet.Categories.LOCATION)

        print("The following data are from properties matching these "
              "criteria: ")

        for item in criteria:
            print(f"- {item}")

        labels = ["Minimum", "Average", "Maximum"]
        print(f"{'':21}", end='')
        for label in labels:
            print(f"{label:20}", end='')

        print('')
        for item in self.get_labels(rows):
            try:
                data = self._table_statistics(rows, item)
                print(f"{item:<20} $ {data[0]:<17.2f} $ {data[1]:<17.2f} $"
                      f" {data[2]:<17.2f}")
            except NoMatchingItems:
                print(f"{item:<20} $ {error:<17} $ {error:<17} $"
                      f" {error: <17}")

    def load_default_data(self):
        """ Load default data into class"""
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

    def _initialize_sets(self):
        """ initialize the labels"""
        if self._data is None:
            raise EmptyDatasetError

        location_set = set([data[0] for data in self._data])
        property_set = set([data[1] for data in self._data])

        active_location_set = set([data[0] for data in self._data])
        active_property_set = set([data[1] for data in self._data])

        self._labels[DataSet.Categories.LOCATION] = location_set
        self._labels[DataSet.Categories.PROPERTY_TYPE] = property_set

        self._active_labels[DataSet.Categories.LOCATION] = \
            active_location_set
        self._active_labels[DataSet.Categories.PROPERTY_TYPE] = \
            active_property_set

        # print("Labels")
        # print(self._labels)
        # print("Active Labels")
        # print(self._active_labels)

    def display_cross_table(self, stat: Stats):
        """ display cross table to show min, max, and avg data"""
        if self._data is None:
            raise EmptyDatasetError

        # create lists from self._labels dictionary
        locations = []
        for i in self._labels[DataSet.Categories.LOCATION]:
            locations.append(i)

        properties = []
        for i in self._labels[DataSet.Categories.PROPERTY_TYPE]:
            properties.append(i)

        header_column = "Locations"
        error = "N/A"

        # creating header
        print(f"{header_column:20}", end='')

        for i in properties:
            print(f"{i:20}", end='')

        print("")

        for location in locations:
            print(f"{location:20}", end='')
            for some_property in properties:
                try:
                    data = self._cross_table_statistics(location,
                                                        some_property)
                    if stat == DataSet.Stats.MIN:
                        print(f"$ {data[DataSet.Stats.MIN.value]:<18.2f}",
                              end='')
                    elif stat == DataSet.Stats.MAX:
                        print(f"$ {data[DataSet.Stats.MAX.value]:<18.2f}",
                              end='')
                    elif stat == DataSet.Stats.AVG:
                        print(f"$ {data[DataSet.Stats.AVG.value]:<18.2f}",
                              end='')
                    else:
                        print("Not sure what you are looking for")
                except NoMatchingItems:
                    print(f"$ {error:<18}", end='')
            print("")


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
            try:
                dataset.display_cross_table(DataSet.Stats.AVG)
            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()
        elif choice == 2:
            try:
                dataset.display_cross_table(DataSet.Stats.MIN)

            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()
        elif choice == 3:
            try:
                dataset.display_cross_table(DataSet.Stats.MAX)
            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()
        elif choice == 4:
            try:
                dataset.display_field_table(DataSet.Categories.LOCATION)
            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()

        elif choice == 5:
            try:
                dataset.display_field_table(DataSet.Categories.PROPERTY_TYPE)
            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()

        elif choice == 6:
            try:
                manage_filter(dataset, DataSet.Categories.LOCATION)
            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()

        elif choice == 7:
            try:
                manage_filter(dataset, DataSet.Categories.PROPERTY_TYPE)
            except EmptyDatasetError:
                print("Please load a Dataset First")
                print()
        elif choice == 8:
            dataset.load_default_data()
            print("Data loaded")
            dataset._initialize_sets()
            print("Data initialized")
            print()

        elif choice == 9:
            print("Good bye! Thanks for using the database")
            is_user_inputting = False


def manage_filter(dataset: DataSet, category: DataSet.Categories):
    """
    method to print out labels for a given category and determine if active
    or not active
    """
    if dataset._data is None:
        raise EmptyDatasetError

    is_inputting = True

    while is_inputting:
        print("The following labels are in the dataset: ")
        for number, item in enumerate(dataset.get_labels(category), 1):
            if item in dataset.get_active_labels(category):
                state = "ACTIVE"
                print(f"{number}: {item:20} {state}")
            else:
                state = "INACTIVE"
                print(f"{number}: {item:20} {state}")

        choice = input('Please select an item to toggle or enter a blank line \
when you are finished: ')

        if choice == "":
            is_inputting = False
            print()
            print("Moving back to the main screen")
            continue
        elif not choice.isnumeric():
            print("Please enter a number or an empty line to exit")
            continue
        elif int(choice) not in list(range(1, len(dataset.get_labels(category)
                                                  )+1)):
            print("ERROR. Please enter a number from the list")
            continue
        else:
            for number, item in enumerate(dataset.get_labels(category), 1):
                if int(choice) == number:
                    dataset.toggle_active_label(category, item)
                    break
                else:
                    continue


def unit_test():
    data = DataSet()
    data.load_default_data()
    data._initialize_sets()
    data._table_statistics(DataSet.Categories.LOCATION, "Brooklyn")
    data.display_field_table(DataSet.Categories.LOCATION)

    # my_set.display_cross_table(Stats.AVG)


if __name__ == "__main__":
    main()


r"""
Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
What is your home currency? USD
Enter a header for the menu: AirBNB
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
AirBNB
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
What is your choice? 4
Please load a Dataset First

AirBNB
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
What is your choice? 8
Data loaded
Data initialized

AirBNB
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
What is your choice? 4
The following data are from properties matching these criteria: 
- Private room
- Entire home/apt
                     Minimum             Average             Maximum             
Staten Island        $ 70.00             $ 70.00             $ 70.00            
Brooklyn             $ 50.00             $ 118.00            $ 200.00           
Bronx                $ 40.00             $ 40.00             $ 40.00            
Queens               $ 350.00            $ 350.00            $ 350.00           
Manhattan            $ 98.00             $ 143.43            $ 196.00           
AirBNB
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
What is your choice? 5
The following data are from properties matching these criteria: 
- Staten Island
- Brooklyn
- Bronx
- Queens
- Manhattan
                     Minimum             Average             Maximum             
Private room         $ 40.00             $ 86.33             $ 125.00           
Entire home/apt      $ 100.00            $ 181.22            $ 350.00           
AirBNB
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
What is your choice? 6
The following labels are in the dataset: 
1: Staten Island        ACTIVE
2: Brooklyn             ACTIVE
3: Bronx                ACTIVE
4: Queens               ACTIVE
5: Manhattan            ACTIVE
Please select an item to toggle or enter a blank line when you are finished: 1
Staten Island removed from active_labels
The following labels are in the dataset: 
1: Staten Island        INACTIVE
2: Brooklyn             ACTIVE
3: Bronx                ACTIVE
4: Queens               ACTIVE
5: Manhattan            ACTIVE
Please select an item to toggle or enter a blank line when you are finished: 2
Brooklyn removed from active_labels
The following labels are in the dataset: 
1: Staten Island        INACTIVE
2: Brooklyn             INACTIVE
3: Bronx                ACTIVE
4: Queens               ACTIVE
5: Manhattan            ACTIVE
Please select an item to toggle or enter a blank line when you are finished: 

Moving back to the main screen
AirBNB
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
What is your choice? 4
The following data are from properties matching these criteria: 
- Private room
- Entire home/apt
                     Minimum             Average             Maximum             
Staten Island        $ 70.00             $ 70.00             $ 70.00            
Brooklyn             $ 50.00             $ 118.00            $ 200.00           
Bronx                $ 40.00             $ 40.00             $ 40.00            
Queens               $ 350.00            $ 350.00            $ 350.00           
Manhattan            $ 98.00             $ 143.43            $ 196.00           
AirBNB
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
What is your choice? 5
The following data are from properties matching these criteria: 
- Bronx
- Queens
- Manhattan
                     Minimum             Average             Maximum             
Private room         $ 40.00             $ 87.67             $ 125.00           
Entire home/apt      $ 100.00            $ 188.50            $ 350.00           
AirBNB
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
What is your choice? 7
The following labels are in the dataset: 
1: Private room         ACTIVE
2: Entire home/apt      ACTIVE
Please select an item to toggle or enter a blank line when you are finished: 2
Entire home/apt removed from active_labels
The following labels are in the dataset: 
1: Private room         ACTIVE
2: Entire home/apt      INACTIVE
Please select an item to toggle or enter a blank line when you are finished: 

Moving back to the main screen
AirBNB
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
What is your choice? 4
The following data are from properties matching these criteria: 
- Private room
                     Minimum             Average             Maximum             
Staten Island        $ 70.00             $ 70.00             $ 70.00            
Brooklyn             $ 50.00             $ 88.80             $ 120.00           
Bronx                $ 40.00             $ 40.00             $ 40.00            
Queens               $ N/A               $ N/A               $ N/A              
Manhattan            $ 98.00             $ 111.50            $ 125.00           
AirBNB
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
What is your choice? 5
The following data are from properties matching these criteria: 
- Bronx
- Queens
- Manhattan
                     Minimum             Average             Maximum             
Private room         $ 40.00             $ 87.67             $ 125.00           
Entire home/apt      $ 100.00            $ 188.50            $ 350.00           
AirBNB
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
What is your choice? 7
The following labels are in the dataset: 
1: Private room         ACTIVE
2: Entire home/apt      INACTIVE
Please select an item to toggle or enter a blank line when you are finished: 1
Private room removed from active_labels
The following labels are in the dataset: 
1: Private room         INACTIVE
2: Entire home/apt      INACTIVE
Please select an item to toggle or enter a blank line when you are finished: 3
ERROR. Please enter a number from the list
The following labels are in the dataset: 
1: Private room         INACTIVE
2: Entire home/apt      INACTIVE
Please select an item to toggle or enter a blank line when you are finished: 

Moving back to the main screen
AirBNB
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
What is your choice? 4
The following data are from properties matching these criteria: 
                     Minimum             Average             Maximum             
Staten Island        $ N/A               $ N/A               $ N/A              
Brooklyn             $ N/A               $ N/A               $ N/A              
Bronx                $ N/A               $ N/A               $ N/A              
Queens               $ N/A               $ N/A               $ N/A              
Manhattan            $ N/A               $ N/A               $ N/A              
AirBNB
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
What is your choice? 5
The following data are from properties matching these criteria: 
- Bronx
- Queens
- Manhattan
                     Minimum             Average             Maximum             
Private room         $ 40.00             $ 87.67             $ 125.00           
Entire home/apt      $ 100.00            $ 188.50            $ 350.00           
AirBNB
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
