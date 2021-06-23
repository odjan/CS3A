"""
This program extends Assignment One and prompts the user
to select an option from a menu. The core objective is to show
how to use exception handling and handle input
"""


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
    print_menu()

    raw_choice = input("What is your choice? ")

    try:
        choice = int(raw_choice)
    except ValueError:
        print("Next time, please enter a number")
    else:
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
            print("Good bye!")


if __name__ == "__main__":
    main()


r"""
---Sample Run #1: Valid Option---
Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
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
What is your choice? 2
Print Minimum Rent is not ready yet. Stay tuned!


---Sample Run #2: Valid Option---
Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
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
You'll get to load data soon!


---Sample Run #3: Invalid Integer---
Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
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
What is your choice? 11
Please input numbers ranging from 1 to 9


---Sample Run #4: User types something other than an integer---
Please enter your name: Oliver
Hi, Oliver, welcome to Foothill's database project
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
What is your choice? Everything
Next time, please enter a number

"""
