*James Henderson  
8/24/2022  
IT FDN 110 B  
Assignment07*  
[https://github.com/hendej25/IntroToProg-Python-Mod07](https://github.com/hendej25/IntroToProg-Python-Mod07)  
[https://hendej25.github.io/IntroToProg-Python-Mod07/](https://hendej25.github.io/IntroToProg-Python-Mod07/)

# Assignment 7 – Menu Script
## Introduction
For this assignment, I worked to modify an existing script similar to the one that we completed for processing a list of tasks and their priorities. I used the base of that code to represent an interactive restaurant menu that can be edited and saved to a file in a binary format using the pickle module. The script is separated into 3 distinct layers – processing, I/O, and a main code section. The script also has several areas that illustrate the use of error handling in Python.

## Menu Script: Processing Binary Data using Pickle
To accomplish the goals of this assignment, I created a class called PickleJuice which performs the processing tasks. The functions that read / write data out to a flat *.dat file use the pickle module, since that data uses binary formatting; the other functions in this class modify data in the program’s memory.
 
![Figure 1](pictures/1%20-%20PickleJuice%20Class.png "Figure 1")  
***Figure 1* – The processing layer of the script is organized into the PickleJuice class**

In **Figure 2**, you can see how the pickle module is used to read in an entire list of Dictionary objects at once. Even though the load function only loads a single line at a time from the text file, and the menu list may contain multiple objects, the entire list is treated as if it were a single line – so there is no need to iterate through during the load process. Saving the data is equally simple, using the dump function.
 
 ![Figure 2](pictures/2%20-%20Pickling%20%2B%20Unpickling.png "Figure 2")  
***Figure 2* – Using the pickle.load() and pickle.dump() functions to read and write binary data**

## Menu Script: Input / Output
As I mentioned in the introduction section, the script for this assignment has been separated into 3 distinct layers. The Input / Output functions that display data to the user, or take in input from the user, are organized into a Class named “IO”. There are eight functions in all – of these, 2 just display data or choices to the user, while 6 are interactive in that they require some type of input from the user. 
The interactive functions (names beginning with “input_”) return the user input via one or more variables. Within the main code body, these returned values are then handed off to one of the Processor-class functions as needed.
 
![Figure 3](pictures/3%20-%20IO%20-%20Functions.png "Figure 3")  
***Figure 3* – There are 8 different static methods for handling interaction with the user**

One of the areas in the script where error handling is used is inside the print_restaurant_menu function **(Figure 4)**. This function has the ability to sort the menu (which is a list object) by different characteristics of the items on the menu (which are Dictionary keys). However, if the function is passed sort keys that don’t actually correspond to the names of the Dictionary keys in the list, an exception will be raised – the user is notified of the error and no sort is applied.
 
![Figure 4](pictures/4%20-%20IO%20-%20Print%20Menu%20-%20Sort%20Exceptions.png "Figure 4")  
***Figure 4* - Raising an error if invalid sort keys are passed to the print_restaurant_menu function**

## Menu Script: Custom Error Classes
The script also contains a few custom error classes for errors that are explicitly raised in the main code body section **(Figure 5)**:

```python
class UserCancelledNewFileCreation(Exception):
    pass


class InvalidUserMenuChoice(Exception):
    pass


class InvalidSaveChoice(Exception):
    pass
```
***Figure 5* – Custom error classes for better identification of custom errors**

As you can see in **Figure 6**, these classes can be visually helpful for other individuals editing the code to see what the specific error being raised is related to:
```python
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
```
***Figure 6* – Using the custom error classes to raise errors in the main code body**

## Menu Script: Running the Script
To test the script, I first ran the Assignment07.py file within PyCharm, using the latest available Python interpreter on my machine (Python 3.10). 
You can see part of the script’s input / output in process in **Figure 7** below – I intentionally added a bug to the main code body to ask the menu to print on a key that wasn’t one of the Dictionary keys being used for the menu items, to show how the error handling would work. The user is notified of the issue, and the menu is printed with a default sort order (no sort) instead:
 
![Figure 7](pictures/7%20-%20Invalid%20Function%20Argument%20-%20Raising%20a%20Custom%20Error.png "Figure 7")  
***Figure 7* – Testing the error handling when a bug was intentionally added to the code**

I also ran the script from the Windows Command Prompt window **(Figure 8)**. I verified that data from a previous run of the script was correctly picked up at the start of the program. 
 
![Figure 8](pictures/8%20-%20running%20the%20program%20in%20Command%20Prompt.png "Figure 8")  
***Figure 8* – running the script from the Windows command prompt**

## Summary
In this assignment, I edited an existing script to make it work with 3 layers – a processing layer (one class), interactive layer (one class), and a main code body. I made sure that the functions in the script were all appropriately documented with docstrings, and that the code I added was compartmentalized correctly. I also demonstrated the use of pickle to read/write data in a binary format, as well as basic error handling throughout the script.

