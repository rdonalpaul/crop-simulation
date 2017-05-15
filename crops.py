from wheat_class import *
from potato_class import *

def display_menu():
    print()
    print("Please Select a Crop to Grow")
    print("1 - Potato")
    print("2 - Wheat")
    print("Please Select an Option From Above")

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option Selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
 
    
        
