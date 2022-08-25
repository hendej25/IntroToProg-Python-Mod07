# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: This program demonstrates:
#               1) the use of the pickle module, which can convert Python objects
#               into a binary format for storage in a text file ("pickling") as
#               well as read previously-stored binary data that was written to a
#               file with pickle.
#               2) the use of exception handling in Python, which can trap the
#               errors for which the program designer wants to provide a more
#               user-friendly error message, or run additional code in the event
#               the error(s) occur
# ChangeLog (Who,When,What):
# JHenderson,8.22.2022,Created script
# JHenderson, 8.23.2022,Modified code to complete Assignment 07
# ---------------------------------------------------------------------------- #
import pickle

# Data ----------------------------------------------------------------------- #
MENU_FILE_STR = "MenuData.dat"  # The name of the data file
SUCCESS_STR = "Success"  # String indicating a method completed successfully
FAIL_STR = "Fail"  # String indicating a method failed to complete
menu_lst = []  # List object for storing menu data in memory
choice_str = ""  # Captures the user option selection
item_name_str = ""  # Restaurant menu item name
item_price_flt = 0.00  # Restaurant menu item price
item_category_str = ""  # Restaurant menu item category
item_description_str = ""  # Restaurant menu item description


class PickleJuice:
    """  Performs processing tasks using the pickle module """

    @staticmethod
    def create_new_file(file_name):
        """ Creates a new file with the specified name.

        :param file_name: (string) with name of file
        :return:
            status - (string) indicating function status
        """
        file = open(file_name, "wb")  # open the file in write mode then close, to create it
        file.close()
        status = SUCCESS_STR

        return status

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads binary data from a file that was stored with pickle.

        :param file_name: (string) with name of file
        :return:
            menu - (list) of data rows
            status - (string) indicating function status
        """
        menu = []  # initialize menu list
        with open(file_name, "rb") as file:
            menu = (pickle.load(file))
            status = SUCCESS_STR

        return menu, status

    @staticmethod
    def save_data_to_file(file_name, menu):
        """ Saves a binary representation of Python object data into a file using pickle.

        :param file_name: (string) with name of file
        :param menu: (list) containing data to be written out:
        :return:
            menu - (list) of data rows
            status - (string) indicating function status
        """

        with open(file_name, 'wb') as file:
            pickle.dump(menu, file)
            status = SUCCESS_STR

        return menu, status

    @staticmethod
    def add_item_to_menu(name, price, category, description, menu):
        """ Adds a new menu item to the current menu.

        :param name: (string) name of the menu item
        :param price: (float) item price (USD)
        :param category: (string) item category (i.e., appetizers, drinks, entrees, etc.)
        :param description: (string) item description
        :param menu: (list) to which you want to add data
        :return:
            menu - (list) of data rows
            status - (string) indicating function status
        """
        item = {'Name': name, 'Price': price, 'Category': category, 'Description': description}
        menu.append(item)
        status = str(f'{name} (${price:.2f}) was added to the {category} section of the menu.')
        return menu, status

    @staticmethod
    def remove_data_from_menu(name, menu):
        """ Removes a menu item from a list of Dictionary rows.

        :param name: (string) name of the menu item
        :param menu: (list) from which you want to remove data
        :return:
            menu - (list) of data rows
            status - (string) indicating function status
        """
        if name:
            item_found = False
            for item in menu:
                if item['Name'].lower() == name.lower():
                    menu.remove(item)
                    item_found = True

            if item_found:
                status = str(f'{name} was successfully removed from the menu.')
            else:
                status = str(f'{name} was not on the menu, so nothing was removed.')
        else:  # nothing was entered
            status = ''

        return menu, status


class IO:
    """  Performs tasks related to the interactive portion of the program"""

    @staticmethod
    def print_user_choice_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new menu item
        2) Remove an existing menu item
        3) Save menu to file       
        4) Reload menu from file
        5) Exit program
        ''')
        #  print()  # Add an extra line for looks

    @staticmethod
    def create_new_file(file_name):
        """ Asks the user if they would like to create a new menu file with the specified name.

        :param file_name: (string) with name of file
        :return:
            status - (string) indicating function status
        """
        valid_choice = False  # initialize user choice validity variable
        choice = False  # initialize user choice variable
        while not valid_choice:
            choice = IO.input_yes_no_choice("The menu has not been created yet. "
                                            "Would you like to save it to " + " (y/n)? ")
            if choice == "y" or choice == "n":
                valid_choice = True
            else:
                print("Please make a valid selection. ", end="")
                continue

        if choice == "y":  # the user chooses to create the menu file
            PickleJuice.create_new_file(file_name)
            print("File created successfully.")
            status = SUCCESS_STR
        else:  # the user did not choose to create a menu file yet
            status = FAIL_STR

        return status

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing.

        :param optional_message: (string) optional message to display to the user
        :return:
            None
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_user_menu_choice():
        """ Gets the menu choice from a user.

        :return:
            (String) of user input.
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_restaurant_menu(menu, sort_by_key1='', sort_by_key2=''):
        """ Shows the current restaurant menu.

        :param menu: (list) of restaurant menu items
        :param sort_by_key1: (string) optional key to sort by: Name, Price, Category, etc.
        :param sort_by_key2: (string) optional 2nd key to sort by: Name, Price, Category, etc.
        :return:
            None
        """
        #  sort the menu items for display (or not) according to the sort key arguments
        try:
            if sort_by_key1 and not sort_by_key2:
                sorted_menu = sorted(menu, key=lambda d: d[sort_by_key1])
            elif sort_by_key1 and sort_by_key2:
                sorted_menu = sorted(menu, key=lambda elem: "%s %s" % (elem[sort_by_key1], elem[sort_by_key2]))
            else:
                sorted_menu = menu
        except Exception as e:
            print("The program tried to sort the menu items on a characteristic that doesn't exist. "
                  "A default sort order was applied.")
            sorted_menu = menu

        print("******* Here is our current menu: *******")
        category = ""
        for item in sorted_menu:
            if category != item["Category"]:
                category = item["Category"]
                print(category)
                print("*******************************************")

            print(item["Name"] + ' - ' +
                  str(f'${item["Price"]:.0f}') + ' - ' +
                  item["Description"])

            print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user.

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_new_menu_item():
        """ Gets input from the user on a new item to add to the menu.

        :return:
            - (string) menu item name
            - (float) item price
            - (string) item category
            - (string) item description)
        """
        task = input("Please enter a new menu item: ").title()
        price = float(input("Price: "))
        category = input("Category: ").title()
        description = input("Description: ").lower()

        return task, price, category, description

    @staticmethod
    def input_menu_item_to_remove():
        """ Gets input from the user on a menu item to remove.

        :return:
            - (string) menu item name
        """
        item = input('Which menu item would you like to remove? ')
        return item


class UserCancelledNewFileCreation(Exception):
    pass


class InvalidUserMenuChoice(Exception):
    pass


class InvalidSaveChoice(Exception):
    pass


# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, load data from the menu file
try:
    menu_lst, status_str = PickleJuice.read_data_from_file(MENU_FILE_STR)  # read file data
    IO.input_press_to_continue('Data loaded successfully.')

except IOError:  # file does not exist
    try:  # ask the user if they want to create the file
        result = IO.create_new_file(MENU_FILE_STR)
        if result == FAIL_STR:
            raise UserCancelledNewFileCreation("The user chose not to create the menu file.")
        else:
            pass

    except UserCancelledNewFileCreation as e:  # user chose not to create a menu file, program ends
        print("\tBuilt-In Python error info: ")
        print('\tName of the custom exception: ' + str(e), 'Exception docstring: ' + str(e.__doc__),
              'Type of the exception: ' + str(type(e)), sep='\n\t')
        IO.input_press_to_continue("No menu file was created. Thanks for running the program!")

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 - Show current data
    IO.print_restaurant_menu(menu_lst, "Category", "Name")  # Show current restaurant menu, sorted by category
    IO.print_user_choice_menu()  # Shows main menu

    try:
        choice_str = IO.input_user_menu_choice()  # Get user menu selection

        # Step 4 - Process user's menu selection
        if choice_str.strip() == '1':  # Add a new restaurant menu item
            item_name_str, item_price_flt, item_category_str, item_description_str = IO.input_new_menu_item()
            menu_lst, status_str = PickleJuice.add_item_to_menu(item_name_str,
                                                                item_price_flt,
                                                                item_category_str,
                                                                item_description_str,
                                                                menu_lst)
            IO.input_press_to_continue(status_str)
            continue  # to show the user menu

        elif choice_str == '2':  # Remove an existing menu item
            item_name_str = IO.input_menu_item_to_remove()
            menu_lst, status_str = PickleJuice.remove_data_from_menu(item_name_str, menu_lst)
            IO.input_press_to_continue(status_str)
            continue  # to show the user menu

        elif choice_str == '3':  # Save restaurant menu to file

            while True:  # prompt user to save the menu to the file or not
                try:
                    choice_str = IO.input_yes_no_choice("Save this menu to file (binary output)? (y/n) - ")
                    if choice_str == "y":
                        table_lst, status_str = PickleJuice.save_data_to_file(MENU_FILE_STR, menu_lst)
                        IO.input_press_to_continue(status_str)
                        break
                    elif choice_str == "n":
                        IO.input_press_to_continue("Save cancelled!")
                        break
                    else:
                        raise InvalidSaveChoice("Invalid choice")

                except InvalidSaveChoice as e:
                    print("Please enter a valid choice ('y' to save, 'n' to cancel).")

            continue  # to show the user menu

        elif choice_str == '4':  # Reload restaurant menu from file
            print("Warning: Unsaved Data Will Be Lost!")

            while True:  # prompt user to save the menu to the file or not
                try:
                    choice_str = IO.input_yes_no_choice("Are you sure you want to reload the last saved menu? (y/n) - ")
                    if choice_str == "y":
                        menu_lst, status_str = PickleJuice.read_data_from_file(MENU_FILE_STR)
                        IO.input_press_to_continue(status_str)
                        break
                    elif choice_str == "n":
                        IO.input_press_to_continue("File reload cancelled!")
                        break
                    else:
                        raise InvalidSaveChoice("Invalid choice")

                except InvalidSaveChoice as e:
                    print("Please enter a valid choice ('y' to save, 'n' to cancel).")

            continue  # to show the user menu

        elif choice_str == '5':  # Exit Program
            print("Goodbye!")
            break  # and exit

        else:  # prompt the user for a valid menu choice if an invalid choice was entered
            raise InvalidUserMenuChoice("Invalid menu choice.")

    except InvalidUserMenuChoice:  # if invalid choice, let the user know
        print("Please enter a valid choice [1-5].")
